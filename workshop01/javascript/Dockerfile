from node:17
## Build
ARG APP_DIR=/app
workdir ${APP_DIR}

#copy files from local into image
add main.js .
add package.json .
add package-lock.json .
#Add directories
add public public
add views views

#install dependencies
run npm ci

## Run
ENV APP_DIR=/app
ENV PORT=3000

EXPOSE ${PORT}
workdir ${APP_DIR}
##Run the app (Entry points are like the main function java)
## CMD can be used as configurations of the ENTRYPOINT command
ENTRYPOINT [ "node" , "main" ]
#CMD [""]