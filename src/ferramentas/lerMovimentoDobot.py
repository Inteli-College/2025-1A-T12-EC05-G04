import pydobot
import os
from serial.tools import list_ports


os.system('sudo chmod 666 /dev/ttyACM0')

# Conecta com o Dobot
available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[32].device
d = pydobot.Dobot(port='/dev/ttyACM0', verbose=False)
d.speed(100)
readingPoses = True

while readingPoses:
    (x, y, z, r, j1, j2, j3, j4) = d.pose()
    print(f'x:{x} y:{y} z:{z}')
    os.system(f'echo "x:{x} y:{y} z:{z}" >> ./posicao.txt')
    continueReading = input("Deseja continuar lendo? (s/n): ")
    if continueReading == 'n':
        readingPoses = False
    elif continueReading != 's':
        print("Opção inválida, encerrando leitura.")
        readingPoses = False
d.close()