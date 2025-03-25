import pydobot
import os
import pandas
from serial.tools import list_ports
# Script de leitura de arquivo de instrução
from modulosCodigo.leitorInstrucao import lerJsonMovimento
# Script de parser de comando do modo manual
from modulosCodigo.parserComando import lerComando
# Script de execução de comando do modo manual
from modulosCodigo.seletorComandos import rodarComando
from modulosCodigo.lerSensores import lerQR, lerInfra

def execComando(comando, port):
    d = pydobot.Dobot(port)
    #Antigamente havia uma lógica de seleção e leitura de linhas de comando aqui. Com a mudança de CLI para interface, não será mais necessário essa leitura
    #Pensando nisso, parece meio redundante utilizar essa função, que será chamada no ws_client, para chamar outra função ao invés de invocar diretamente a função rodarComando
    #Apesar disso, acredito eu que isto deixa o código mais limpo no ws_client, focando apenas na comunicação com o servidor, enquanto este cuida das interações com o físico
    rodarComando(d, comando)

def lerQrCode(port):
    try:
        qr = lerQR(port)
        if 'bin:' not in qr:
            raise ValueError('qr_read_invalid')
        return qr
    except ValueError as e:
        return str(e)
    
def lerSensorInfra(port):
    try:
        valor = lerInfra(port)
        return valor
    except ValueError as e:
        return str(e)