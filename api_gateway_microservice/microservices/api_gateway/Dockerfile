FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

COPY . /microservices/api_gateway

WORKDIR /microservices/api_gateway

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

# This container port will be used by our api_gateway.py webservice.
# The host port should be mapped to the ephemeral port (i.e. fake container port) 8080
EXPOSE 8080

ENTRYPOINT [ "python3" ]

CMD [ "api_gateway.py" ]
