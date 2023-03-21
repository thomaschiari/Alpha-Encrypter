from setuptools import find_packages, setup

setup(
    name='AlphaEncrypter',
    packages=find_packages(include=['AlphaEncrypter']),
    version='0.1.2',
    description='Dont be Sigma, be Alpha, encrypt your messages with AlphaEncrypter',
    author='Marcelo Rabello Barranco, Thomas Chiari Ciocchetti de Souza',
    license='MIT',
    install_requires=[
        'pip',
        'requests',
        'numpy',
        'flask',
        'setuptools',
        'unidecode',
    ],
)
