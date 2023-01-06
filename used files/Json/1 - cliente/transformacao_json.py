import json

lista = ['Emilio Santiago','32564197849','1946-12-06','santiagoemilio@gmail.com','41985475362','41966325487','ave','Cândido de Abreu','300','Centro Civico','Apto 403','Curitiba ','PR','81830325']

with open('json_emilio_santiago.json', 'w') as f:
    json.dump(lista, f)