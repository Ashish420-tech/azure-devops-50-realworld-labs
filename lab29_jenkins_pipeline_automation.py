import os
import subprocess
import sys
import requests
from requests.auth import HTTPBasicAuth

# ================= USER CONFIG =================
JENKINS_URL = "http://localhost:8080"
JENKINS_USER = "admin"
JENKINS_API_TOKEN = "YOUR_API_TOKEN"

JOB_NAME = "lab-29-jenkins-kubernetes"
GIT_REPO = "https://github.com/Ashish420-tech/azure-devops-50-realworld-labs.git"
BRANCH = "main"

LAB_DIR = "lab-29-jenkins-kubernetes"
JENKINSFILE_PATH = f"{LAB_DIR}/Jenkinsfile"
COMMIT_MSG = "Lab 29: Auto Jenkinsfile + Pipeline creation"

# ================= UTIL =================
def run_cmd(cmd, error_msg):
    try:
        result = subprocess.run(
            cmd, shell=True, check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"\n❌ {error_msg}")
        print(e.stderr)
        sys.exit(1)

# ================= STEP 1: VALIDATE GIT =================
def validate_git():
    if not os.path.isdir(".git"):
        print("❌ Not a git repository")
        sys.exit(1)

    if not os.path.isdir(LAB_DIR):
        print(f"❌ {LAB_DIR} folder not found")
        sys.exit(1)

# ================= STEP 2: CREATE JENKINSFILE =================
def create_jenkinsfile():
    os.makedirs(LAB_DIR, exist_ok=True)

    jenkinsfile = """pipeline {
    agent any

    environment {
        IMAGE = "ashishmondal420/lab29"
        TAG = "v1"
        RELEASE = "lab29"
        CHART = "helm/lab29"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ashish420-tech/azure-devops-50-realworld-labs.git'
            }
        }

        stage('Build & Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'U',
                    passwordVariable: 'P'
                )]) {
                    sh '''
                    docker build -t $IMAGE:$TAG app/
                    echo $P | docker login -u $U --password-stdin
                    docker push $IMAGE:$TAG
                    '''
                }
            }
        }

        stage('Deploy with Helm') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'helm upgrade --install $RELEASE $CHART'
                }
            }
        }
    }

    post {
        success { echo "✅ Deployment successful" }
        failure { echo "❌ Deployment failed" }
    }
}
"""
    try:
        with open(JENKINSFILE_PATH, "w") as f:
            f.write(jenkinsfile)
        print("✅ Jenkinsfile created")
    except Exception as e:
        print("❌ Failed to write Jenkinsfile")
        print(e)
        sys.exit(1)

# ================= STEP 3: GIT PUSH =================
def git_push():
    run_cmd(f"git add {LAB_DIR}", "Git add failed")

    status = run_cmd("git status --porcelain", "Git status failed")
    if status:
        run_cmd(f'git commit -m "{COMMIT_MSG}"', "Git commit failed")
        print("✅ Git commit done")
    else:
        print("⚠️ No changes to commit")

    branch = run_cmd("git branch --show-current", "Branch detection failed")
    run_cmd(f"git push origin {branch}", "Git push failed")
    print("✅ Code pushed to GitHub")

# ================= STEP 4: CREATE JENKINS PIPELINE =================
def create_jenkins_job():
    job_config = f"""
<flow-definition plugin="workflow-job">
  <description>Auto-created Jenkins Pipeline for Lab 29</description>
  <definition class="org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition">
    <scm class="hudson.plugins.git.GitSCM">
      <userRemoteConfigs>
        <hudson.plugins.git.UserRemoteConfig>
          <url>{GIT_REPO}</url>
        </hudson.plugins.git.UserRemoteConfig>
      </userRemoteConfigs>
      <branches>
        <hudson.plugins.git.BranchSpec>
          <name>*/{BRANCH}</name>
        </hudson.plugins.git.BranchSpec>
      </branches>
    </scm>
    <scriptPath>{LAB_DIR}/Jenkinsfile</scriptPath>
    <lightweight>true</lightweight>
  </definition>
</flow-definition>
"""

    url = f"{JENKINS_URL}/createItem?name={JOB_NAME}"

    response = requests.post(
        url,
        data=job_config,
        headers={"Content-Type": "application/xml"},
        auth=HTTPBasicAuth(JENKINS_USER, JENKINS_API_TOKEN)
    )

    if response.status_code == 200:
        print("✅ Jenkins Pipeline Job created")
    elif response.status_code == 400:
        print("⚠️ Jenkins job already exists")
    else:
        print("❌ Jenkins job creation failed")
        print(response.text)
        sys.exit(1)

# ================= MAIN =================
def main():
    print("\n🚀 Lab 29 Jenkins Automation Started\n")

    validate_git()
    create_jenkinsfile()
    git_push()
    create_jenkins_job()

    print("\n🎉 COMPLETE: Jenkinsfile + Pipeline fully automated")

if __name__ == "__main__":
    main()
