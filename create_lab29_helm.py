import os

print("\n🚀 Jenkins + Kubernetes + Helm Lab Generator\n")

docker_user = input("DockerHub username: ").strip()
image_name = input("Docker image name: ").strip()
image_tag = input("Docker image tag: ").strip()

BASE_DIR = "lab-29-jenkins-kubernetes"
FULL_IMAGE = f"{docker_user}/{image_name}:{image_tag}"

FILES = {

# ================= APP =================
"app/index.html": f"""<!DOCTYPE html>
<html>
<head>
  <title>Lab 29 Helm</title>
</head>
<body>
  <h1>🚀 Deployed using Jenkins + Helm</h1>
  <p>Image: {FULL_IMAGE}</p>
</body>
</html>
""",

"app/Dockerfile": """FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
""",

# ================= HELM =================
"helm/lab29/Chart.yaml": """apiVersion: v2
name: lab29
description: Jenkins + Helm Kubernetes Deployment
type: application
version: 0.1.0
appVersion: "1.0"
""",

"helm/lab29/values.yaml": f"""replicaCount: 2

image:
  repository: {docker_user}/{image_name}
  tag: {image_tag}

service:
  type: NodePort
  port: 80
""",

"helm/lab29/templates/deployment.yaml": """apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}
    spec:
      containers:
      - name: app
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        ports:
        - containerPort: 80
""",

"helm/lab29/templates/service.yaml": """apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}
spec:
  type: {{ .Values.service.type }}
  selector:
    app: {{ .Release.Name }}
  ports:
  - port: {{ .Values.service.port }}
    targetPort: 80
""",

# ================= JENKINS =================
"Jenkinsfile": f"""pipeline {{
    agent any

    environment {{
        IMAGE = "{docker_user}/{image_name}"
        TAG   = "{image_tag}"
    }}

    stages {{

        stage('Checkout') {{
            steps {{
                git branch: 'main',
                url: 'https://github.com/Ashish420-tech/azure-devops-50-realworld-labs.git'
            }}
        }}

        stage('Build Image') {{
            steps {{
                sh 'docker build -t $IMAGE:$TAG app/'
            }}
        }}

        stage('Push Image') {{
            steps {{
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'U',
                    passwordVariable: 'P'
                )]) {{
                    sh '''
                    echo $P | docker login -u $U --password-stdin
                    docker push $IMAGE:$TAG
                    '''
                }}
            }}
        }}

        stage('Deploy via Helm') {{
            steps {{
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {{
                    sh '''
                    helm upgrade --install lab29 helm/lab29
                    '''
                }}
            }}
        }}
    }}
}}
""",

# ================= README =================
"README.md": f"""# Lab 29 – Jenkins + Helm Kubernetes Deployment

## Objective
Automate Docker build and Kubernetes deployment using Jenkins and Helm.

## Image
{FULL_IMAGE}

## Flow
Git → Jenkins → Docker → Helm → Kubernetes

## Helm Benefits
- Versioned deployments
- Easy rollback
- Environment-based configs

## Interview Highlight
Python-based automation to generate CI/CD and Helm charts.
"""
}

def create_lab():
    print("\n📁 Creating Lab structure...\n")

    for path, content in FILES.items():
        full_path = os.path.join(BASE_DIR, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w") as f:
            f.write(content)

        print(f"✅ {full_path}")

    print("\n🎉 Lab with Helm created successfully!")
    print("🚀 Ready for Lab 30 interviews")

if __name__ == "__main__":
    create_lab()
