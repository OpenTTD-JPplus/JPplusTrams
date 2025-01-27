
import json

def LoadJSON(target_file):
    with open(target_file, 'r') as file:
        data = json.load(file)
    return data

trams = LoadJSON('lib/jpplustrams.json')
schema = LoadJSON('lib/stats_schema.json')


#print((schema['Speed']['ignore_string']))
#print((schema['Intro_Date']['ignore_string']))

#print(list(schema.keys()))

stats = list(schema.keys())
for s in stats:
    content = list(schema[s].keys())
    if 'ignore_string' in content:
        print(s + " has ignore")
    else:
        print(s + " does not have ignore")