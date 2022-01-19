import yaml


model_dict ={
    'NY': {'model_name': 'NY-Model', 'model_id': 1234},
    'CA': {'model_name': 'CA-Model', 'model_id': 2345}}




with open('my_yaml_file.yaml', 'w') as file:
    documents = yaml.dump(model_dict, file)



# Load Yaml File
with open('my_yaml_file.yaml') as file:
    doc = yaml.load(file, Loader=yaml.FullLoader)
    print(doc)


