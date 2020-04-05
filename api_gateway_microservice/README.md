# Requirements for extending a microservice:
  1. New microservice directory must be placed as a sub-directory within `microservices/` directory.
  2. New microservice should be locally running at `0.0.0.0`.
  3. New microservice's OpenAPI file must be named `api_doc.yaml` or `api_doc.yml`.
  4. If you create test files for a microservice, create a test directory and put the test file in that.

## How to run:
1. Install pystache module to read/write from mustache templates `pip install pystache`
2. Run `docker pull postgres` to get the postgres image for the database
2. From `api_gateway_microservice` directory, run `python build.py` to build requisite YAMLs and database files
3. From `api_gateway_microservice` directory, run `docker-compose up` to spin up microservices
4. Open a new terminal and run `bash database/Scripts/dbsetup` to initialize database

## Notes:
1. Default configuration information is in `config/` directory.
2. Database documentation is in `database/Documentation` directory.