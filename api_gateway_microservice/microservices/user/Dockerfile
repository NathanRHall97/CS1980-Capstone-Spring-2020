FROM python:3
COPY . /microservices/user
WORKDIR /microservices/user
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD python3 user.py
