🚀 Lab-30: Argo CD GitOps Deployment (Azure DevOps Journey)
📌 Overview

This lab demonstrates a GitOps-based Continuous Delivery (CD) workflow using Argo CD and Kubernetes.

Instead of deploying applications using kubectl apply, the entire deployment is controlled by Git, and Argo CD continuously reconciles the Kubernetes cluster state with the desired state defined in the repository.

This lab is part of the azure-devops-50-realworld-labs series and represents a modern, production-aligned CD approach.

🎯 Objectives

Understand GitOps principles

Deploy applications using Argo CD

Use Git as the single source of truth

Observe sync, health, drift detection, and reconciliation

Gain interview-ready, real-world experience

🧠 Architecture (High Level)
Git Repository
   └── Kubernetes Manifests
           ↓
        Argo CD
           ↓
     Kubernetes Cluster


CI: Azure DevOps / Jenkins (out of scope for this lab)

CD: Argo CD (GitOps – pull-based)

Platform: Kubernetes (Minikube / AKS-ready)

📁 Repository Structure
lab-30-argocd-gitops/
├── deployment.yaml
├── service.yaml
└── README.md

📄 Kubernetes Manifests
🔹 deployment.yaml

Deploys an Nginx application

Maintains desired replica count

Ensures self-healing via Kubernetes Deployment controller

Key features:

Declarative desired state

Version-controlled scaling

Managed entirely by Argo CD

🔹 service.yaml

Exposes the application using NodePort

Routes traffic using label selectors

Provides stable networking despite pod restarts

🔄 GitOps Workflow

Developer updates Kubernetes YAML in Git

Changes are committed and pushed

Argo CD detects the difference (OutOfSync)

Argo CD reconciles the cluster state

Application reaches Healthy & Synced state

🚫 No manual kubectl apply
✅ Git controls everything

🟢 Application Status (Argo CD)

Sync Status: Synced

Health Status: Healthy

Target Branch: main

Watched Path: lab-30-argocd-gitops

This confirms a successful GitOps deployment.

🔁 Scaling Example (GitOps in Action)

To scale the application:

replicas: 2 → replicas: 3


Steps:

Update deployment.yaml

Commit and push to Git

Argo CD detects and applies the change automatically

This demonstrates Git-driven operational changes.

🔙 Rollback Strategy

Rollback is performed by reverting a Git commit:

git revert <commit-id>
git push origin main


Argo CD automatically restores the previous stable state.

✔ No rollback commands
✔ No cluster access required

🧠 Key Learnings

GitOps is pull-based, not push-based

Argo CD continuously reconciles desired state

Git history = deployment history

Rollbacks are safe, auditable, and simple

This model is widely used in modern Kubernetes platforms
