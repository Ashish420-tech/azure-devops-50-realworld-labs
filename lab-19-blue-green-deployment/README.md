Lab-19: Blue-Green Deployment on Kubernetes using Azure DevOps (WSL Agent)
📌 Objective

Implement Blue-Green deployment on Kubernetes using Azure DevOps pipelines, ensuring zero downtime traffic switching between application versions.

This lab simulates real-world DevOps challenges involving:

Self-hosted Azure DevOps agents

Kubernetes (Minikube)

OS and tooling alignment (Windows vs WSL)

CI/CD pipeline troubleshooting

🧱 Architecture Used
WSL (Ubuntu)
 ├── Minikube (Kubernetes cluster)
 ├── kubectl
 ├── Azure DevOps Linux Agent (self-hosted)
 └── Azure DevOps Pipeline (bash)


⚠️ Windows agent was intentionally avoided due to kubeconfig and certificate path issues.

🛠️ Tools & Versions

Azure DevOps (YAML pipeline)

Kubernetes (Minikube)

kubectl

WSL Ubuntu

Azure DevOps Linux Agent (self-hosted)

📂 Repository Structure
lab-19-blue-green-deployment/
├── azure-pipelines.yml
└── k8s/
    ├── deployment-blue.yaml
    ├── deployment-green.yaml
    └── service.yaml

🚀 Blue-Green Deployment Flow

Deploy BLUE version

Deploy GREEN version

Switch Service selector from BLUE → GREEN

Verify traffic is routed to GREEN pods

⚙️ Azure Pipeline (Linux / WSL)

Key characteristics:

Uses bash, not PowerShell

Runs on Linux (WSL) self-hosted agent

Uses native kubectl and sed

trigger: none

pool:
  name: Default

stages:
- stage: Deploy_Blue
  jobs:
  - job: Blue
    steps:
    - checkout: self
    - bash: |
        kubectl apply -f k8s/deployment-blue.yaml
        kubectl apply -f k8s/service.yaml
      workingDirectory: lab-19-blue-green-deployment

- stage: Deploy_Green
  dependsOn: Deploy_Blue
  jobs:
  - job: Green
    steps:
    - checkout: self
    - bash: |
        kubectl apply -f k8s/deployment-green.yaml
      workingDirectory: lab-19-blue-green-deployment

- stage: Switch_Traffic
  dependsOn: Deploy_Green
  jobs:
  - job: Switch
    steps:
    - checkout: self
    - bash: |
        sed -i 's/version: blue/version: green/' k8s/service.yaml
        kubectl apply -f k8s/service.yaml
      workingDirectory: lab-19-blue-green-deployment

🧨 Major Issues Faced & Fixes
❌ Issue 1: Windows Agent + WSL Kubernetes Mismatch

Error:

kubectl failed: authentication required


Root Cause:

Minikube running in WSL

Azure DevOps agent running on Windows

kubeconfig paths incompatible (/home/... vs C:\Users\...)

Fix:
✅ Installed Linux Azure DevOps agent inside WSL
✅ Stopped Windows agent

❌ Issue 2: kubectl Not Found in Pipeline

Error:

Program 'kubectl' failed to run


Root Cause:

Windows PowerShell pipeline

kubectl installed only in WSL

Fix:
✅ Switched pipeline to Linux agent + bash

❌ Issue 3: Azure DevOps Agent Offline

Error:

Linux agent offline


Root Cause:

Agent installed but run.sh not running

Terminal closed

Fix Commands:

cd ~/azagent
chmod +x run.sh config.sh
./run.sh


⚠️ Terminal must stay open.

❌ Issue 4: DNS Failure in WSL

Error:

curl: Could not resolve host azureedge.net


Root Cause:

WSL DNS auto-generation issue

Fix:

# Windows PowerShell (Admin)
notepad C:\Users\<user>\.wslconfig

[wsl2]
generateResolvConf=false

wsl --shutdown

# WSL
sudo rm /etc/resolv.conf
echo -e "nameserver 8.8.8.8\nnameserver 1.1.1.1" | sudo tee /etc/resolv.conf

❌ Issue 5: Azure DevOps Agent Already Exists

Error:

Agent name already exists


Fix:

Used unique agent name

Replaced stale registration safely

Enter replace? Y
Agent name: wsl-agent

🧪 Verification Commands
kubectl get nodes
kubectl get pods -n bluegreen
kubectl get svc -n bluegreen

✅ Final Result

✔ Azure DevOps pipeline running on WSL Linux agent

✔ Blue & Green deployments successful

✔ Traffic switched without downtime

✔ Real-world CI/CD troubleshooting completed

🧠 Key Learnings (Interview-Ready)

Azure DevOps agent OS must match Kubernetes runtime

Windows + WSL mixing causes kubeconfig & cert issues

Self-hosted Linux agents are ideal for Kubernetes pipelines

DNS & agent registration issues are common in real projects

🏁 Status

Lab-19: COMPLETED SUCCESSFULLY ✅
