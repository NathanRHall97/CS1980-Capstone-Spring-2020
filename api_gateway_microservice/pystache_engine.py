import pystache
from prance import ResolvingParser

# Class for constructing code based on pystache templates
class PystacheEngine:
    def __init__(self):
        self.code = dict()
        self.template = str

    # Takes the path of input files and a microservice: IP address dict and generates a dict with all info
    def convert_yamls_pystache(self, inputs, ip_dict, dict_variables=None):
        for micro_dir, yaml in inputs.items():
            *x, name = micro_dir.split('/')
            if(ip_dict.get(name)):
                if(len(self.code) >= 1):
                    temp = self.get_swagger_info(self.get_spec(yaml), ip_dict.get(name), dict_variables)
                    for operation in temp['operations']:
                        self.code['operations'].append(operation)
                else:
                    self.code = self.get_swagger_info(self.get_spec(yaml), ip_dict.get(name), dict_variables)
        return self.code

    # Takes a template input file and an output file path and renders the pystache template and writes it
    def render_write(self, infile, outfile):
        with open(infile, "r") as file:
            self.template = file.read()

        output = pystache.render(self.template, self.code)

        with open(outfile, 'w') as file:
            file.write(output)

    # Returns a dict of file specs using a parser
    def get_spec(self, filename):
        parser = ResolvingParser(filename)
        return parser.specification

    # Using a dict of inputted file specs and a dict of microservice: IPs, generates a new dict with both data in form needed for pystache
    def get_swagger_info(self, spec, ip, dict_variables=None):
        variables = {}
        operations = []
        for path_key, path_val in spec['paths'].items():
            for method_key, method_val in path_val.items():
                parameters = []
                if 'parameters' in method_val:
                    for parameter_info in method_val['parameters']:
                        parameters.append({'param_name': parameter_info['name'], 'required': parameter_info['required'],})
                # This WITH the basePath prepended
                # operation = {'name': method_val['operationId'], 'ip': ip, 'request_method': method_key, 'path': spec['basePath'] + path_key, 'parameters': parameters,}
                # This is WITHOUT the basePath prepended
                operation = {'name': method_val['operationId'], 'ip': ip, 'request_method': method_key, 'path': path_key, 'parameters': parameters,}
                if dict_variables:
                    for key, val in dict_variables.items():
                        operation[key] = val
                operations.append(operation)
        variables = {'operations': operations}
        return variables    