import re

def rodarComando(device, comando):
    #Pega a referência da posição atual do dobot
    (x, y, z, r, j1, j2, j3, j4) = device.pose()
    if ('(' in comando):
        instrucao = comando.split('(')[0]
        valor = re.search(r'\((.*?)\)', comando)
        if not valor:
            raise ValueError('command_value_not_found')
        valor = valor.group(1)
    else:
        instrucao = comando
        valor = None
    match comando:
        case "moveX":
            units = float(input("Insira a quantidade de unidades \n"))
            device.move_to(x+units, y,z,r=0, wait=True)
            currentPose = device.pose()
            if currentPose[0] not in range(x+units-1, x+units+1):
                raise ValueError('move_not_executed_correctly')
        case "moveY":
            units = float(input("Insira a quantidade de unidades \n"))
            device.move_to(x,y+units, z, r=0, wait=True)
            currentPose = device.pose()
            if(currentPose[1] not in range(y+units-1, y+units+1)):
                raise ValueError('move_not_executed_correctly')
        case "moveZ":
            units = float(input("Insira a quantidade de unidades \n"))
            device.move_to(x,y,z+units, r=0, wait=True)
            currentPose = device.pose()
            if(currentPose[2] not in range(z+units-1, z+units+1)):
                raise ValueError('move_not_executed_correctly')
        case "suck":
            device.suck(True)
        case "unsuck":
            device.suck(False)
        case "moveTo":
            x = float(input("Insira a posição x \n"))
            y = float(input("Insira a posição y \n"))
            z = float(input("Insira a posição z \n"))
            device.move_to(x,y,z,r=0, wait=True)
            currentPose = device.pose()
            if currentPose[0] not in range(x-1, x+1) or currentPose[1] not in range(y-1, y+1) or currentPose[2] not in range(z-1, z+1):
                raise ValueError('move_not_executed_correctly')
        case _:
            raise ValueError('command_not_found')