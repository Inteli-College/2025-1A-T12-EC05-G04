def rodarComando(device, comando):
    (x, y, z, r, j1, j2, j3, j4) = device.pose()
    match comando:
        case "moveX":
            units = float(input("Insira a quantidade de unidades \n"))
            device.move_to(x+units, y,z,r=0, wait=True)
        case "moveY":
            units = float(input("Insira a quantidade de unidades \n"))
            device.move_to(x,y+units, z, r=0, wait=True)
        case "moveZ":
            units = float(input("Insira a quantidade de unidades \n"))
            device.move_to(x,y,z+units, r=0, wait=True)
        case "suck":
            device.suck(True)
        case "unsuck":
            device.suck(False)
