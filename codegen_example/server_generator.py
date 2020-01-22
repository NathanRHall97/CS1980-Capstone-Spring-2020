#!/usr/bin/env python
import pystache
from prance import ResolvingParser
import pprint

def madlib(mustache_template, variables):
    output = pystache.render(mustache_template, variables)
    return output

def get_swagger_info(spec):
    variables = {}
    operations = []
    for path_key, path_val in spec['paths'].items():
        for method_key, method_val in path_val.items():
            parameters = []
            if 'parameters' in method_val:
                for parameter_info in method_val['parameters']:
                    parameters.append(
                        {
                            'param_name': parameter_info['name'],
                            'required': parameter_info['required'],
                        }
                    )
            operation = {
                'name': method_val['operationId'],
                'request_method': method_key,
                'path': spec['basePath'] + path_key,
                'parameters': parameters,
            }
            operations.append(operation)
    variables = {'operations': operations}
    return variables

def get_spec(filename):
    parser = ResolvingParser(filename)
    return parser.specification

def main():
    print("Reading in server mustache template...")
    with open("templates/server.mustache", "r") as file:
        server_template = file.read()

    print("Reading in API documentation...")
    spec = get_spec('mogwai.yaml')

    print("Parsing API operations...")
    variables = get_swagger_info(spec)

    print("Generating server code...")
    output = madlib(server_template, variables)

    print("Writing server code to file...")
    with open('generated_server.py', 'w') as output_file:
        output_file.write(output)

    print("All done!")

if __name__ == '__main__':
    main()
