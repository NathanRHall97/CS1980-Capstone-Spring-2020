from yaml import full_load, dump

# Wrapper class that represents our API document dictionary
# Credit to Charlie Mietzner
class MasterYaml:
    
    # Constructor with a YAML file to load initial data from
    def __init__(self, yaml_file=None):
        if yaml_file:
            self.api_doc_dict = yaml_to_dict(yaml_file)
        else:
            self.api_doc_dict = dict()

    # Get value based on key
    def get(self, key):
        return self.api_doc_dict.get(key)

    # Returns shallow copy of field
    def copy(self):
        return self.api_doc_dict.copy()

    # adds additional microservice info to our master API dict 
    def append_yaml(self, file_path):
        file_data = yaml_to_dict(file_path)
        for element in file_data:
            current = file_data[element]
            if(isinstance(current, list)):
                if(self.api_doc_dict.get(element)):
                    self.api_doc_dict[element] = merge_lists_no_dups(current, self.api_doc_dict[element])
                else:
                    self.api_doc_dict[element] = current
            elif(isinstance(current, dict)):
                self.add(element, current)


    # Adds key: value to field dict
    def add(self, key, value):
        if(self.api_doc_dict.get(key)):
            self.api_doc_dict[key] = merge_dicts(self.api_doc_dict.get(key), value)
        else:
            self.api_doc_dict[key] = value

    # Dumps self to file
    def write_me_to_file(self, file_name):
        with open(file_name, 'w') as f:
            dump(self.api_doc_dict, f)

#  Takes a file path and loads raw YAML data into dict
def yaml_to_dict(file_path):
    with open(file_path) as stream:
        yaml_dict = full_load(stream)
    return yaml_dict

#  Merges two dicts
def merge_dicts(d1, d2):
    temp1 = d1
    temp2 = d2
    return({**temp1 , **temp2})

# Merges two lists, avoiding duplicates
def merge_lists_no_dups(l1, l2):
    temp_list = l2.copy()
    for entry in l1:
        if not(entry in l2):
            temp_list.append(entry)
    return temp_list
