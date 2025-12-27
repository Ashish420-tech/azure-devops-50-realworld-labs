# ---- build stage ----
FROM node:18-alpine AS build
WORKDIR /app

# copy dependency files
COPY 01-foundation/lab-04-nodejs-ci/package*.json ./
RUN npm ci

# copy application source
COPY 01-foundation/lab-04-nodejs-ci/ ./

# run tests
RUN npm test

# ---- runtime stage ----
FROM node:18-alpine
WORKDIR /app
COPY --from=build /app /app

EXPOSE 3000
CMD ["npm","start"]
