FROM python:3
COPY . /microservices/pet
WORKDIR /microservices/pet
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD python3 pet.py
