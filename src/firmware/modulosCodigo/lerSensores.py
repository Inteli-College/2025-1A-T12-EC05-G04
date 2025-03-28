import serial as s
from time import sleep



def lerQR(port = '/dev/ttyUSB0'):
    ser = s.Serial(port, 9600)
    while True:
        tries = 0
        while tries < 5:
            valor = ser.readline().decode().strip()
            if valor != '':
                ser.close()
                return valor
            else:
                tries += 1
                continue
        if tries == 5:
            ser.close()
            raise ValueError('qr_not_read')
        sleep(0.5)


def lerInfra(port = '/dev/ttyACM0'):
    ser = s.Serial(port, 9600)
    while True:
        valor = ser.readline().decode().strip()
        if valor != '':
            ser.close()
            return valor
        else:
            continue