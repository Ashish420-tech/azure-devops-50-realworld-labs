app/node_modules/.bin/jest: not found


### Root Cause
- `node:alpine` image caused binary resolution issues
- Jest binary was present but not executable correctly in Alpine
- CI environment differed from local execution

### Fix
- Switched base image to `node:18-slim`
- Ensured devDependencies are installed during CI
- Executed tests inside the container during image build

### Final Fix (Dockerfile)
```dockerfile
FROM node:18-slim
WORKDIR /app
COPY 01-foundation/lab-04-nodejs-ci/package*.json ./
ENV NODE_ENV=development
RUN npm ci
COPY 01-foundation/lab-04-nodejs-ci/ ./
RUN npm test

Issue 2: Docker build failing in monorepo structure
Problem

Docker build could not find package.json.

Root Cause

Monorepo structure

Incorrect Docker build context

Relative paths not handled correctly

Fix

Explicitly referenced application path inside Dockerfile

Used repository root as Docker build context

Issue 3: CI pipeline inconsistent results
Problem

Tests passed locally but failed in CI.

Root Cause

Environment mismatch between local and CI

Node and npm versions differed

Fix

Standardized Node version using Docker image

Ensured tests always run inside container

Final Result

Docker image builds successfully

Unit tests run inside container

Azure DevOps pipeline is stable and green

CI is reproducible and deterministic

✅ Lab-05 CI stabilized successfully


---


