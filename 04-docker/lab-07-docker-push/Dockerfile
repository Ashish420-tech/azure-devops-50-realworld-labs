FROM node:18-slim

WORKDIR /app

# Copy package files first (layer caching)
COPY 01-foundation/lab-04-nodejs-ci/package*.json ./

# Install only production dependencies
RUN npm ci --omit=dev

# Copy application source
COPY 01-foundation/lab-04-nodejs-ci/ .

EXPOSE 3000

CMD ["node", "app.js"]
