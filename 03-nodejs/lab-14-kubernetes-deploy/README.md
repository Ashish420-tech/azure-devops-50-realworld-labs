📘 Lab-14: Kubernetes Deployment via Azure DevOps (Troubleshooting Guide)
🔥 Lab Objective

Deploy a Node.js application to Kubernetes (Minikube) using an Azure DevOps self-hosted Windows agent, and troubleshoot real-world CI/CD and Kubernetes issues.

🧩 Environment Details
Component	Value
OS	Windows 10
CI Tool	Azure DevOps Pipelines
Agent Type	Self-hosted Windows Agent
Kubernetes	Minikube (Docker driver)
Runtime	Docker Desktop
App	Node.js
Exposure	NodePort / Port-Forward
❌ Issue 1: error: current-context is not set
🔍 Symptom
error: current-context is not set
Authentication required

🧠 Root Cause

Minikube was initially created inside WSL

Azure DevOps agent runs on Windows

Kubernetes kubeconfig is OS & user specific

✅ Fix

Install Minikube on Windows

Start Minikube using Docker driver

Copy kubeconfig for SYSTEM user

minikube start --driver=docker

mkdir C:\Windows\System32\config\systemprofile\.kube
copy C:\Users\Ashish\.kube\config C:\Windows\System32\config\systemprofile\.kube\config

❌ Issue 2: EOF / API Server Unreachable
🔍 Symptom
couldn't get current server API group list: EOF

🧠 Root Cause

Minikube host was running

Kubernetes control plane was stopped

✅ Fix

Recreate the cluster completely:

minikube delete --all --purge
minikube start --driver=docker --force


Verification:

minikube status
kubectl get nodes

❌ Issue 3: ErrImagePull / ImagePullBackOff
🔍 Symptom
Failed to pull image "lab14-nodejs:latest"
repository does not exist or may require 'docker login'

🧠 Root Cause

Docker image built on host Docker

Minikube has its own Docker daemon

Kubernetes could not see the image

✅ Correct Fix (CI-SAFE): minikube image load
🔑 Key Insight

Azure DevOps runs each script step in a new shell.
Docker environment variables do not persist across steps.

✅ Final Working Pipeline Solution

Build image normally → explicitly load it into Minikube.

- script: |
    cd 03-nodejs/lab-14-kubernetes-deploy/app
    docker build -t lab14-nodejs:latest .
  displayName: "Build Docker Image"

- script: |
    minikube image load lab14-nodejs:latest
  displayName: "Load Image into Minikube"

❌ Issue 4: Pod Running but Portal Not Opening
🔍 Symptom

Pod status: Running

Service exists

Browser does not open

🧠 Root Cause

NodePort is unreliable on Minikube + Windows + Docker driver

This is a known Minikube limitation

✅ Guaranteed Access Method: Port-Forward
🔑 Debug & Demo Command
kubectl port-forward deployment/lab14-nodejs-deployment 3000:3000


Access in browser:

http://localhost:3000


✅ Portal opens successfully

❌ Issue 5: Cannot curl inside container
🔍 Symptom
exec: "curl": executable file not found

🧠 Root Cause

Node.js base images do not include curl

✅ Correct Debug Approach

Use logs and port-forward instead:

kubectl logs <pod-name>
kubectl port-forward deployment/<deployment> 3000:3000

✅ Final Validation Checklist

✔ Azure DevOps pipeline green
✔ Docker image built successfully
✔ Image loaded into Minikube
✔ Pod status: Running
✔ App logs show server started
✔ Portal accessible via port-forward

🧠 Interview-Ready Learnings

Kubernetes images must be available to the cluster runtime

Minikube uses its own Docker daemon

Azure DevOps script steps are isolated shells

minikube image load is CI-safe and reliable

Port-forward is the fastest way to validate app health

Pod Running ≠ App reachable

🏁 Conclusion

This lab demonstrated real-world DevOps troubleshooting, covering:

OS mismatch (WSL vs Windows)

Kubernetes authentication

ImagePullBackOff errors

CI pipeline isolation behavior

Minikube networking limitations

This is production-grade Kubernetes + CI/CD knowledge, not tutorial-level.
