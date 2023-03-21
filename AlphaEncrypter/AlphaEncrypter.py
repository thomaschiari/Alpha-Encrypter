import numpy as np
import unidecode
import string
import copy

# converte uma string de mensagem em uma matriz de one-hot encoding
def para_one_hot(msg: str) -> np.array:
    if isinstance(msg, np.ndarray):
        M = msg
    else:
        M = np.zeros((37, len(msg)))  # matriz de zeros 37xN, onde N é o comprimento da mensagem
        msg = msg.lower()  # converte a mensagem em minúsculas
        msg = unidecode.unidecode(msg)  # remove acentos e caracteres especiais
        char_list = list(string.ascii_lowercase)  # lista de letras minúsculas do alfabeto
        numbers = list(range(10))  # lista de números de 0 a 9
        char_list.extend(numbers)  # adiciona os números à lista de caracteres
        char_list.append(' ')  # adiciona o espaço à lista de caracteres
        dict_char = {str(char_list[i]): i for i in range(len(char_list))}  # cria um dicionário para mapear cada caractere a um índice inteiro
        for i in range(len(msg)):
            M[dict_char[msg[i]], i] = 1  # define o valor 1 na posição correspondente à letra ou número na matriz
    return M

# converte uma matriz de one-hot encoding em uma string de mensagem
def para_string(M: np.array) -> np.array:
    char_list = list(string.ascii_lowercase)  # lista de letras minúsculas do alfabeto
    numbers = list(range(10))  # lista de números de 0 a 9
    char_list.extend(numbers)  # adiciona os números à lista de caracteres
    char_list.append(' ')  # adiciona o espaço à lista de caracteres
    dict_char = {i: str(char_list[i]) for i in range(len(char_list))}  # cria um dicionário para mapear cada índice inteiro a um caractere
    msg = ''
    for i in range(M.shape[1]):
        msg += dict_char[np.argmax(M[:, i])]  # encontra o índice (ou posição) com o maior valor em cada coluna da matriz e o mapeia para o caractere correspondente
    return msg

# criptografa uma mensagem utilizando uma matriz de permutação P
def cifrar(msg: str, P: np.array) -> str:
    M = para_one_hot(msg)  # converte a mensagem em uma matriz de one-hot encoding
    MC = P @ M  # multiplica a matriz de permutação P pela matriz da mensagem
    return para_string(MC)  # converte a matriz criptografada em uma string de mensagem

# descriptografa uma mensagem criptografada utilizando uma matriz de permutação inversa de P
def de_cifrar(msg: str, P: np.array) -> str:
    M = para_one_hot(msg)  # converte a mensagem criptografada em uma matriz de one-hot encoding
    MP = np.linalg.inv(P) @ M  # multiplica a matriz inversa de P pela matriz da mensagem criptografada
    return para_string(MP)  # converte a matriz descriptografada em uma string de mensagem

# Criptografa uma mensagem utilizando o algoritmo Enigma
def enigma(msg: str, P: np.array, E: np.array) -> (str, np.array, np.array):
    # Inicializa a mensagem cifrada como uma string vazia
    msg_cifrada = ""
    # Inicializa o índice i como 0
    i = 0
    # Itera enquanto i for menor que o comprimento da mensagem
    for caractere in msg:
        caractere_enigma = cifrar(caractere, P)
        # Cifra a porção da mensagem de tamanho 37 com a matriz E e armazena na mensagem cifrada
        for _ in range(i):
            caractere_enigma = cifrar(caractere_enigma, E)
        msg_cifrada += caractere_enigma
        i += 1
    return msg_cifrada, P, E

# Descriptografa uma mensagem criptografada utilizando o algoritmo Enigma
def de_enigma(msg: str, P: np.array, E: np.array) -> str:
    # Inicializa a mensagem decifrada como uma string vazia
    msg_decifrada = ""
    # Inicializa o índice i como 0
    i = 0
    # Itera enquanto i for menor que o comprimento da mensagem
    for caractere in msg:
        caractere_enigma = caractere
        # Decifra a porção da mensagem de tamanho 37 com a matriz E e armazena na mensagem decifrada
        for _ in range(i):
            caractere_enigma = de_cifrar(caractere_enigma, E)
        msg_decifrada += de_cifrar(caractere_enigma, P)
        i += 1
    return msg_decifrada
