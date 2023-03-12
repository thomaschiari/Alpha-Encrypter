import numpy as np
import unidecode
import string
import copy


def para_one_hot(msg: str) -> np.array:
    if isinstance(msg, np.ndarray):
        M = msg
    else:
        M = np.zeros((37, len(msg)))
        msg = msg.lower()
        msg = unidecode.unidecode(msg)
        char_list = list(string.ascii_lowercase)
        numbers = list(range(10))
        char_list.extend(numbers)
        char_list.append(' ')
        dict_char = {str(char_list[i]): i for i in range(len(char_list))}
        for i in range(len(msg)):
            M[dict_char[msg[i]], i] = 1
    return M


def para_string(M: np.array) -> np.array:
    char_list = list(string.ascii_lowercase)
    numbers = list(range(10))
    char_list.extend(numbers)
    char_list.append(' ')
    dict_char = {i: str(char_list[i]) for i in range(len(char_list))}
    msg = ''
    for i in range(M.shape[1]):
        msg += dict_char[np.argmax(M[:, i])]
    return msg

def cifrar(msg: str, P: np.array) -> str:
    M = para_one_hot(msg)
    MC = P @ M
    return para_string(MC)

def de_cifrar(msg: str, P: np.array) -> np.array:
    M = para_one_hot(msg)
    MP = np.linalg.inv(P) @ M
    return MP

def enigma(msg: str, P: np.array, E: np.array) -> str:
    msg_cifrada = ""
    i = 0
    while i < len(msg):
        msg_cifrada += cifrar(msg[i:i+37], P)
        i += 37
    msg_cifrada = para_one_hot(msg_cifrada)
    msg_cifrada = E @ msg_cifrada
    msg_cifrada = para_string(msg_cifrada)
    return msg_cifrada, P, E

def de_enigma(msg: str, P: np.array, E: np.array) -> str:
    msg_decifrada = ""
    i = 0
    while i < len(msg):
        msg_decifrada += cifrar(msg[i:i+37], np.linalg.inv(E))
        i += 37
    msg_decifrada = para_one_hot(msg_decifrada)
    msg_decifrada = np.linalg.inv(P) @ msg_decifrada
    msg_decifrada = para_string(msg_decifrada)
    return msg_decifrada
