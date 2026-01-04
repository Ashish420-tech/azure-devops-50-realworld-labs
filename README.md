# 🚀 Azure DevOps – 50 Real-World CI/CD Labs

> Maintained and implemented by **Ashish Mondal**, focusing on real-world Azure DevOps
> troubleshooting, CI/CD failures, and production-grade deployment strategies.


This repository contains **50 real-world, hands-on Azure DevOps labs** focused on
**CI/CD pipelines, Docker, Kubernetes, Terraform, and Azure**.

Unlike tutorial-based projects, these labs are built with a **production mindset**:
❌ failures  
✅ troubleshooting  
🧠 root-cause analysis  
🔁 fixes and improvements  

This repo reflects **practical DevOps experience**, not just theory.

---

## 🧑‍💻 Who This Repo Is For
- DevOps Engineers (3–8 years)
- Azure DevOps / CI-CD roles
- Kubernetes & Cloud Engineers
- Candidates preparing for **real interviews**, not exams

---

## 🛠 Tools & Technologies Used
- Azure DevOps (Pipelines, Repos, Agents)
- Docker & Docker Hub
- Kubernetes (Minikube / AKS-compatible)
- Terraform (Azure IaC)
- Azure (VMs, Networking, Storage)
- Git & GitHub
- Linux & Shell Scripting
- Node.js sample applications

---

## 🧪 Lab Index (Complete Overview)

### 🔹 Foundation & CI
| Lab | Topic |
|----|------|
| Lab-01 | Azure DevOps Repo & Pipeline Basics |
| Lab-02 | YAML Pipeline Fundamentals |
| Lab-03 | Node.js CI Pipeline |
| Lab-04 | Handling Build Errors in Pipelines |
| Lab-05 | Agent & Workspace Debugging |

---

### 🔹 Docker & Containerization
| Lab | Topic |
|----|------|
| Lab-06 | Dockerfile Basics |
| Lab-07 | CI Pipeline with Docker Build |
| Lab-08 | Docker Push to Docker Hub |
| Lab-09 | Docker Build Context Issues |
| Lab-10 | Image Tagging & Versioning |

---

### 🔹 Kubernetes (Local → Production Style)
| Lab | Topic |
|----|------|
| Lab-11 | Kubernetes Deployment Basics |
| Lab-12 | Services & Pod Networking |
| Lab-13 | Resource Requests & Limits |
| Lab-14 | Helm Chart Deployment |
| Lab-15 | Helm Upgrade & Rollback |
| Lab-16 | ImagePullBackOff Troubleshooting |

---

### 🔹 Azure DevOps + Kubernetes CI/CD
| Lab | Topic |
|----|------|
| Lab-17 | Azure DevOps → Kubernetes CI/CD |
| Lab-18 | Rolling Update Strategy |
| Lab-19 | Blue-Green Deployment |
| Lab-20 | Zero-Downtime Deployment Patterns |

---

### 🔹 Terraform & Infrastructure as Code
| Lab | Topic |
|----|------|
| Lab-21 | Terraform Basics |
| Lab-22 | Azure VM Provisioning |
| Lab-23 | Terraform State & Backend |
| Lab-24 | IaC + Azure DevOps Pipeline |
| Lab-25 | Destroy & Cost Optimization |

---

### 🔹 Advanced DevOps (Planned / Ongoing)
| Lab | Topic |
|----|------|
| Lab-26+ | AKS Architecture (Cost-Optimized) |
| Lab-30+ | Monitoring & Logging |
| Lab-40+ | Security & Secrets |
| Lab-50 | End-to-End Production CI/CD |

> ⚠️ Some labs intentionally use **Minikube instead of AKS**  
> to demonstrate **cost-optimized non-production design**, while remaining AKS-compatible.

---

## 🔥 Key Real-World Problems Solved
- Git push & branch misconfiguration
- Azure DevOps agent issues
- Docker authentication failures
- ImagePullBackOff errors
- YAML syntax & indentation bugs
- Kubernetes rollout failures
- Resource starvation & limits
- Zero-downtime deployment challenges

---

## 🎯 What Interviewers Can Ask From This Repo
- “Explain a CI/CD failure you debugged”
- “How do you handle zero downtime?”
- “Why use resource limits?”
- “Minikube vs AKS?”
- “How do you reduce cloud cost?”
- “What breaks first in pipelines?”

👉 Every answer exists **inside these labs**.

---

## 📌 Why This Repository Matters
✔️ Real failures, not happy paths  
✔️ Production-style CI/CD  
✔️ Cost-aware cloud usage  
✔️ Interview-ready DevOps experience  

---
🔹 LAB 1–5 : Azure DevOps & Git (FOUNDATION)
🧪 Lab-01: Repo & Pipeline Basics

Problem Faced

Pipeline not triggering after commit

Error / Symptom

No run created in Azure DevOps

Root Cause

Wrong branch selected in pipeline trigger

Fix / Learning

Corrected trigger: branch in YAML

Learned how pipeline triggers work

🧪 Lab-02: YAML Pipeline Basics

Problem Faced

YAML validation failed

Error / Symptom

mapping values are not allowed here

Root Cause

Incorrect indentation in YAML

Fix / Learning

Fixed spacing

Learned YAML is indentation-sensitive

🧪 Lab-03: Node.js CI Pipeline

Problem Faced

Build failed on agent

Error / Symptom

npm: command not found

Root Cause

Node.js not installed on agent

Fix / Learning

Used Microsoft-hosted agent with Node

Verified versions using node -v

🧪 Lab-04: Build Errors Handling

Problem Faced

Pipeline failed randomly

Error / Symptom

App directory not found

Root Cause

Wrong working directory

Fix / Learning

Used workingDirectory

Learned agent workspace structure

🧪 Lab-05: Agent Debugging

Problem Faced

Commands running but output unclear

Error / Symptom

Debugging difficult

Root Cause

No logging enabled

Fix / Learning

Added echo, ls, pwd

Learned pipeline debugging techniques

🔹 LAB 6–10 : Docker (VERY IMPORTANT)
🧪 Lab-06: Dockerfile Basics

Problem Faced

Docker image build failed

Error / Symptom

COPY failed: file not found

Root Cause

Wrong file path in Dockerfile

Fix / Learning

Corrected build context

Understood Docker build context

🧪 Lab-07: Docker Build in CI

Problem Faced

Docker build failed in pipeline

Error / Symptom

Docker daemon not available

Root Cause

Docker not installed on agent

Fix / Learning

Used Microsoft-hosted Linux agent

🧪 Lab-08: Docker Push to Docker Hub

Problem Faced

Image push failed

Error / Symptom

authentication required

Root Cause

Docker Hub credentials missing

Fix / Learning

Created service connection

Learned secure credential handling

🧪 Lab-09: Docker Build Context Issue

Problem Faced

Build succeeded locally, failed in CI

Error / Symptom

Files missing during build

Root Cause

.dockerignore excluded files

Fix / Learning

Fixed .dockerignore

Learned CI vs local differences

🧪 Lab-10: Image Tagging

Problem Faced

Old image deployed again

Error / Symptom

Changes not reflected

Root Cause

Used latest tag

Fix / Learning

Implemented versioned tags

Learned why latest is dangerous

🔹 LAB 11–16 : Kubernetes (CRITICAL)
🧪 Lab-11: Kubernetes Deployment

Problem Faced

Pod not starting

Error / Symptom

CrashLoopBackOff

Root Cause

Wrong container port

Fix / Learning

Fixed container spec

Learned pod debugging

🧪 Lab-12: Kubernetes Service

Problem Faced

App not accessible

Error / Symptom

Service reachable, app not

Root Cause

Selector mismatch

Fix / Learning

Corrected labels

Learned Service → Pod mapping

🧪 Lab-13: Resource Limits

Problem Faced

Pod restarted automatically

Error / Symptom

OOMKilled

Root Cause

Memory limit too low

Fix / Learning

Adjusted limits

Learned resource planning

🧪 Lab-14: Helm Deployment

Problem Faced

Helm install failed

Error / Symptom

Template rendering error

Root Cause

Incorrect values.yaml

Fix / Learning

Fixed values

Learned Helm templating

🧪 Lab-15: Helm Upgrade

Problem Faced

New version failed

Error / Symptom

App broken after upgrade

Root Cause

Bad image version

Fix / Learning

Used helm rollback

Learned safe rollback strategy

🧪 Lab-16: ImagePullBackOff

Problem Faced

Pod stuck in ImagePullBackOff

Error / Symptom

Image not pulled

Root Cause

Wrong image name / auth issue

Fix / Learning

Fixed image reference

Learned image pull troubleshooting

🔹 LAB 17–19 : CI/CD + K8s (FLAGSHIP)
🧪 Lab-17: Azure DevOps → Kubernetes

Problem Faced

Pipeline deployed but app not updated

Error / Symptom

Old version still running

Root Cause

Kubernetes context mismatch

Fix / Learning

Fixed kubeconfig

Learned pipeline → cluster flow

🧪 Lab-18: Rolling Update

Problem Faced

Pods restarted simultaneously

Error / Symptom

Temporary downtime

Root Cause

Default rolling strategy

Fix / Learning

Configured maxUnavailable

Learned zero-downtime rollout

🧪 Lab-19: Blue-Green Deployment

Problem Faced

Traffic not switching

Error / Symptom

Old pods still serving traffic

Root Cause

Service selector mismatch

Fix / Learning

Corrected labels

Learned safe production deployment
---

## 👤 Author & Maintainer

**:contentReference[oaicite:0]{index=0}**  
Senior DevOps Engineer | Azure DevOps | CI/CD | Docker | Kubernetes | Terraform  

🔹 This repository represents my **hands-on DevOps journey**, where I built and troubleshot
real-world CI/CD pipelines, containerized applications, and Kubernetes deployments.

🔹 Every lab is based on **actual problems I faced**, including pipeline failures,
Docker build issues, Kubernetes deployment errors, and production-style rollout strategies
(Rolling, Blue-Green).

🔹 The focus of this repository is **practical DevOps experience**, not theoretical demos.

📌 **Key strengths demonstrated in this repo:**
- CI/CD pipeline design and debugging
- Docker build & push automation
- Kubernetes deployment & troubleshooting
- Zero-downtime deployment strategies
- Cost-aware cloud and AKS-compatible architecture

🔗 GitHub: https://github.com/Ashish420-tech  
🔗 LinkedIn: https://www.linkedin.com/in/ashish-mondal-a4190638a/

## 📬 Author
**Ashish Mondal**  
DevOps Engineer | Azure | CI/CD | Kubernetes | Terraform  


