# Lab-05: Docker CI – Fixes & Stabilization

## Issue 1: Jest command not found inside Docker container

### Problem
Docker build was failing with the error:

```md
# Lab-05: Docker CI – Issues Observed

## Jest execution failure in Docker
- Error: `jest: not found`
- Occurred only in Docker CI

## Docker build context issues
- `package.json` not detected initially
- Monorepo path confusion

## CI vs local environment mismatch
- Tests passed locally
- Failed inside pipeline initially
