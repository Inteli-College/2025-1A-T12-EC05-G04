import pandas as pnd
import pydobot
import os
from serial.tools import list_ports

os.system('sudo chmod 666 /dev/ttyACM0')

isInputing = True
currentInput = 0
available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[32].device
d = pydobot.Dobot(port='/dev/ttyACM0', verbose=False)
d.speed(200)

tipoAcao = []
valorGrab = []
posicaoX = []
posicaoY = []
posicaoZ = []


while isInputing:
    tipoAcao.append(input("Digite o tipo de ação (1: movimento, 2: movimento com leitura, 3: pegar/soltar): \n"))
    if(tipoAcao[currentInput] == "3"):
        valorGrab.append(input("Digite o valor de pegada: \n"))
        posicaoX.append("0")
        posicaoY.append("0")
        posicaoZ.append("0")
    elif(tipoAcao[currentInput] == "1" or tipoAcao[currentInput] == "2"):
        valorGrab.append("0")
        (x, y, z, r, j1, j2, j3, j4) = d.pose()
        posicaoX.append(x)
        posicaoY.append(y)
        posicaoZ.append(z)
    finalizar = input("Deseja finalizar? (S/N) \n")
    if finalizar == "S" or finalizar == "s":
        isInputing = False
    else:
        currentInput += 1

fileName = input("Digite o nome do arquivo: \n")
df = pnd.DataFrame({
    'tipoAcao': tipoAcao,
    'valorGrab': valorGrab,
    'x': posicaoX,
    'y': posicaoY,
    'z': posicaoZ
    
})
df.to_json(fileName + ".instrucao")