FROM node:20-alpine AS build
WORKDIR /app
COPY Excalidraw/excalidraw ./
#WORKDIR excalidraw/packages/excalidraw
RUN ls -la
RUN cd /app/packages/excalidraw && yarn && cd /app/excalidraw-app && yarn build:app:docker
#WORKDIR /app/excalidraw/excalidraw-app
#RUN yarn build:app:docker

FROM nginx AS web
COPY default.conf /etc/nginx/conf.d
COPY --from=build /app/excalidraw-app/build /usr/share/nginx/html/
