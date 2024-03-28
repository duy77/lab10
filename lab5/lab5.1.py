
    


import json

with open('bank.json') as f:
    data = json.load(f)

for person in data['PNC bank']['customers']:
    print(person['first_name'])
    
#for person in data['PNC bank']['customers']:
#    print(person['first_name'], person['last_name'])