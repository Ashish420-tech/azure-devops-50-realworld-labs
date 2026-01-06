import os

BASE_DIR = "lab-29-jenkins-kubernetes"

FILES = {
    "app/index.html": """<!DOCTYPE html>
<html>
<head>
  <title>Lab 29 - Jenkins Kubernetes</title>
</head>
<body>
  <h1>🚀 Lab 29 Deployed Successfully!</h1>
  <p>CI/CD with Jenkins and Kubernetes</p>
</body>
</html>
""",

    "app/Dockerfile": """FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
""",

    "k8s/deployment.yaml": """apiVersion: apps/v1
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
        image: ashishmondal420/lab29:latest
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

    "Jenkinsfile": """pipeline {
    agent any

    environment {
        IMAGE_NAME = "ashishmondal420/lab29"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ashish420-tech/azure-devops-50-realworld-labs.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest app/'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $IMAGE_NAME:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'kubectl apply -f k8s/'
                }
            }
        }
    }
}
""",

    "README.md": """# Lab 29 – Jenkins + Kubernetes CI/CD

## Objective
Automate Docker build, push, and Kubernetes deployment using Jenkins.

## Tools Used
- Jenkins
- Docker
- Kubernetes
- GitHub

## Pipeline Stages
1. Checkout Code
2. Build Docker Image
3. Push Image to Docker Hub
4. Deploy to Kubernetes

## How to Run
1. Configure Jenkins credentials:
   - dockerhub-creds
   - kubeconfig
2. Create Jenkins pipeline using Jenkinsfile
3. Run the pipeline
4. Access app via NodePort service

## Output
Web page displaying:
🚀 Lab 29 Deployed Successfully!
"""
}

def create_lab():
    print("🚀 Creating Lab 29 structure...")

    for path, content in FILES.items():
        full_path = os.path.join(BASE_DIR, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w") as f:
            f.write(content)

        print(f"✅ Created: {full_path}")

    print("\n🎉 Lab 29 setup completed successfully!")
    print(f"📁 Location: {os.path.abspath(BASE_DIR)}")

if __name__ == "__main__":
    create_lab()
