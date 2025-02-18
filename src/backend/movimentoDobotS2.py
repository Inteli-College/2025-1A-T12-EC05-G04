import pydobot
import os
import pandas
from serial.tools import list_ports
from leitorInstrucao import lerJsonMovimento

os.system('sudo chmod 666 /dev/ttyACM0')

d = pydobot.Dobot(port='/dev/ttyACM0', verbose=False)
d.speed(100)
estaRodando = True

while estaRodando:
    modo = input("Selecione modo (1: Instrução, 2: Manual, Qualquer outra coisa: Sair): \n")
    if(modo == "1"):
        dfInstrucao = lerJsonMovimento()
        print(dfInstrucao)
        for index in dfInstrucao.index:
            if(dfInstrucao["tipoAcao"][index] == 1):
              d.move_to(float(dfInstrucao["x"][index]), float(dfInstrucao["y"][index]), float(dfInstrucao["z"][index]), r=0, wait=True)
            elif(dfInstrucao["tipoAcao"][index] == 2):
                print("Action")
                if(dfInstrucao["valorGrab"][index] == 1):
                    print("Suck")
                    d.suck(True)
                elif(dfInstrucao["valorGrab"][index] == 0):
                    print("Unsuck")
                    d.suck(False)
            d.wait(500)
    elif(modo == "2"):
        rodandoManual = True
        while rodandoManual:
            comando = input("Insira o comando: \n")
            (x, y, z, r, j1, j2, j3, j4) = d.pose()
            if(comando == "moveX"):
                units = float(input("Insira a quantidade de unidades \n"))
                d.move_to(x+units, y,z,r=0, wait=True)
            elif(comando == "moveY"):
                units = float(input("Insira a quantidade de unidades \n"))
                d.move_to(x,y+units, z, r=0)
            elif(comando == "moveZ"):
                units = float(input("Insira a quantidade de unidades \n"))
                d.move_to(x,y,z+units, r=0)
            elif(comando == "sair"):
                rodandoManual=False


    else:
        estaRodando = False


d.close()