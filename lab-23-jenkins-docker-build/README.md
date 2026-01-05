# Lab-23: Jenkins CI – Docker Image Build

## Objective
Build a Docker image using Jenkins from application source code.

## Problem Faced
Application container image was not being built automatically in CI.

## Error / Symptom
Docker image build was missing from Jenkins workflow.

## Root Cause
Jenkins job did not include Docker build stage.

## Fix / Learning
Validated Docker availability in Jenkins agent,
navigated to correct application directory,
and successfully built Docker image using Dockerfile.

## Tools Used
- Jenkins
- Docker
- Node.js
- GitHub

## Interview Talking Points
- Jenkins + Docker integration
- Docker build in CI
- Jenkins permissions for Docker
- Dockerfile usage in pipelines
# Lab 23 – Jenkins Full CI/CD Pipeline with Docker Deployment

## 📌 Overview
This lab demonstrates a **complete end-to-end CI/CD pipeline using Jenkins**, where code is automatically:
- Checked out from GitHub
- Built into a Docker image
- Pushed securely to Docker Hub
- Deployed automatically as a running container
- Verified via health check

This lab goes beyond basic CI and implements **true Continuous Deployment (CD)**.

---

## 🧰 Tools & Technologies Used
- Jenkins (Pipeline as Code)
- Git & GitHub
- Docker & Docker Hub
- Node.js (sample application)
- Linux (Jenkins server)

---

## 🏗️ Architecture Flow

Git Push  
⬇  
Jenkins Pipeline (Jenkinsfile)  
⬇  
Docker Build  
⬇  
Docker Push (Docker Hub)  
⬇  
Deploy Container  
⬇  
Application Verification  

---

## 📁 Project Structure

lab-23-jenkins-docker-build/
├── app/
│ └── index.js
├── Dockerfile
├── Jenkinsfile
└── README.md


---

## ⚙️ Jenkins Pipeline Stages

1. **Checkout**
   - Pulls latest code from GitHub repository

2. **Build Docker Image**
   - Builds Docker image using a specified Dockerfile and build context  
   - Handles monorepo structure correctly

3. **Push Image**
   - Authenticates securely using Jenkins Credentials
   - Pushes image to Docker Hub

4. **Deploy (CD)**
   - Stops existing container (if any)
   - Runs new container from latest image

5. **Verify**
   - Performs health check using `curl` on port 3000

---

## 🔐 Security Best Practices
- Docker Hub credentials stored securely in Jenkins Credentials Manager
- No hardcoded secrets in Jenkinsfile
- Credentials injected at runtime

---

## 🧪 Verification

On Jenkins server:
```bash
docker ps
curl http://localhost:3000
Expected Output:

Lab 23 Jenkins CI/CD is LIVE 🚀
