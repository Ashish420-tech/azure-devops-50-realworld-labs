FROM node:18-slim

# 1. Set working directory
WORKDIR /app

# 2. Copy package files first (for layer caching)
COPY 01-foundation/lab-04-nodejs-ci/package*.json ./

# 3. Install dependencies (including devDependencies)
ENV NODE_ENV=development
RUN npm ci

# 4. Copy application source code
COPY 01-foundation/lab-04-nodejs-ci/ ./

# 5. Run tests (robust way for CI)
RUN npx jest --runInBand
