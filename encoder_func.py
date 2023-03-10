import numpy as np
import unidecode
import string
import copy


def para_one_hot(msg):
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

def para_string(M: np.array):
    char_list = list(string.ascii_lowercase)
    numbers = list(range(10))
    char_list.extend(numbers)
    char_list.append(' ')
    dict_char = {i: str(char_list[i]) for i in range(len(char_list))}
    msg = ''
    for i in range(M.shape[1]):
        msg += dict_char[np.argmax(M[:, i])]
    return msg

def cifrar(msg, P):
    M = para_one_hot(msg)
    MC = P @ M
    return para_string(MC)

def de_cifrar(msg, P):
    M = para_one_hot(msg)
    MP = np.linalg.inv(P) @ M
    return para_string(MP)

def enigma(msg, P, E):
    M = para_one_hot(msg)
    PC = P @ E
    MC = PC @ M
    return para_string(MC)

def de_enigma(msg, P, E):
    M = para_one_hot(msg)
    PP = np.linalg.inv(E) @ P
    MP = np.linalg.inv(PP) @ M
    return para_string(MP)

n = 37
P = np.eye(n)
np.random.shuffle(P)
E = copy.deepcopy(P)
np.random.shuffle(E)


print(de_cifrar(cifrar('hello world', P), P))

enigma = enigma('hello world', P, E)
print(enigma)

deenigma = de_enigma(enigma, P, E)
print(deenigma)