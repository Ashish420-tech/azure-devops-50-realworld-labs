Lab-26: Jenkins Blue-Green Deployment with Kubernetes + GitHub Webhook
🔥 Objective

Implement a real-world Blue-Green Deployment using:

Jenkins Declarative Pipeline

Docker image build & push

Kubernetes (Minikube)

GitHub Webhooks (via ngrok)

Zero-downtime traffic switch

Automatic rollback on failure

This lab simulates production CI/CD behavior, not tutorial shortcuts.

🏗️ Architecture Overview
GitHub Push
   ↓
GitHub Webhook (ngrok)
   ↓
Jenkins Pipeline
   ├─ Build Docker Image
   ├─ Push to Docker Hub
   ├─ Deploy GREEN version to Kubernetes
   ├─ Smoke Test GREEN
   ├─ Switch Service Traffic (BLUE → GREEN)
   └─ Rollback to BLUE on failure

🧩 Folder Structure
lab-26-jenkins-blue-green/
│
├── Jenkinsfile
├── k8s/
│   ├── deployment-blue.yaml
│   ├── deployment-green.yaml
│   └── service.yaml

⚙️ Key Jenkins Pipeline Stages

Checkout Source

Build & Push Docker Image

Deploy GREEN Version

Smoke Test GREEN

Switch Traffic to GREEN

Rollback to BLUE (on failure)

🚨 REAL PROBLEMS FACED & FIXED (IMPORTANT)
❌ Problem 1: GitHub Webhook Returning 404

Error

Response: 404
Ngrok-Error-Code: ERR_NGROK_3200


Root Cause

Jenkins GitHub plugin was installed

❌ Job trigger was NOT enabled

Fix

Job → Configure → Build Triggers
✔ GitHub hook trigger for GITScm polling

❌ Problem 2: Jenkins Still Running Old Lab-23 Pipeline

Root Cause

Jenkins job was pointing to wrong Jenkinsfile

Fix

Pipeline Definition → Pipeline script from SCM
Script Path: lab-26-jenkins-blue-green/Jenkinsfile

❌ Problem 3: kubectl Fails with “Authentication required”

Error

couldn't get current server API group list
Authentication required


Root Cause

Jenkins user had no kubeconfig

Minikube config existed only for ashish user

Fix

sudo -u ashish kubectl get nodes


And in Jenkinsfile:

sudo -u ashish /usr/local/bin/kubectl ...

❌ Problem 4: Jenkins Pipeline Hanging on sudo Password

Error

sudo: a terminal is required to read the password


Root Cause

Jenkins cannot accept interactive sudo

Fix

sudo visudo


Add:

jenkins ALL=(ashish) NOPASSWD: /usr/local/bin/kubectl

❌ Problem 5: Wrong Jenkins Credential Type

Error

Credentials 'dockerhub-creds' is of type 'Username with password'
but StringCredentials was expected


Fix

Use usernamePassword for Docker login

Do NOT use StringCredential for Docker Hub

✅ Final Working Behavior

✔ GitHub push triggers Jenkins automatically
✔ Docker image builds and pushes
✔ GREEN deployment created successfully
✔ Smoke test verifies pods
✔ Service selector switches traffic
✔ Automatic rollback works

🧠 What This Lab Demonstrates (Interview Value)

Real CI/CD debugging under pressure

Jenkins ↔ GitHub webhook internals

Kubernetes authentication handling

Zero-downtime deployment strategy

Safe rollback patterns

🚀 Next Improvements

Canary deployment

Manual approval gates

Slack notifications

Helm-based Blue-Green
