FROM node:lts-alpine as build-stage

MAINTAINER Qi Zhao <zhaoqi99@outlook.com>

WORKDIR /app
COPY package*.json ./
RUN npm install -g cnpm --registry=https://registry.npm.taobao.org
RUN cnpm install
COPY . .
RUN cnpm run build

FROM nginx:stable-alpine as production-stage

MAINTAINER Qi Zhao <zhaoqi99@outlook.com>

RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]