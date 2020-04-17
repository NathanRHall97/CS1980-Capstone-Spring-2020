# Requirements for extending a microservice:
  1. New microservice directory must be placed as a sub-directory within `microservices/` directory.
  2. New microservice should be locally running at `0.0.0.0`.
  3. New microservice's OpenAPI file must be named `api_doc.yaml` or `api_doc.yml`.
  4. If you create test files for a microservice, create a test directory and put the test file in that.

## How to run:
1. Install requirements from root folder Documentation `pip install -r requirements.txt`
2. Run `docker pull postgres` to get the postgres image for the database
2. From `api_gateway_microservice` directory, run `python build.py` to build requisite YAMLs and database files
3. From `api_gateway_microservice` directory, run `docker-compose build` to build all microservices
4. From `api_gateway_microservice` directory, run `bash dbsetup` to initialize the database (Linux/Mac Bash)
3. From `api_gateway_microservice` directory, run `docker-compose up` to spin up microservices

## Notes:
1. Default configuration information is in `config/` directory.
2. Database documentation is in `database/Documentation` directory.
