import pydobot
import os
from serial.tools import list_ports
# Script de leitura de arquivo de instrução
from modulosCodigo.leitorInstrucao import lerJsonMovimento
# Script de parser de comando do modo manual
from modulosCodigo.parserComando import lerComando
# Script de execução de comando do modo manual
from modulosCodigo.seletorComandos import rodarComando

from modulosCodigo.instrucoesDobot import execInstrucao

def execComando(comando, port='/dev/ttyACM1'):
    d = pydobot.Dobot(port)
    #Antigamente havia uma lógica de seleção e leitura de linhas de comando aqui. Com a mudança de CLI para interface, não será mais necessário essa leitura
    #Pensando nisso, parece meio redundante utilizar essa função, que será chamada no ws_client, para chamar outra função ao invés de invocar diretamente a função rodarComando
    #Apesar disso, acredito eu que isto deixa o código mais limpo no ws_client, focando apenas na comunicação com o servidor, enquanto este cuida das interações com o físico
    rodarComando(d, comando)

def rodarInstrucao(instrucao, port='/dev/ttyACM0', callback=None, id_montagem=None):
    verificarPorta()
    d = pydobot.Dobot(port)
    result, qr = execInstrucao(d, instrucao, callback=callback, id_montagem=id_montagem)
    return result, qr
    

def verificarPorta():
    available_ports = list_ports.comports()
    print(f'available ports: {[x.device for x in available_ports]}')
