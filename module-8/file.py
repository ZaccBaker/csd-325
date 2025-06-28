import json

#Read json file, set as data
def read_file(fileName):
    with open(fileName, 'r') as file:
        
        data = json.load(file)
        
        return data

#Updates json file with my data
def update_file(fileName, dataUpdated):
    with open(fileName, 'w') as file:
        json.dump(dataUpdated, file, indent = 2)
