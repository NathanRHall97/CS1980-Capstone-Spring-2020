FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

COPY . /internal_microservice

WORKDIR /internal_microservice

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]

EXPOSE 8080

CMD [ "internal_microservice.py" ]
