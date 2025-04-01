---
title: Controle de instruções
slug: controle-instrucoes
sidebar_position: 2
---
# instrucoesDobot - Controle de instruções do braço

## Visão geral

&emsp;O módulo instrucoesDobot é responsável por controlar as instruções recebidas do servidor e repassá-las para o braço robótico Dobot. Ele é composto por um conjunto de funções que permitem a comunicação com o Dobot, a execução de instruções e o retorno de informações sobre o estado atual da montagem.

## LerQRCode(port='/dev/ttyUSB0')

&emsp;Essa função é responsável por ler um código QR e retornar o seu conteúdo. Chama outro código que retorna o valor serial do scanner utilizado, verificando também se segue a formatação correta de nossos códigos QR.

```python

def lerQrCode(port='/dev/ttyUSB0'):
    try:
        qr = lerQR(port)
        #Verifica se a formatação está correta com o qrcode
        if 'bin:' not in qr:
            raise ValueError('qr_read_invalid')
        return qr
    except ValueError as e:
        return str(e)
```

&emsp;Assim como a maioria das etapas desse código, a função é desenvolvida com a capacidade de voltar erros claros e específicos para o servidor, ao invés de simplesmente parar o código. Isso permite que um erro seja tratado de maneira mais eficiente e, principalmente, não atrapalhe o funcionamento geral ou necessite da reinicialização manual do sistema. Neste caso, são retornados erros caso o código QR não siga a formatação correta (qr_read_invalid) ou se nenhum código for lido depois de certo tempo (qr_not_read).

## LerSensorInfra(port='/dev/ttyACM0')

&emsp;Assim como a função acima, esta é responsável por ler um sensor infravermelho e retornar o seu valor. A diferença é que, ao invés de um código QR, ela retorna um valor booleano a depender da distância do sensor em relação a um objeto, indicando se o objeto foi pego ou não. Devido à limitações de tempo e necessidade de testar, a função foi retirada do loop principal de execução, mas pode ser facilmente implementada de volta.

```python
def lerQrCode(port='/dev/ttyUSB0'):
    try:
        qr = lerQR(port)
        #Verifica se a formatação está correta com o qrcode
        if 'bin:' not in qr:
            raise ValueError('qr_read_invalid')
        return qr
    except ValueError as e:
        return str(e)
```


## execInstrucao(d, instrucao, callback=None)

&emsp;Essa é a função principal que rege todas as ações do Dobot. Ela primeiro lê o json de instrução, e em seguida itera sobre cada linha da instrução, executando um comando diferente dependendo dos valores. A função também chama a função de callback, que retorna o estado atual da montagem para o servidor.
&emsp;Primeiramente, as ações de ID 1 e 2 configuram movimentos do Dobot, com a diferença de que a ação 1 realiza apenas um movimento simples, enquanto a 2 espera uma leitura de código QR ao final. A ação 3 é responsável pela ventosa sugadora na ponta do robô. Ambas as primeiras ações recebem como parâmetro as posições X,Y e Z do Dobot, enquanto a terceira recebe um valor numérico valorGrab de 0 ou 1, indicando se a ventosa deve ser desativada ou ativada, respectivamente. Novamente há o tratamento de erros na função, indicando qual foi o problema atual, seja leitura errada de QR ou erro na movimentação
```python
ef execInstrucao(d, instrucao, callback=None):
    dfInstrucao = pd.DataFrame(eval(instrucao))
    qrLido = ''
    shouldHaveGot = False
    for index in dfInstrucao.index:
            if(dfInstrucao["tipoAcao"][index] == "2" or dfInstrucao["tipoAcao"][index] == "1"):
                if callback:
                    callback(index+1 / len(dfInstrucao), f'move_pos(x:{float(dfInstrucao["x"][index])}, y:{float(dfInstrucao["y"][index])}, z:{float(dfInstrucao["z"][index])}')
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
    return 2, qrLido
```
&emsp;A função retorna o código de acerto 2 e o valor do QR Code lido.