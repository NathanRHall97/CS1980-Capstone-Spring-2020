# Databases with Microservices

<h3>Implementation</h3>

When looking at how to add databases into a microservice architecture there are typically 2 routes that one can take. 

-  Shared Database Pattern
-  Database per Microservice Pattern

For this project, we thought that it would be best to go with the [Database per Microservice Pattern](https://microservices.io/patterns/data/database-per-service.html). This pattern allows for our team (and teams in the future) to maintain loosely coupled services and low overhead. 

<h3>Overall Design</h3>
- 
With the overall design of this pattern, 3 main things must occur. 

1.  Ensure that Database initialization is easy and correct.
2.  Confirm that the PostgreSQL server runs correctly with all containers utilizing it.
3.  Leave good documentation on how to expand the database infrastructure for new services that may come in the future.

<h4>Database Initialization</h4>
- 
This process is made to be simple for any new developer who should pick up this project. We will achieve this simplicity through the use of Python and Bash scripts initializing and installing everything that the project will need. SQL Files will be bundled in with the project that the python script will execute and set up for testing the project with values.

<h4>PostgreSQL Server</h4>
- 
To make sure that the PostgreSQL server runs correctly we will pull the PostgreSQL docker image and run in it a container of our own. Since PostgreSQL has functionality with docker we can simply write in a db_server service in our docker-compose.YAML file to have it spin up with all the other containers. To ensure that the containers can work with the server we must bridge the networks between the two.

<h4>Future Development</h4>
- 
Development in the future is key to this architecture. We want to implement it so that it is scalable, simple, and easy for other developers to pick up. 

This project will come with a Python script and SQL file contained with a schema for each service. The script can execute the SQL file and make calls to the database that is spun up with the docker PostgreSQL server. For any future developer who wishes to implement further services, they can simply use those 2 files as a guide. 
There will also be a fleshed-out Readme.md with instructions on how to implement more databases per service.