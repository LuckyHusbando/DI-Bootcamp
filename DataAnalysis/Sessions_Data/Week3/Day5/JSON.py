#JSON - JavaScript Object Notation - Can be read by any computer, any program. It makes it easy to exchange data across platforms.

import json
import os

#Convert a dictionary to Json

dir_path = os.path.dirname(os.path.realpath(__file__)) 

my_family = {
    'parents':['Beth', 'Jerry'],
    'children':['Summer', 'Morty']
}

#Convert a dict to a JSON file
with open(f'{dir_path}/family.json', 'w') as f:
    json.dump(my_family,f)

#Convert a dict to a JSON string
json_my_family_string = json.dumps(my_family)
print(type(json_my_family_string))

#Convert from a Json file to a dictionary
with open(f'{dir_path}/family.json', 'r') as f:
    my_family2 = json.load(f)

print(type(my_family2))

#Convert from a Json string to a dictionary
parsed_family = json.loads(json_my_family_string)
print(type(parsed_family))