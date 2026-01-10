# Enterprise GitOps DevOps Project 🚀

## Overview
This project demonstrates an **end-to-end, enterprise-grade DevOps platform** built using modern DevOps and GitOps practices.  
It integrates **CI, Infrastructure as Code, Kubernetes, GitOps, Security, and Monitoring** into a single cohesive system.

The project is implemented **inside an existing lab repository** to reflect real-world evolution of DevOps systems rather than greenfield demos.

---

## 🎯 Project Goals
- Implement a **production-style CI/CD pipeline**
- Provision infrastructure using **Terraform (Azure VM)**
- Package and deploy applications using **Docker & Kubernetes**
- Manage deployments using **GitOps (Argo CD)**
- Apply **security best practices**
- Enable **monitoring and observability**
- Follow **real enterprise workflows**

---

## 🏗️ High-Level Architecture

Developer
↓
GitHub Repository
↓
Azure DevOps (CI Pipeline)
├─ Docker Build
├─ Image Security Scan
↓
Container Registry
↓
GitOps Repository (Helm)
↓
Argo CD
↓
Kubernetes Cluster
├─ RBAC
├─ Secrets
├─ Network Policies
├─ Prometheus
└─ Grafana


Additionally:



Terraform
↓
Azure Virtual Machine (CI / Bastion / Management Node)


---

## 📁 Repository Structure



enterprise-gitops-project/
├── app/ # Application source code
│ ├── index.html
│ └── Dockerfile
├── ci/ # CI pipeline definitions
│ └── azure-pipelines.yml
├── terraform/ # Azure infrastructure provisioning
│ ├── main.tf
│ ├── variables.tf
│ └── outputs.tf
├── k8s/ # Raw Kubernetes manifests
├── helm/ # Helm charts (GitOps-ready)
├── docs/ # Architecture & documentation
└── README.md


---

## 🔁 CI – Continuous Integration

**Tool:** Azure DevOps  

### CI Capabilities:
- Triggered on every commit to `main`
- Builds Docker image using a minimal base image
- Tags images with immutable versions
- (Later stages) Security scanning before promotion

**Why this matters:**
- Ensures repeatable and consistent builds
- Prevents “works on my machine” issues
- Enables fast rollback

---

## 🧱 Infrastructure as Code – Terraform (Azure VM)

**Tool:** Terraform  
**Platform:** Microsoft Azure  

### What We Provision:
- Azure Resource Group
- Virtual Network & Subnet
- Network Security Group
- Azure Linux Virtual Machine

### Why Azure VM is Included:
- Acts as a **CI runner / bastion / management node**
- Used for:
  - Terraform execution
  - kubectl & helm operations
  - Cluster administration
- Demonstrates **real enterprise infra patterns**

### Key Terraform Concepts Used:
- Declarative infrastructure
- State management
- Variable-driven configuration
- Idempotent provisioning

---

## ☸️ Kubernetes

### Core Capabilities:
- Deployment objects for application lifecycle
- Service for internal/external access
- Resource requests & limits
- Liveness & readiness probes

**Why Kubernetes:**
- High availability
- Self-healing
- Horizontal scaling

---

## 📦 Helm – Application Packaging

### Why Helm:
- Avoids YAML duplication
- Environment-specific configuration using `values.yaml`
- Versioned releases with rollback support

Helm charts are structured to support:
- dev / staging / prod environments
- GitOps-driven deployments

---

## 🔄 GitOps – Continuous Delivery

**Tool:** Argo CD  

### GitOps Principles Applied:
- Git as the single source of truth
- Declarative deployment state
- Automatic sync & self-healing
- Rollback via Git revert

**Why GitOps:**
- Safer deployments
- Full audit trail
- Reduced human error

---

## 🔐 Security Practices

Security is integrated at **multiple layers**:

### CI Security
- Container image scanning (shift-left)

### Kubernetes Security
- Secrets stored securely (no plaintext in Git)
- RBAC with least-privilege access
- Network Policies to restrict traffic
- Immutable image tags (no `latest` in prod)

---

## 📊 Monitoring & Observability

**Tools:**
- Prometheus – metrics collection
- Grafana – visualization & dashboards

### Monitored Metrics:
- CPU & memory usage
- Pod restarts
- Application health
- Cluster performance

**Why Monitoring Matters:**
- Proactive issue detection
- Faster incident response
- Production reliability

---

## 🧠 Real-World Scenarios Covered

- CI pipeline failures and recovery
- Git merge conflicts and resolution
- Kubernetes deployment rollbacks
- Resource misconfiguration troubleshooting
- Secure secret handling
- Infrastructure reproducibility using Terraform

---

## 🎤 Interview-Ready Summary

> “I designed and implemented an enterprise-grade DevOps platform using Azure DevOps for CI, Terraform for Azure infrastructure provisioning, Docker and Kubernetes for container orchestration, Helm for application packaging, Argo CD for GitOps-based delivery, and Prometheus–Grafana for monitoring, with security controls applied across CI and runtime layers.”

---

## 📌 Author
**Ashish Mondal**  
DevOps | Cloud | Kubernetes | GitOps

---

## 🚀 Status
🔧 Actively evolving  
✅ Production-style architecture  
📦 Real-world DevOps practices
