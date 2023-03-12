import flask
from flask import request, jsonify
import numpy as np
import json
import string
from encoder_func import *
import flask_cors

app = flask.Flask(__name__)
app.config["DEBUG"] = True
flask_cors.CORS(app)

@app.route('/api/enigma', methods=['POST'])
def enigma_route():
    data = request.json
    msg = data.get('msg')
    P = np.array(data.get('P'))
    E = np.array(data.get('E'))

    # Chama a função enigma com os parâmetros recebidos
    msg_cifrada = enigma(msg, P, E)

    # Retorna o resultado como JSON
    return jsonify({'msg_cifrada': msg_cifrada})

@app.route('/api/de_enigma', methods=['POST'])
def de_enigma_route():
    data = request.json
    msg_cifrada = data.get('msg_cifrada')
    P = np.array(data.get('P'))
    E = np.array(data.get('E'))

    # Chama a função de_cifrar com os parâmetros recebidos
    msg_original = de_cifrar(msg_cifrada, P, E)

    # Retorna o resultado como JSON
    return jsonify({'msg_original': msg_original})

if __name__ == '__main__':
    app.run(debug=True)


app.run()


