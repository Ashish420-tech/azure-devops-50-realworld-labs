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
