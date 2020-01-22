FROM python:3
COPY . /microservices/ui
WORKDIR /microservices/ui
ADD . ../../api_gateway.yaml
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD python3 ui.py
