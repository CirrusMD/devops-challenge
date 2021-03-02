FROM python:3.8-alpine

RUN mkdir -p /opt/server
COPY . /opt/server/
WORKDIR /opt/server
RUN pip install -r requirements.txt 
EXPOSE 8080
ENTRYPOINT python server.py 
