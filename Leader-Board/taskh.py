import json
import flask, render_templates

def write_json (data, filename='intern.json'):
     with open (filename , 'w') as f:
          json.dump(data, f, indent= 4, sort_keys= True)
with open ('intern.json') as json_file:
     data =json.load(json_file)
write_json(data)
from pprint import pprint as pp
pp(data)



