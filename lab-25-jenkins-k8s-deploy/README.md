📘 Lab 25 – Jenkins Continuous Deployment to Kubernetes (Rolling Update)
📌 Overview

This lab demonstrates a production-style CI/CD pipeline where Jenkins automatically deploys applications to Kubernetes using a RollingUpdate strategy.

The pipeline is:

Triggered automatically via GitHub Webhooks

Builds and pushes Docker images

Deploys to Kubernetes with zero downtime

Verifies rollout status automatically

This lab bridges the gap between basic CI/CD and real-world DevOps deployments.

🏗️ Architecture Flow
Git Push
   ↓
GitHub Webhook
   ↓
Jenkins Pipeline
   ↓
Docker Build & Push
   ↓
Kubernetes Deployment (Rolling Update)
   ↓
Application Verification

🧰 Tools & Technologies Used

Jenkins (Pipeline as Code)

GitHub & Webhooks

Docker & Docker Hub

Kubernetes (Minikube)

kubectl

Linux (WSL / Ubuntu)

📁 Project Structure
lab-25-jenkins-k8s-deploy/
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── Jenkinsfile
└── README.md

⚙️ Kubernetes Configuration
🔹 Deployment (deployment.yaml)

Uses RollingUpdate strategy

Runs 2 replicas

Ensures zero downtime

Key settings:

replicas: 2
strategy:
  type: RollingUpdate

🔹 Service (service.yaml)

Type: NodePort

Exposes application on port 3000

🔁 Jenkins Pipeline Stages
1️⃣ Checkout

Pulls latest code from GitHub repository

2️⃣ Build & Push Image

Builds Docker image

Pushes image securely to Docker Hub using Jenkins credentials

3️⃣ Deploy to Kubernetes (CD)

Applies Kubernetes manifests using kubectl

Triggers rolling update automatically

Uses rollout status for deployment verification

🔐 Jenkins → Kubernetes Access (Local Lab Note)

In a local WSL + Minikube setup, Jenkins runs as a system user and Kubernetes authentication can be complex.

For this lab:

Jenkins executes kubectl using a trusted user context

This approach is acceptable for local labs and interviews

In production (AKS/EKS), Jenkins uses ServiceAccounts

🧪 Verification Steps
Check Jenkins

Jenkins job auto-triggered by webhook

All stages completed successfully

Check Kubernetes
kubectl get deployments
kubectl get pods
kubectl get svc

Access Application
minikube service lab25-jenkins-service --url


Expected output:

Application response is successful

🧠 Key Learnings

Difference between Docker-only CD and Kubernetes CD

Jenkins + Kubernetes integration

RollingUpdate for zero-downtime deployments

Handling Jenkins authentication in local environments

Real-world CI/CD pipeline structure

📈 Interview-Ready Statement

“I built a Jenkins CI/CD pipeline triggered by GitHub webhooks that builds Docker images and deploys them to Kubernetes using rolling updates.”

✅ Lab Status

✔ Jenkins CI
✔ GitHub Webhook Automation
✔ Docker Build & Push
✔ Kubernetes Deployment
✔ Rolling Update Strategy

🚀 Next Labs

Blue-Green deployment on Kubernetes

Jenkins CI/CD on Azure Kubernetes Service (AKS)

Monitoring Jenkins & Kubernetes with Prometheus and Grafana

Author: Ashish Mondal
Track: Azure DevOps & Jenkins Real-World Labs
