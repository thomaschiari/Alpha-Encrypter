# AlphaEncrypter: an implementation of the Enigma Machine

### Authors:
- Marcelo Rabello Barranco
- Thomas Chiari Ciocchetti de Souza

### Description

This project is an implementation of the Enigma Machine, a cryptography machine used by the German Army during World War II. The Enigma Machine was used to encrypt messages, and the encryption keys were changed every day.

In this project, we make the AlphaEncrypter package available so you can install it using ```pip```, and also a simple Flask API that you can run locally or deploy on any web service you might want. Both the package and the API will have the same functions.

### Installation
In order to install the package, you can use ```pip```. The installation of the package will already install the dependencies. You can do that in your local environment, or create a virtual environment instead.

```bash
python3 -m venv env 
```

```bash
source env/bin/activate
```

```bash
pip install AlphaEncrypter
```

To check that the installation was successful, you can run the following command:

```bash
pip list
```
If you find the packages AlphaEncrypter, Numpy, Flask and Unidecode on the list that follows, the installation went correct.

If you want a demonstration of the usage of the package, you can run the ```demo.py``` file. Remember that you must have the package installed at the same environment you are running the script.

If you want to use the API, you can clone the repository and install the dependencies. Below you will find the full API documentation.

### Usage
In order to use the package, you can import it in your code and use the functions. Below, we will show a sample code that can be helpful:

```python
from AlphaEncrypter.AlphaEncrypter import enigma, de_enigma
import numpy as np

# Generate random keys
P = np.random.permutation(np.eye(37))
E = np.random.permutation(np.eye(37))

# Encrypt the message
msg = "Hello World"
encrypted_msg = enigma(msg, P, E)

# Decrypt the message
decrypted_msg = de_enigma(encrypted_msg, P, E)
```

Note that the message must be a string and the keys must be numpy arrays. The message must only contain numbers, alphabet letters and spaces, and the program does not differentiate between upper and lower case letters. The keys must be square matrices with the same number of rows and columns, being permutations of the eye matrix, with 37 rows and 37 columns (the number of characters accepted by the program).


### Theory
Classic encryption algorithms usually use a cipher alphabet in order to encrypt a message. The Enigma algorithm, on the other hand, ciphers the cipher alphabet at every new character of the message. In this way, it is almost impossible to decrypt the message without knowing the keys used to encrypt it, as it is extremely hard to detect patterns. The Enigma Machine was used by the German Army during World War II, and it was considered unbreakable at the time.

In this project, the first step of the encryption is to turn the message into a matrix of ones and zeros, with the number one representing the character. This matrix has 37 lines, representing the 37 characters available in the algorithm, and the number of columns depends on the length of the message. This process is called "One Hot Encoding". In the end, it will deliver a matrix like the one that follows:

$$
\begin{bmatrix}
    1 & 0 & 0 & 1 & 0 & 0 \\
    0 & 1 & 0 & 0 & 1 & 0 \\
    0 & 0 & 1 & 0 & 0 & 1
\end{bmatrix}
$$

With the lines representing every character of the alphabet, and the ones representing whether at that position you have that character or not. Note that you cannot have more than one character at the same column. In the case above, the message would have only 3 characters available. In the matrix used in the package, the matrix has 37 lines representing every single character.

The next step is to multiply the permutation square matrix P, with the same number of lines, by the One-Hot encoded matrix provided. This matrix is a permutation of the eye matrix, and it is used to shuffle the columns of the matrix. The result of this multiplication is a matrix with the same number of lines and columns. The Permutation Matrix will be similar to an eye matrix, but with the ones and zeros shuffled.

The result will be a matrix with shuffled ones and zeros, like the one that follows:

$$
\begin{bmatrix}
    0 & 0 & 1 & 0 & 0 & 1 \\
    1 & 0 & 0 & 1 & 0 & 0 \\
    0 & 1 & 0 & 0 & 1 & 0
\end{bmatrix}
$$

If the original message was *ABCABC*, the encrypted message will now be *BCABCA*, for instance.

The Enigma Algorithm adds another step: at every character of the message, the permutation matrix P will be shuffled, as it will be multiplied by the permutation matrix E. The permutation matrix E is also a permutation of the eye matrix, and is called an Auxiliary Cipher.

After that process, the program will use the One-Hot Encoding algorithm to turn the result of all those permutations into a string in order to return the encrypted message.



---
# REST API

## API Reference

#### Encrypt the message with random keys

```http
  POST /api/enigma
```

| Parameter | Type     | Description               |
| :-------- | :------- |:--------------------------|
| `msg`     | `string` | **Required**. Mensagem    |

#### Encrypt the message with existing keys

```http
  POST /api/enigma_keys
```

| Parameter | Type     | Description                          |
|:----------|:---------|:-------------------------------------|
| `msg`     | `string` | **Required**. Mensagem               |
| `P`       | `list`   | **Required**. Matriz de Permutação P |
| `E`       | `list`   | **Required**. Matriz de Permutação E |

#### Decrypt the message with the keys

```http
  POST /api/de_enigma
```

| Parameter | Type     | Description                                                |
| :-------- | :------- |:-----------------------------------------------------------|
| `msg`     | `string` | **Required**. Mensagem cryptografada                       |
| `P`       | `list`   | **Required**. Matriz P utilizada para encriptar a mensagem |
| `E`       | `list`   | **Required**. Matriz E utilizada para encriptar a mensagem |

### Run Locally

To run the project locally, clone the project and install the dependencies.

```bash
  git clone https://github.com/thomaschiari/Algebra-Linear-Enigma.git
```
    
```bash
cd Algebra-Linear-Enigma
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```
In order to test the API, you can use the script ```test_api.py```. You can also edit it to add your own keys, or to test the API with your own messages. Just keep in mind the requirements for the keys and the message.

```bash
python test_api.py
```

