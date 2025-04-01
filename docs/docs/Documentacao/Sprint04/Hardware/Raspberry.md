---
title: Raspberry
slug: raspberry
sidebar_position: 1
---
# Raspberry - o controlador do hardware

## Visão geral

&emsp;O Raspberry Pi é o microcomputador que serve como ponto central de controle no projeto. Ele é responsável por gerenciar a comunicação com o servidor via WebSocket, receber instruções do servidor e repassá-las para o braço robótico Dobot, capturar dados dos sensores e realizar decições com base nesses dados (como interromper o processo).
&emsp;Esse ecossistema permite que o Raspberry Pi atue como um “hub” inteligente para o controle do robô, conectando hardware (Dobot e sensores) com software (servidor e, futuramente, interface de usuário).

## main.py

&emsp; Esse script é a "mãe" da nossa implementação no Raspberry Pi, sendo responsável por chamar todos os outros scripts e gerenciar a comunicação com o servidor por websocket, utilizando a biblioteca socketio para realizar a comunicação.

### Recebimento de instruções

&emsp; Para recebermos as instruções de montagem do servidor, o sistema utiliza ouve o evento 'instrucao', que contém um json com os comandos do Dobot e o id da montagem atual. Com base nesses dados, o sistema chama a função 'rodarInstrucao(data['instrucao'], callback)': data['instrucao'] equivale ao json da instrução e callback é uma função que retorna periodicamente o estado atual de montagem para o servidor. Olharemos para essa função mais tarde.

```python
@sio.on("instrucao")
def listen_instrucao(data):
    print(f"Mensagem recebida: {data}")
    try:
        #Pega instrução e roda
        resultado, qr = rodarInstrucao(data['instrucao'], callback=send_callback)
        #Envio:
        send_message('qr_code', {'result': resultado, 'qr': qr, 'id_montagem': data['id_montagem']})
    except Exception as e:
        print(f"Erro ao executar instrução: {e}")
        send_message('error_status', {'message': 'Erro ao executar instrução', 'error': str(e)})
```

&emsp; Nota-se também o tratamento de erros nesse segmento. Na página de controle do robô, iremos ver casos de erros diferentes para certas situações, como algum impedimento que resulte no Dobot não chegando na posição necessária. Nesses casos, o Raspberry relata a mensagem de erro no próprio terminal, e retorna esse erro para o servidor de modo a ser tratado na lógica de negócios do mesmo e da interface.

### Envio de informações

&emsp;O envio de informações do Raspberry para o servidor é feito através da função 'send_message(event, data)', event sendo o evento WS que o servidor ouve, e data sendo o json com as informações a serem enviadas. Atualmente temos três tipos de mensagem sendo enviadas para o servidor: "error_status", que são códigos de erro durante o processo; "qr_code", que são os códigos de QR lidos durante o processo e retornados para o servidor caso tudo dê certo; e "current_status", que retorna os callbacks durante o processo de montagem.

```python
def send_message(event, data):
    """Envia mensagens WebSocket, comporta dois parâmetros, event e message."""
    sio.emit(event, data)
```

### Callbacks

&emsp;Ao passar a função send_callback(percentage, acao) para a função rodarInstrucao, o sistema consegue retornar o estado de completude atual da montagem para o servidor, resultando em uma atualização mais efetiva da interface. Essa abordagem também impede erros que aconteceriam tentando rodar a função diretamente no script do robô, como importação circular e problemas de comunicação/conexão

```python
def send_callback(percentage, acao):
    send_message('current_status', {'percentage': percentage, 'acao': acao})
```

## firmwarePi.py

### VerificarPorta()

&emsp;Essa função é uma ferramenta responsável por verificar todas as portas USB conectadas ao Raspberry Pi, entre elas o Dobot e ambos os sensores. Com isso, podemos verificar quais portas são necessárias para fazer cada sistema funcionar, e pode-se alterá-las no código. É imprático automaticamente indexar essas portas para o código, pois o sistema pode ser utilizado em diferentes ambientes e com diferentes configurações de hardware. No nosso caso, o Dobot está em ttyACM1, o leitor de QR Code em ttyUSB0 e o infravermelho em ttyACM0. 
&emsp;Obs: Foi notado que a ordem que os dispositivos são conectados afeta qual porta cada um se localiza: Em nossos testes, ttyUSB0 sempre era o leitor de QR Code, mas entre o Dobot e o sensor infravermelho, o ttyACM0 era dado ao primeiro conectado, e ttyACM1 ao segundo. Porém, se removermos o dispositivo em ttyACM0 e reconectarmos, as portas continuam a mesma do que antes.

```python
def verificarPorta():
    available_ports = list_ports.comports()
    print(f'available ports: {[x.device for x in available_ports]}')
```

### rodarInstrucao(instrucao, port='/dev/ttyACM1', callback=None)

&emsp;A função rodarInstrução é responsável por receber a instrução do servidor e chamar o código de controle do Dobot, além de iniciar a comunicação serial com o braço robótico. Ele recebe a string de instrução, a porta serial do Dobot (padrão ttyACM1) e o callback para retornar o estado atual da montagem para o servidor. Para os testes de uso, a função também aciona o verificarPorta(), que listando todas as portas USB conectadas ao Raspberry Pi.

```python
def rodarInstrucao(instrucao, port='/dev/ttyACM1', callback=None):
    verificarPorta()
    d = pydobot.Dobot(port)
    result, qr = execInstrucao(d, instrucao)
    return result, qr
```

&emsp;Por fim, a função retorna o resultado da execução em forma do código de sucesso e o valor do QR Code lido

### execComando(comando, port='/dev/ttyACM1')

&emsp;Um vestígio da antiga versão do controlador manual do Dobot da sprint 2, esta função reage aos mesmos inputs manuais que eram utilizados na versão antiga. Atualmente, essa função não é utilizada, mas poderia ser implementada em etapas futuras.

```python
def execComando(comando, port='/dev/ttyACM1'):
    d = pydobot.Dobot(port)
    #Antigamente havia uma lógica de seleção e leitura de linhas de comando aqui. Com a mudança de CLI para interface, não será mais necessário essa leitura
    #Pensando nisso, parece meio redundante utilizar essa função, que será chamada no ws_client, para chamar outra função ao invés de invocar diretamente a função rodarComando
    #Apesar disso, acredito eu que isto deixa o código mais limpo no ws_client, focando apenas na comunicação com o servidor, enquanto este cuida das interações com o físico
    rodarComando(d, comando)
```
