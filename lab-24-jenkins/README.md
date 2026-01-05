# Lab 24 – Jenkins CI/CD Automation using GitHub Webhooks

## 📌 Overview
This lab extends the Jenkins CI/CD pipeline by introducing **GitHub Webhooks** to enable
**fully automated, event-driven CI/CD**.

With this setup, every `git push` automatically triggers Jenkins without any manual intervention.

---

## 🎯 Objective
- Eliminate manual “Build Now” in Jenkins
- Automatically trigger CI/CD on GitHub push events
- Implement industry-standard event-driven automation

---

## 🧰 Tools & Technologies
- Jenkins (Pipeline as Code)
- GitHub Webhooks
- Docker & Docker Hub
- ngrok (for exposing local Jenkins)
- Node.js application
- Linux (Jenkins server)

---

## 🏗️ CI/CD Flow Architecture

Git Push  
⬇  
GitHub Webhook  
⬇  
Jenkins Pipeline  
⬇  
Docker Build  
⬇  
Docker Push  
⬇  
Deploy Container  
⬇  
Application Verification  

---

## 🌐 Webhook Configuration

### Jenkins Side
- Build Trigger enabled:
