FROM node:18-slim

WORKDIR /app

COPY 01-foundation/lab-04-nodejs-ci/package*.json ./

ENV NODE_ENV=development
RUN npm ci

COPY 01-foundation/lab-04-nodejs-ci/ ./

RUN npx jest --runInBand
