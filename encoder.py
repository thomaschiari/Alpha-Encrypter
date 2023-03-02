import numpy as np
import unidecode
import string


def para_one_hot(msg):
    M = np.zeros((37, len(msg)))
    msg = msg.lower()
    msg = unidecode.unidecode(msg)
    char_list = list(string.ascii_lowercase)
    numbers = list(range(10))
    char_list.extend(numbers)
    char_list.append(' ')

    dict_char = {char_list[i]: i for i in range(len(char_list))}

    for i in range(len(msg)):
        M[dict_char[msg[i]], i] = 1

    return M


def para_string(M: np.array):
    char_list = list(string.ascii_lowercase)
    numbers = list(range(10))
    char_list.extend(numbers)
    char_list.append(' ')
    dict_char = {i: char_list[i] for i in range(len(char_list))}

    msg = ''
    for i in range(M.shape[1]):
        msg += dict_char[np.argmax(M[:, i])]

    return msg
