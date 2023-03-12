import requests
import json
import numpy as np


url_enigma = 'http://localhost:5000/api/enigma'
url_de_enigma = 'http://localhost:5000/api/de_enigma'

msg = 'hello world'
P = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
E = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

response_enigma = requests.post(url_enigma, json={'msg': msg, 'P': P, 'E': E})
response_de_enigma = requests.post(url_de_enigma, json={'msg': response_enigma.text, 'P': P, 'E': E})

print('Original message:', msg)
print('Encoded message:', response_enigma.text)
print('Decoded message:', response_de_enigma.text)