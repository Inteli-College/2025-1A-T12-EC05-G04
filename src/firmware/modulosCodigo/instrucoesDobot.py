import pandas as pd
from modulosCodigo.lerSensores import lerQR, lerInfra

def execInstrucao(d, instrucao, callback=None, id_montagem=None):
    dfInstrucao = pd.DataFrame(eval(instrucao))
    qrLido = ''
    shouldHaveGot = False
    print(dfInstrucao.index)
    for index in dfInstrucao.index:
            if(dfInstrucao["tipoAcao"][index] == "2" or dfInstrucao["tipoAcao"][index] == "1"):
                if callback:
                    
                    message = f'move_pos(x:{dfInstrucao["x"][index]}, y: {dfInstrucao["y"][index]}, z:{dfInstrucao["z"][index]}'

                    print(f'index: {index}' )
                    callback((int(index)+1) / len(dfInstrucao), message, id_montagem)
                    print("Enviou callback")
                # Se move para a posição da instrução se ação for tipo 1
                d.move_to(float(dfInstrucao["x"][index]), float(dfInstrucao["y"][index]), float(dfInstrucao["z"][index]), r=0, wait=True)
                d.wait(1000)
                poseAtual = d.pose()
                if not (dfInstrucao["x"][index] - 1 <= poseAtual[0] <= dfInstrucao["x"][index] + 1) or not dfInstrucao["y"][index] - 1 <= poseAtual[1] <= dfInstrucao["y"][index] + 1 or not dfInstrucao["z"][index] - 1 <= poseAtual[2] <= dfInstrucao["z"][index] + 1:
                    raise ValueError(f'move_not_executed_correctly: Expected to be around {dfInstrucao["x"][index]}, {dfInstrucao["y"][index]}, {dfInstrucao["z"][index]},  but is at {poseAtual[0]}, {poseAtual[1]}, {poseAtual[2]}')
                if dfInstrucao["tipoAcao"][index] == "2":
                    try:
                        qrLido = lerQrCode('/dev/ttyUSB0')
                        print(qrLido)
                    except ValueError as e:
                        # Se não conseguir ler o QR Code, levanta exceção. Deve impedir o resto da execução mas verifico amanhã (26/03)
                        raise e
            elif(dfInstrucao["tipoAcao"][index] == "3"):
                if(dfInstrucao["valorGrab"][index] == "1"):
                    print("Suck")
                    d.suck(True)
                    shouldHaveGot = True
                elif(dfInstrucao["valorGrab"][index] == "0"):
                    print("Unsuck")
                    d.suck(False)
                    shouldHaveGot = False
        
            d.wait(500)
    callback(1.00, message, id_montagem)
    return 2, qrLido


def lerQrCode(port='/dev/ttyUSB0'):
    try:
        qr = lerQR(port)
        #Verifica se a formatação está correta com o qrcode
        if 'bin:' not in qr:
            raise ValueError('qr_read_invalid')
        return qr
    except ValueError as e:
        return str(e)
    
def lerSensorInfra(port='/dev/ttyACM0'):
    try:
        valor = lerInfra(port)
        if('irread:' not in valor):
            raise ValueError('no_ir_read')
        print(valor)
        return int(valor.split(':')[1]) < 20000
    except ValueError as e:
        return str(e)