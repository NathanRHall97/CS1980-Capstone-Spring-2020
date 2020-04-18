# Database Configuration

- In order to keep the database consistent we set it up so that the ip address is always allocated to be the highest ip address in build.py. 
- Anytime a microservice is added it will cause the database ip to be wrong in the files that make calls to it. So if you add a microservice just go to these files and increment the db ip by 1. 
Files: 
1. microservices/pet/pet.py
2. microservices/user/user.py
