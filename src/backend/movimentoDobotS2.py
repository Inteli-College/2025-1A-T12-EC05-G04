import pydobot
import os
import pandas
from serial.tools import list_ports
from leitorInstrucao import lerJsonMovimento
from parserComando import lerComando

#No linux, garante que a porta está acessível para o sistema
os.system('sudo chmod 666 /dev/ttyACM0')

#Conecta com o dobot pela porta disponível
d = pydobot.Dobot(port='/dev/ttyACM0', verbose=False)
d.speed(200)
estaRodando = True

while estaRodando:
    modo = input("Selecione modo (1: Instrução, 2: Manual, Qualquer outra coisa: Sair): \n")
    #Modo de instrução
    if(modo == "1"):
        #Carrega dataframe de instrução
        dfInstrucao = lerJsonMovimento()
        print(dfInstrucao)
        #Para cada linha de instrução, executa a ação da linha
        for index in dfInstrucao.index:
            if(dfInstrucao["tipoAcao"][index] == 1):
                # Se move para a posição da instrução se ação for tipo 1
                d.move_to(float(dfInstrucao["x"][index]), float(dfInstrucao["y"][index]), float(dfInstrucao["z"][index]), r=0, wait=True)
            elif(dfInstrucao["tipoAcao"][index] == 2):
                # Se ação for tipo 2, executa ação de pegar ou soltar
                if(dfInstrucao["valorGrab"][index] == 1):
                    print("Suck")
                    d.suck(True)
                elif(dfInstrucao["valorGrab"][index] == 0):
                    print("Unsuck")
                    d.suck(False)
            d.wait(500)
    elif(modo == "2"):
        # Entra no modo manual
        rodandoManual = True
        while rodandoManual:
            #Chama o parser de comando para separar o encadeamento. Teoricamente suporta infinitos comandos encadeados
            comandos = lerComando()
            for comando in comandos:
                (x, y, z, r, j1, j2, j3, j4) = d.pose()
                match comando:
                    case "moveX":
                        units = float(input("Insira a quantidade de unidades \n"))
                        d.move_to(x+units, y,z,r=0, wait=True)
                    case "moveY":
                        units = float(input("Insira a quantidade de unidades \n"))
                        d.move_to(x,y+units, z, r=0, wait=True)
                    case "moveZ":
                        units = float(input("Insira a quantidade de unidades \n"))
                        d.move_to(x,y,z+units, r=0, wait=True)
                    case "suck":
                        d.suck(True)
                    case "unsuck":
                        d.suck(False)           
                    case "sair":
                        rodandoManual=False
    else:
        estaRodando = False

#Termina conexão
d.close()