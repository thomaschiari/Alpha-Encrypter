import numpy as np
import unidecode
import string


class EnigmaEncoder:

    def __init__(self):
        char_list = list(string.ascii_lowercase)
        numbers = list(range(10))
        char_list.extend(numbers)
        char_list.append(' ')
        self.dict_char = {char_list[i]: i for i in range(len(char_list))}

    def para_one_hot(self, msg):
        M = np.zeros((37, len(msg)))
        msg = msg.lower()
        msg = unidecode.unidecode(msg)
        for i in range(len(msg)):
            M[self.dict_char[msg[i]], i] = 1
        return M

    def para_string(self, M: np.array):
        msg = ''
        for i in range(M.shape[1]):
            msg += self.dict_char[np.argmax(M[:, i])]
        return msg

