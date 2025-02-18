import pydobot
import os
import pandas
from serial.tools import list_ports
from leitorInstrucao import lerJsonMovimento

os.system('sudo chmod 666 /dev/ttyACM0')

d = pydobot.Dobot(port='/dev/ttyACM0', verbose=False)
d.speed(100)

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

d.close()