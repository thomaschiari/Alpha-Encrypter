# gAAAAABkAPMmGJYkdZOZKCs4OIw7BPK9W80RTG5moJzbnu88C7tixQkEJ0jKacsoy2FZTadiruofJnDrLHm7rpFYzXwXX5J-0t0_1p5LEPVFkENZHQ2VMPI=
Implementação de um pacote para criptografia Enigma para a disciplina de Álgebra Linear

### Autores:
- Marcelo Rabello Barranco
- Thomas Chiari Ciocchetti de Souza

Para descriptografar o título, use a chave disponível no arquivo ```key.key```!


# REST API

## API Reference

#### Get all items

```http
  POST /api/enigma
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `msg`     | `string` | **Required**. Menssagem    |

#### Get item

```http
  POST /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `msg`     | `string` | **Required**. Mensagem cryptografada |
| `P`       | `list`   | **Required**. Matriz P do return da rota anterior |
| `E`       | `list`   | **Required**. Matriz E do return da rota anterior |

#### test_api.py

A api pode ser testada usando esse arquivo

