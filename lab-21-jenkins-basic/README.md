# Lab-21: Jenkins CI – Basic Setup

## Objective
Set up a basic Jenkins freestyle job to pull source code from GitHub
and validate Jenkins CI functionality.

---

## Problem Faced
Jenkins job failed while cloning the Git repository during the first build.

---

## Error / Symptom

---

## Root Cause
Jenkins was configured to build the default `master` branch,  
but the GitHub repository uses `main` as the default branch.

Jenkins does **not auto-detect** branch names.

---

## Fix / Learning
- Updated Jenkins job branch configuration from `master` to `main`
- Rebuilt the job successfully
- Learned that branch mismatch is a common Jenkins CI failure

---

## Tools Used
- Jenkins
- GitHub
- Linux

---

## Interview Talking Points
- Jenkins branch configuration
- Common Git clone failures in Jenkins
- Difference between `master` and `main`
- How Jenkins checks out source code
