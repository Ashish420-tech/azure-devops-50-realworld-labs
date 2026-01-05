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
GitHub hook trigger for GITScm polling

- Jenkins webhook endpoint:


/github-webhook/


### GitHub Side
- Webhook added under:


Repository → Settings → Webhooks

- Payload URL (via ngrok):


https://<ngrok-id>.ngrok-free.dev/github-webhook/

- Event type:
- Push events
- Content type:
- application/json

---

## 🔐 Why ngrok?
Jenkins was running on a private/local network.
ngrok was used to securely expose Jenkins to the internet so GitHub could reach it.

---

## ✅ Verification Steps

1. **Webhook Ping Event**
 - GitHub sends a `ping`
 - Jenkins responds with `200 OK`

2. **Push Event Verification**
 ```bash
 git commit --allow-empty -m "Webhook test"
 git push origin main


Jenkins Auto Trigger

Jenkins build starts automatically

Build reason shows:

Started by GitHub push


Deployment Verification

curl http://localhost:3000


Expected Output:

Webhook PUSH event verified 🚀

🧠 Key Learnings

Difference between manual CI and automated CI/CD

GitHub Webhooks vs polling

Exposing private Jenkins securely

End-to-end automation without human intervention

✅ Lab Status

✔ Jenkins CI
✔ Jenkins CD
✔ GitHub Webhook Automation
✔ Event-driven CI/CD
