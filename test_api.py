import requests
import json
import numpy as np


url_enigma = 'http://localhost:5000/api/enigma'
url_de_enigma = 'http://localhost:5000/api/de_enigma'

P = np.random.permutation(np.eye(37))
P = P.tolist()
E = np.random.permutation(np.eye(37))
E = E.tolist()

msg = "hello world"

response_enigma = requests.post(url_enigma, json={'msg': msg, 'P': P, 'E': E})
print(response_enigma.json())

