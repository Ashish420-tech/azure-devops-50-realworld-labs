# Lab-22: Jenkins CI with Node.js Application

## Objective
Configure Jenkins to perform CI for a Node.js application using npm.

## Problem Faced
Jenkins initially validated the environment but failed to build the Node.js app.

## Error / Symptom
Build failed due to incorrect directory navigation inside Jenkins workspace.

## Root Cause
Incorrect relative path was used while navigating to the Node.js application directory.

## Fix / Learning
Verified Jenkins workspace using `pwd` and `ls`, corrected directory path,
and successfully executed `npm install` inside the application folder.

## Tools Used
- Jenkins
- Node.js
- npm
- GitHub

## Interview Talking Points
- Jenkins workspace structure
- Running Node.js builds in CI
- Debugging path issues in Jenkins
- Difference between local and CI builds

