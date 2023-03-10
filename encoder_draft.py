import numpy as np
import unidecode
import string


class EnigmaEncoder:

    def __init__(self):
        __char_list = list(string.ascii_lowercase)
        __numbers = list(range(10))
        __char_list.extend(__numbers)
        __char_list.append(' ')
        self.dict_char = {__char_list[i]: i for i in range(len(__char_list))}
        print(self.dict_char)

    def para_one_hot(self, msg: str):
        M = np.zeros((37, len(msg)))
        msg = msg.lower()
        msg = unidecode.unidecode(msg)
        for i in range(len(msg)):
            M[self.dict_char[msg[i]], i] = 1
        return M

    def para_string(self, M: np.array):
        msg = ''
        for i in range(M.shape[1]):
            idx = np.argmax(M[:, i])
            msg += self.dict_char[idx]
        return msg

    def cifrar(self, msg: str, P: np.array):
        M = self.para_one_hot(msg)
        MC = P @ M
        return self.para_string(MC)

    def de_cifrar(self, msg: str, P: np.array):
        M = self.para_one_hot(msg)
        MP = np.linalg.inv(P) @ M
        return self.para_string(MP)

    def enigma(self, msg: str, P: np.array, E: np.array):
        M = self.para_one_hot(msg)
        PC = P @ E
        MC = PC @ M
        return self.para_string(MC)

    def de_enigma(self, msg: str, P: np.array, E: np.array):
        M = self.para_one_hot(msg)
        PP = np.linalg.inv(E) @ P
        MP = np.linalg.inv(PP) @ M
        return self.para_string(MP)

if __name__ == '__main__':
    n = 37
    P = np.eye(n)
    np.random.shuffle(P)
    E = np.eye(n)
    np.random.shuffle(E)
    msg = 'hello world'
    encoder = EnigmaEncoder()
    msg_cifrado = encoder.enigma(msg, P, E)
    msg_decifrado = encoder.de_enigma(msg_cifrado, P, E)
    print(msg)