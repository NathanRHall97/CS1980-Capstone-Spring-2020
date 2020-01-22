# Requirements for extending a microservice:
  1. New microservice directory must be placed as a sub-directory within `microservices/` directory.
  2. New microservice should be locally running at `0.0.0.0`.
  3. New microservice's OpenAPI file must be named `api_doc.yaml` or `api_doc.yml`.

## How to run:
1. Install pystache module to read/write from mustache templates `pip install pystache`
2. From `api_gateway_microservice` directory, run `python build.py` to build requisite YAMLs
3. Run newly generated API gateway server with `python api_gateway.py`
4. From `api_gateway_microservice` directory, run `docker-compose up` to spin up microservices

## Notes:
1. Default configuration information is in `config/` directory.
