🚀 Azure DevOps – 50 Real-World CI/CD & Cloud DevOps Labs

This repository showcases hands-on, real-world DevOps scenarios implemented as part of my DevOps and Cloud engineering journey.
It focuses on practical CI/CD pipelines, containerization, Kubernetes deployments, Infrastructure as Code, and troubleshooting patterns commonly faced in production environments.

The labs are designed around real DevOps problems, not just tutorials, covering build failures, deployment strategies, infrastructure automation, and monitoring concepts.

🎯 Skills & Technologies Demonstrated

CI/CD Pipelines

Azure DevOps YAML pipelines

Jenkins pipelines

Pipeline debugging and fixes

Containerization

Docker image creation

Multi-stage Docker builds

Containerized application deployment

Kubernetes

Kubernetes deployments and services

Blue-Green and rolling deployment strategies

Minikube-based Kubernetes labs

Troubleshooting pod and service issues

Infrastructure as Code (IaC)

Terraform with Azure

Automated infrastructure provisioning

Basic state and resource management

Cloud & DevOps Practices

Azure DevOps project configuration

Environment-based deployments

CI/CD integration with containers and Kubernetes

Monitoring and operational awareness

📁 Repository Structure (High-Level)
azure-devops-50-realworld-labs/
│
├── ci-cd/                 # CI/CD pipeline labs
├── docker/                # Docker build & image labs
├── kubernetes/            # Kubernetes deployment & troubleshooting labs
├── terraform/             # Terraform & Azure IaC labs
├── scripts/               # Automation & helper scripts
├── screenshots/           # Pipeline / deployment screenshots (where applicable)
└── README.md


Each lab folder contains YAML files, scripts, and configuration files used to solve a specific DevOps scenario.

⭐ Highlighted Real-World Labs
🔹 CI/CD Pipeline Implementation & Debugging

Built CI/CD pipelines using Azure DevOps YAML

Identified and fixed pipeline build and deployment errors

Integrated source code with automated build workflows

🔹 Docker & Container Workflows

Created Dockerfiles for application builds

Automated Docker image creation through pipelines

Tested container images locally and in CI/CD flows

🔹 Kubernetes Deployments

Deployed containerized applications to Kubernetes

Implemented Blue-Green deployment strategy

Debugged pod failures, service exposure, and selector mismatches

🔹 Terraform & Cloud Infrastructure

Provisioned Azure cloud resources using Terraform

Practiced infrastructure automation and repeatable deployments

Integrated IaC workflows with CI/CD concepts

🛠 Example Lab Breakdown
🔸 Blue-Green Deployment (Kubernetes)

Problem: Deploy application updates without downtime
Approach:

Maintain two environments (Blue & Green)

Switch traffic using Kubernetes services
Tools: Kubernetes, Azure DevOps Pipelines
Learning Outcome:

Zero-downtime deployment concepts

Rollback safety and service selector management

🔸 Terraform Azure Infrastructure Lab

Problem: Manual cloud provisioning is error-prone
Approach:

Use Terraform to provision Azure resources

Apply infrastructure changes via code
Tools: Terraform, Azure
Learning Outcome:

Infrastructure as Code fundamentals

Repeatable and auditable cloud deployments

🧪 How to Use This Repository

Clone the repository:

git clone https://github.com/Ashish420-tech/azure-devops-50-realworld-labs.git


Navigate to any lab folder:

cd kubernetes/lab-19


Review:

YAML files

Dockerfiles

Terraform configs

Scripts

Follow comments inside files for execution and learning steps.

These labs are intended for learning and demonstration purposes, not as production-ready templates.

📌 Why This Repository Matters

This repository demonstrates:

Practical DevOps problem-solving

Exposure to real CI/CD failures and fixes

Hands-on work with containers, Kubernetes, and IaC

Understanding of production-style deployment patterns

It directly supports my transition into DevOps / Cloud Engineering roles by providing verifiable evidence of hands-on experience.

🔗 Links

GitHub: https://github.com/Ashish420-tech

LinkedIn: https://www.linkedin.com/in/ashish-mondal-a4190638a/

📄 License

This repository is intended for learning and portfolio demonstration purposes.
