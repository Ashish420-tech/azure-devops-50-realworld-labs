FROM node:18-slim

WORKDIR /app

COPY 01-foundation/lab-04-nodejs-ci/package*.json ./
RUN npm ci --omit=dev

COPY 01-foundation/lab-04-nodejs-ci/ .

EXPOSE 3000
CMD ["node", "app.js"]
