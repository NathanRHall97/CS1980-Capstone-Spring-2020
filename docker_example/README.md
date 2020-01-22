# Instructions for use:

 1. Ensure you have docker and docker-compose installed on your host machine
 2. From the `docker-example` directory, run this command: `docker compose up --build`
 3. This command uses the docker-compose.yml file in this directory to build and run the two different containers under `api_gateway` directory and `internal_microservice` directory.
 4. The API gateway container will be listening at `127.0.0.1` on `port 8080`. You shouldn't be able to contact the `internal_microservice` container from the outside world.
 5. Once the containers are running, make the following `cURL` request against the API gateway container: `curl 127.0.0.1:8080/`
 6. You should get a message from `api_gateway` AND a message from `internal_microservice` by way of the gateway...neato
 