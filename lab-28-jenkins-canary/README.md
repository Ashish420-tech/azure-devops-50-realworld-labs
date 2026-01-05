Jenkins Canary Deployment on Kubernetes
🔷 Lab Name

Lab-28: Jenkins Canary Deployment using Kubernetes

🎯 Objective

Implement a Canary Deployment strategy using Jenkins CI/CD, Docker, and Kubernetes, where:

Stable version continues serving most traffic

Canary version receives limited traffic

Rollback is instant if canary fails

🧱 Tech Stack

Jenkins (Declarative Pipeline)

Docker & Docker Hub

Kubernetes (Minikube)

NGINX (Stable + Canary)

WSL (Linux environment)

📂 Project Structure
lab-28-jenkins-canary/
├── Jenkinsfile
├── README.md
├── app/
│   ├── Dockerfile
│   └── index.html
└── k8s/
    ├── stable-deployment.yaml
    ├── canary-deployment.yaml
    └── service.yaml

🔁 Canary Deployment Flow

Build Docker image for Canary

Push image to Docker Hub

Deploy Stable version (100% traffic initially)

Deploy Canary version (small replica count)

Service routes traffic to both versions

Monitor pods & traffic

Rollback instantly if Canary fails

⚙️ Jenkins Pipeline Stages

Checkout SCM

Build Canary Docker Image

Push Image to Docker Hub

Deploy Stable to Kubernetes

Deploy Canary to Kubernetes

Post-deployment verification

🔍 Verification Steps
Check Pods
kubectl get pods


Expected:

stable-nginx-xxxxx   Running
canary-nginx-xxxxx   Running

Check Service
kubectl get svc web-service

Test Traffic
minikube service web-service --url
curl <URL>


Responses should alternate between Stable and Canary.

🔙 Rollback Strategy

If Canary shows errors:

kubectl scale deployment canary-nginx --replicas=0


Traffic automatically returns to Stable only.

🧠 Key Learnings

Real-world Canary deployment workflow

Jenkins → Docker → Kubernetes integration

Safe production release strategy explained

Zero-downtime rollout & rollback

✅ Status

✔ Pipeline executed successfully
✔ Stable & Canary pods running
✔ Traffic verified
✔ Rollback tested

📌 Why Canary Deployment?

Canary deployment reduces production risk by exposing new versions to limited users before full rollout.
