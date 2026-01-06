🚀 Project: Jenkins CI/CD Blue-Green Deployment on Kubernetes

This lab demonstrates a real-world Blue-Green deployment strategy using Jenkins, Docker, and Kubernetes (Minikube) to achieve zero-downtime releases with instant rollback capability.

🎯 Objective

Automate Docker image build & push using Jenkins

Deploy applications to Kubernetes using Blue-Green strategy

Switch live traffic without downtime

Perform instant rollback using Kubernetes Service selector

🧠 What is Blue-Green Deployment?

Blue-Green deployment runs two identical environments:

🔵 BLUE → current production version

🟢 GREEN → new release version

Traffic is controlled by a Kubernetes Service selector, enabling:

Zero downtime

Safe releases

Immediate rollback

🧩 Architecture Overview
📁 Repository Structure
lab-27-jenkins-blue-green/
├── Jenkinsfile
├── app/
│   ├── Dockerfile
│   └── index.html
└── k8s/
    ├── blue-deployment.yaml
    ├── green-deployment.yaml
    └── service.yaml

🛠️ Tools & Technologies Used

Jenkins (Declarative Pipeline)

Docker & DockerHub

Kubernetes (Minikube)

NGINX

Linux (WSL)

⚙️ Jenkins Pipeline Stages

Checkout Code

Build Docker Image (GREEN)

Push Image to DockerHub

Deploy GREEN to Kubernetes

Switch Traffic to GREEN

Post-deployment status

🔄 Rollback Strategy (Step-5)

Rollback is achieved without redeploying anything:

kubectl patch svc web-service \
-p '{"spec":{"selector":{"app":"web","version":"blue"}}}'


✔ Instant
✔ Zero downtime
✔ Production-safe

🧪 Verification
minikube service web-service


Expected:

GREEN version after deployment

BLUE version after rollback

🧠 Key Learnings

Jenkins–Kubernetes authentication via kubeconfig

Real Blue-Green traffic switching

Handling production-like permission issues

Designing rollback-ready pipelines

🏆 Outcome

✔ End-to-end CI/CD pipeline
✔ Zero-downtime deployment
✔ Enterprise-grade rollback strategy

📌 Interview-Ready Statement

“I implemented a Jenkins-driven Blue-Green deployment on Kubernetes with zero downtime and instant rollback using Service selector switching.”
