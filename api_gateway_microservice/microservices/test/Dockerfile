FROM python:3
COPY . /microservices/test
WORKDIR /microservices/test
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD pytest -s test.py