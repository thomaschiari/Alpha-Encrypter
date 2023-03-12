import requests
import json
import numpy as np

data = {
    'msg': 'Hello'
}

response = requests.post('http://127.0.0.1:5000/api/onehot', json=data)
print(response.content.decode('utf-8'))

data = {
    "msg": [
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        1.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        1.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        1.0,
        1.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        1.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ]
]
    
}

response = requests.post('http://localhost:5000/api/string', json=data)
print(response.content.decode('utf-8'))


# url_enigma = 'http://localhost:5000/api/enigma'
# url_de_enigma = 'http://localhost:5000/api/de_enigma'

# msg = 'hello world'
# P = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# E = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# response_enigma = requests.post(url_enigma, json={'msg': msg, 'P': P, 'E': E})
# response_de_enigma = requests.post(url_de_enigma, json={'msg': response_enigma.text, 'P': P, 'E': E})

# print('Original message:', msg)
# print('Encoded message:', response_enigma.text)
# print('Decoded message:', response_de_enigma.text)