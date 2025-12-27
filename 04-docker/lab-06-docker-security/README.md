# Lab-06: Docker Image Security Scan (DevSecOps)

This lab demonstrates adding security scanning into a Docker CI pipeline.

## Tools Used
- Azure DevOps
- Docker
- Trivy
- Node.js

## Key Learning
- Shift-left security
- Docker image vulnerability scanning
- CI pipeline failure on security risks
## 📌 Key Learning

This lab helped me clearly understand the difference between **CI validation images** and **deployment images**.

In CI pipelines, Docker images can be built ephemerally for testing and security scanning and discarded afterward if they are not pushed to a registry. This prevents insecure or unverified images from being reused in later stages.
