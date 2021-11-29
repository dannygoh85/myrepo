FROM python:3.9.9
## Build
ARG APP_DIR=/app
WORKDIR ${APP_DIR}

#copy files from local into image
ADD runscript.py .
ADD requirements.txt .
ADD run.sh .
#ADD directories
ADD static static
ADD templates templates

#install dependencies
RUN pip install -r requirements.txt
## Run
ENV APP_DIR=/app
ENV PORT=3000

EXPOSE ${PORT}
WORKDIR ${APP_DIR}
##Run the app (Entry points are like the main function java)
## CMD can be used as configurations of the ENTRYPOINT command
ENTRYPOINT [ "sh" , "run.sh"]
#CMD [""]