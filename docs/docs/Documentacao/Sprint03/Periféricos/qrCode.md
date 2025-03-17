---
title: Leitor de QR Code
slug: perifericos/qrcode
sidebar_position: 1
---

## Visão Geral
O leitor de QR Code é um dos periféricos essenciais do robô, responsável por garantir a correta identificação dos remedios manipulados. Esse processo é fundamental para evitar erros na coleta e distribuição dos remedios, assegurando que cada item seja tratado conforme o esperado.

## Função no Projeto
O robô utiliza o leitor de QR Code para verificar se o objeto coletado corresponde ao esperado. Ao escanear um código QR, o sistema interpreta os dados e os compara com as informações armazenadas no banco de dados ou em um sistema de controle. Caso haja alguma inconsistência, o robô pode sinalizar a necessidade de verificação ou correção da coleta.

## Código do Leitor de QR Code
A implementação do leitor de QR Code foi feita utilizando a biblioteca `serial`, permitindo a comunicação com o dispositivo conectado à porta USB.

```python
import serial as s

def lerQR():
     ser = s.Serial('/dev/ttyUSB0', 9600)
     while True:
         valor = ser.readline().decode().strip()
         if valor != '':
             ser.close()
             return valor
         else:
             continue
```

## Explicação do Código
1. **Inicialização da Comunicação Serial**: O código inicializa a comunicação serial com o leitor de QR Code através da porta `/dev/ttyUSB0` com uma taxa de transmissão de 9600 bps.
2. **Leitura Contínua**: Um loop é utilizado para aguardar a entrada de um código QR.
3. **Processamento da Leitura**: O dado lido é decodificado e formatado para remover espaços extras.
4. **Retorno da Informação**: Se um valor válido for detectado, a comunicação serial é encerrada e a informação do QR Code é retornada.

