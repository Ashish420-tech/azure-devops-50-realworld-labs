FROM node:18-slim

WORKDIR /app

COPY 01-foundation/lab-04-nodejs-ci/package*.json ./

RUN npm ci --omit=optional

COPY 01-foundation/lab-04-nodejs-ci/ .

CMD ["node", "app.js"]
