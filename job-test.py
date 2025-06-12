import json
import os
import time
import requests


print("job started")
time.sleep(5)

print("job started 2")
time.sleep(5)

print("job started 3")
time.sleep(5)

print("job started 4")
value = requests.get("https://rickandmortyapi.com/api/character/154").json()
print("job started 5")
variavel = os.getenv('SCOPE')
outra = os.getenv('REDIRECT_URI')
time.sleep(5)
print(variavel)
time.sleep(5)
print(outra)
with open(f'maisumteste.json', 'w', encoding='utf-8') as f:
    json.dump(value, f, ensure_ascii=False, indent='\t')
print("job done!!!!!!!!!!!!!!")