import os

print("🚀 Jenkins + Kubernetes Lab 29 Generator\n")

docker_user = input("Enter DockerHub username: ").strip()
image_name = input("Enter Docker image name (example: lab29): ").strip()
image_tag = input("Enter image tag (example: latest): ").strip()

BASE_DIR = "lab-29-jenkins-kubernetes"
FULL_IMAGE = f"{docker_user}/{image_name}:{image_tag}"

FILES = {
    "app/index.html": f"""<!DOCTYPE html>
<html>
<head>
  <title>Lab 29 - Jenkins Kubernetes</title>
</head>
<body>
  <h1>🚀 Lab 29 Deployed Successfully!</h1>
  <p>Docker Image: {FULL_IMAGE}</p>
</body>
</html>
""",

    "app/Dockerfile": """FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
""",

    "k8s/deployment.yaml": f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: lab29-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: lab29
  template:
    metadata:
      labels:
        app: lab29
    spec:
      containers:
      - name: lab29-container
        image: {FULL_IMAGE}
        ports:
        - containerPort: 80
""",

    "k8s/service.yaml": """apiVersion: v1
kind: Service
metadata:
  name: lab29-service
spec:
  type: NodePort
  selector:
    app: lab29
  ports:
  - port: 80
    targetPort: 80
""",

    "Jenkinsfile": f"""pipeline {{
    agent any

    environment {{
        IMAGE_NAME = "{docker_user}/{image_name}"
        IMAGE_TAG  = "{image_tag}"
    }}

    stages {{

        stage('Checkout Code') {{
            steps {{
                git branch: 'main',
                    url: 'https://github.com/Ashish420-tech/azure-devops-50-realworld-labs.git'
            }}
        }}

        stage('Build Docker Image') {{
            steps {{
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG app/'
            }}
        }}

        stage('Push Image') {{
            steps {{
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {{
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $IMAGE_NAME:$IMAGE_TAG
                    '''
                }}
            }}
        }}

        stage('Deploy to Kubernetes') {{
            steps {{
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {{
                    sh 'kubectl apply -f k8s/'
                }}
            }}
        }}
    }}
}}
""",

    "README.md": f"""# Lab 29 – Jenkins + Kubernetes CI/CD (Dynamic)

## Objective
Automate Docker build, push, and Kubernetes deployment using Jenkins.

## Docker Image
**{FULL_IMAGE}**

## Tools Used
- Jenkins
- Docker
- Kubernetes
- GitHub
- Python Automation

## Pipeline Stages
1. Checkout Code
2. Build Docker Image
3. Push Image to Docker Hub
4. Deploy to Kubernetes

## Key Learning
- Dynamic CI/CD configuration
- Secure credential handling
- Kubernetes deployment automation
"""
}

def create_lab():
    print("\n📁 Creating Lab 29 structure...\n")

    for path, content in FILES.items():
        full_path = os.path.join(BASE_DIR, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w") as f:
            f.write(content)

        print(f"✅ Created: {full_path}")

    print("\n🎉 Lab 29 created successfully!")
    print(f"📦 Docker Image: {FULL_IMAGE}")
    print(f"📍 Path: {os.path.abspath(BASE_DIR)}")

if __name__ == "__main__":
    create_lab()
