# ---- build stage ----
FROM node:18-alpine AS build
WORKDIR /app
COPY 01-foundation/lab-04-nodejs-ci/package*.json ./
RUN npm ci
COPY 01-foundation/lab-04-nodejs-ci/ ./
RUN npm test

# ---- runtime stage ----
FROM node:18-alpine
WORKDIR /app
COPY --from=build /app /app
EXPOSE 3000
CMD ["npm","start"]
