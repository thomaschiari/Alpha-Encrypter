import flask
from flask import request, jsonify
import numpy as np
import json
import string
from AlphaEncrypter.AlphaEncrypter import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/enigma', methods=['POST'])
def enigma_route():
    data = request.json
    msg = data.get('msg')
    P = np.random.permutation(np.eye(37))
    E = np.random.permutation(np.eye(37))

    # Chama a função enigma com os parâmetros recebidos
    msg_cifrada, P, E = enigma(msg, P, E)

    # Retorna o resultado como JSON
    return jsonify({'msg_cifrada': msg_cifrada,
                    'P': P.tolist(),
                    'E': E.tolist()})

@app.route('/api/de_enigma', methods=['POST'])
def de_enigma_route():
    data = request.json
    msg_cifrada = data.get('msg_cifrada')
    P = np.array(data.get('P'))
    E = np.array(data.get('E'))

    # Chama a função de_cifrar com os parâmetros recebidos
    msg_original = de_enigma(msg_cifrada, P, E)

    # Retorna o resultado como JSON
    return jsonify({'msg_original': msg_original})

if __name__ == '__main__':
    app.run(debug=True)


