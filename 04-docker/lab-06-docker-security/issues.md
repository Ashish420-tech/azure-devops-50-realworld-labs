## Issue 1: Pipeline failed during Trivy scan

**Error:**
HIGH/CRITICAL vulnerabilities detected

**Root Cause:**
Base image contains outdated packages

**Fix:**
- Use slimmer base image
- Keep Node version updated
