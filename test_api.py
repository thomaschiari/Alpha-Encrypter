import requests
import json
import numpy as np


url_enigma = 'http://localhost:5000/api/enigma'
url_de_enigma = 'http://localhost:5000/api/de_enigma'

msg = "hello world"

response_enigma = requests.post(url_enigma, json={'msg': msg})
msg_cifrada = json.loads(response_enigma.text)['msg_cifrada']
P = np.array(json.loads(response_enigma.text)['P'])
E = np.array(json.loads(response_enigma.text)['E'])

print(msg_cifrada)
print(P)
print(E)

response_de_enigma = requests.post(url_de_enigma, json={'msg_cifrada': msg_cifrada, 'P': P.tolist(), 'E': E.tolist()})
msg_original = json.loads(response_de_enigma.text)['msg_original']

print(msg_original)
