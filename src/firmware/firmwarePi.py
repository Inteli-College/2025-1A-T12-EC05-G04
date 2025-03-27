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

def rodarInstrucao(instrucao, port='/dev/ttyACM1'):
    d = pydobot.Dobot(port)
    execInstrucao(d, instrucao)

def verificarPorta():
    available_ports = list_ports.comports()
    print(f'available ports: {[x.device for x in available_ports]}')

verificarPorta()
rodarInstrucao('{"tipoAcao":{"0":"1","1":"1","2":"2","3":"1","4":"3","5":"1","6":"1","7":"3"},"valorGrab":{"0":"0","1":"0","2":"0","3":"0","4":"1","5":"0","6":"0","7":"0"},"x":{"0":226.9400024414,"1":354.7524719238,"2":234.8511962891,"3":307.1087646484,"4":"0","5":307.1087646484,"6":338.8617248535,"7":"0"},"y":{"0":-8.8123865128,"1":-72.7444534302,"2":-96.7423095703,"3":-74.8153915405,"4":"0","5":-74.8153915405,"6":-56.0145263672,"7":"0"},"z":{"0":142.8887023926,"1":72.2275466919,"2":61.2597045898,"3":-57.2363128662,"4":"0","5":-57.2363128662,"6":71.1682739258,"7":"0"}}')