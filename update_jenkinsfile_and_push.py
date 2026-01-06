import os
import subprocess
import sys

# ================= CONFIG =================
LAB_DIR = "lab-29-jenkins-kubernetes"
JENKINSFILE_PATH = os.path.join(LAB_DIR, "Jenkinsfile")
COMMIT_MSG = "Lab 29: Update Jenkinsfile (auto)"

# ================= JENKINSFILE CONTENT =================
JENKINSFILE_CONTENT = """pipeline {
    agent any

    environment {
        IMAGE   = "ashishmondal420/lab29"
        TAG     = "v1"
        RELEASE = "lab29"
        CHART   = "helm/lab29"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Push Docker Image') {
            steps {
                dir('lab-29-jenkins-kubernetes') {
                    withCredentials([usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        sh '''
                        docker build -t $IMAGE:$TAG app
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $IMAGE:$TAG
                        '''
                    }
                }
            }
        }

        stage('Deploy with Helm') {
            steps {
                dir('lab-29-jenkins-kubernetes') {
                    withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                        sh '''
                        helm upgrade --install $RELEASE $CHART \\
                          --set image.repository=$IMAGE \\
                          --set image.tag=$TAG
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Lab 29 deployment successful"
        }
        failure {
            echo "❌ Lab 29 deployment failed"
        }
    }
}
"""

# ================= UTIL =================
def run_cmd(cmd, error_msg):
    try:
        output = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT
        ).decode().strip()
        return output
    except subprocess.CalledProcessError as e:
        print(f"\n❌ {error_msg}")
        print(e.output.decode())
        sys.exit(1)

# ================= MAIN =================
def main():
    print("\n🚀 Updating Jenkinsfile and pushing to GitHub\n")

    # 1️⃣ Validate git repo
    if not os.path.isdir(".git"):
        print("❌ ERROR: Not inside a git repository")
        sys.exit(1)

    # 2️⃣ Validate lab directory
    if not os.path.isdir(LAB_DIR):
        print(f"❌ ERROR: {LAB_DIR} directory not found")
        sys.exit(1)

    # 3️⃣ Create / Update Jenkinsfile
    try:
        with open(JENKINSFILE_PATH, "w") as f:
            f.write(JENKINSFILE_CONTENT)
        print("✅ Jenkinsfile updated")
    except Exception as e:
        print("❌ Failed to write Jenkinsfile")
        print(e)
        sys.exit(1)

    # 4️⃣ Git add
    run_cmd(f"git add {JENKINSFILE_PATH}", "Git add failed")
    print("✅ Git add successful")

    # 5️⃣ Commit if changes exist
    status = run_cmd("git status --porcelain", "Git status failed")
    if status:
        run_cmd(f'git commit -m "{COMMIT_MSG}"', "Git commit failed")
        print("✅ Git commit created")
    else:
        print("⚠️ No changes to commit")

    # 6️⃣ Detect branch
    branch = run_cmd(
        "git branch --show-current",
        "Failed to detect current branch"
    )

    # 7️⃣ Push
    run_cmd(
        f"git push origin {branch}",
        "Git push failed (auth or branch issue)"
    )

    print("\n🎉 SUCCESS")
    print(f"📦 Jenkinsfile updated and pushed to branch: {branch}")

if __name__ == "__main__":
    main()
