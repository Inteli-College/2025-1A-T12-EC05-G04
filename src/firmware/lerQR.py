import serial as s



def lerQR():
    ser = s.Serial('/dev/ttyUSB0', 9600)
    while True:
        valor = ser.readline().decode().strip()
        if valor != '':
            ser.close()
            return valor
        else:
            continue