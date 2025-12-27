# Lab-07: Docker Image Build & Push (Azure DevOps)

## Objective
Build and push a production-ready Docker image using Azure DevOps CI/CD.

## Tools
- Docker
- Azure DevOps Pipelines
- Docker Hub
- Node.js

## Pipeline Flow
1. Checkout source code
2. Build Docker image
3. Tag image with build ID and latest
4. Push image to Docker Hub

## Learning Outcome
Understood the difference between CI validation images and CD deployment images.
🚀 Lab-07: Docker Image Build & Push using Azure DevOps
🎯 Objective

Build a Docker image for a Node.js application and push it to Docker Hub using an Azure DevOps YAML pipeline running on a self-hosted agent.

🛠 Tech Stack

Node.js

Docker

Azure DevOps Pipelines (YAML)

Docker Hub

Self-hosted Windows Agent

📂 Project Structure
04-docker/lab-07-docker-push/
├── Dockerfile
├── azure-pipelines.yml
├── app.js
├── package.json
├── package-lock.json
├── test/
├── issues.md
├── fixes.md
└── README.md

🔄 Pipeline Workflow

Code is pushed to the repository

Azure DevOps pipeline is triggered

Docker image is built using Dockerfile

Image is tagged with:

Build ID

latest

Image is pushed to Docker Hub

🧩 Final Pipeline YAML
trigger:
  paths:
    include:
      - 04-docker/lab-07-docker-push/*

pr: none

pool:
  name: Default

variables:
  dockerRegistryServiceConnection: dockerhub-service-connection
  imageRepository: ashishmondal420/nodejs-lab07
  dockerfilePath: 04-docker/lab-07-docker-push/Dockerfile
  buildContext: 04-docker/lab-07-docker-push
  tag: $(Build.BuildId)

steps:
- checkout: self

- task: Docker@2
  displayName: Build and Push Docker Image
  inputs:
    command: buildAndPush
    containerRegistry: $(dockerRegistryServiceConnection)
    repository: $(imageRepository)
    dockerfile: $(dockerfilePath)
    buildContext: $(buildContext)
    tags: |
      $(tag)
      latest

🐳 Docker Image

Docker Hub Repository:

https://hub.docker.com/r/ashishmondal420/nodejs-lab07

🧠 Key Learnings

Docker build context handling

npm ci vs install

Docker Hub authentication using access tokens

Azure DevOps service connections

CI/CD troubleshooting and RCA

✅ Lab Status

COMPLETED SUCCESSFULLY ✔
