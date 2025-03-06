---
title: Sistema de Controle
slug: /sistema-de-automatizacao/sistema-de-controle-inicial
sidebar_position: 3
---

# Sistema de Controle para o Dobot

## Arquitetura do Sistema

O sistema é composto por três componentes principais e três módulos auxiliares:

### Componentes Principais:

1. **Criador de Movimentos** (`criadorMovimento.py`): Permite ao usuário criar sequências de ações para o robô, incluindo movimentos e operações de sucção, salvando-as em um arquivo de formato `.instrucao` (JSON).

2. **Leitor de Posições** (`lerMovimentoDobot.py`): Auxilia no processo de programação ao permitir a leitura e registro das coordenadas atuais do robô.

3. **Controlador Principal** (`movimentoDobotS2.py`): Executa os comandos armazenados em arquivos de instrução ou permite o controle manual do robô em tempo real.

### Módulos Auxiliares:

1. **Leitor de Instruções** (`leitorInstrucao.py`): Responsável por carregar os arquivos de instrução salvos no formato JSON.

2. **Parser de Comando** (`parserComando.py`): Interpreta os comandos inseridos pelo usuário no modo manual.

3. **Seletor de Comandos** (`seletorComandos.py`): Executa os comandos interpretados pelo parser de comando.

### Diagrama de Componentes

```
┌─────────────────────┐      ┌────────────────────┐
│ criadorMovimento.py │      │lerMovimentoDobot.py│
│                     │      │                    │
│ - Criação de        │      │ - Leitura de       │
│   sequências        │      │   posições         │
└────────┬────────────┘      └────────┬───────────┘
         │                            │
         │                            │
         ▼                            ▼
     ┌───────────────────────────────────┐
     │       Arquivos de Instrução       │
     │           (.instrucao)            │
     └─────────────────┬─────────────────┘
                       │
                       ▼
         ┌─────────────────────────────┐
         │     movimentoDobotS2.py     │
         │                             │
         │ - Modo de Instrução         │
         │ - Modo Manual               │
         └──┬──────────────┬───────────┘
            │              │
  ┌─────────▼─────┐  ┌─────▼─────────┐
  │leitorInstrucao│  │ parserComando │
  └───────────────┘  └───────┬───────┘
                             │
                    ┌────────▼────────┐
                    │ seletorComandos │
                    └────────┬────────┘
                             │
                       ┌─────▼─────┐
                       │   Dobot   │
                       └───────────┘
```

## Componentes do Sistema

### 1. Criador de Movimentos

O módulo `criadorMovimento.py` permite que o usuário crie uma sequência de ações para o robô Dobot. O usuário pode definir dois tipos de ações:

1. **Movimento (tipo 1)**: Move o robô para uma posição específica, capturando as coordenadas X, Y e Z atuais do robô.
2. **Pegar/Soltar (tipo 2)**: Controla a função de sucção do robô (pegar ou soltar objetos).

As sequências criadas são salvas em um arquivo no formato JSON com a extensão `.instrucao`, que pode ser posteriormente carregado pelo controlador principal.

#### Funcionamento

1. O script estabelece comunicação com o robô Dobot através da porta serial disponível.
2. O usuário insere sequencialmente os tipos de ação desejados.
3. Para ações do tipo 1 (movimento), o sistema captura automaticamente as coordenadas atuais do robô.
4. Para ações do tipo 2 (pegar/soltar), o usuário deve especificar o valor de pegada (1 para pegar, 0 para soltar).
5. Ao finalizar a sequência, o usuário fornece um nome para o arquivo onde as instruções serão salvas.

### 2. Leitor de Posições

O módulo `lerMovimentoDobot.py` é uma ferramenta auxiliar que permite ao usuário ler e registrar as coordenadas atuais do robô Dobot. Esta funcionalidade é útil durante o processo de programação, pois permite identificar coordenadas específicas que podem ser posteriormente utilizadas em sequências de movimentos.

#### Funcionamento

1. O script estabelece comunicação com o robô Dobot através da porta serial disponível.
2. O sistema continuamente lê e exibe as coordenadas atuais do robô (X, Y, Z).
3. As coordenadas são registradas em um arquivo de texto (`posicao.txt`).
4. O usuário pode encerrar a leitura a qualquer momento.

### 3. Controlador Principal

O módulo `movimentoDobotS2.py` é o componente central do sistema, responsável por executar os comandos armazenados em arquivos de instrução ou permitir o controle manual do robô. O controlador oferece dois modos de operação:

1. **Modo de Instrução**: Carrega e executa sequências de ações predefinidas a partir de arquivos `.instrucao`.
2. **Modo Manual**: Permite o controle direto do robô através de comandos inseridos pelo usuário.

#### Funcionamento

1. O script estabelece comunicação com o robô Dobot através da porta serial disponível.
2. O usuário seleciona o modo de operação desejado.
3. No modo de instrução, o sistema carrega o arquivo de instrução, interpreta cada ação e as executa sequencialmente.
4. No modo manual, o sistema recebe comandos do usuário, os processa através do parser de comandos e os executa.

## Módulos Auxiliares

### 1. Leitor de Instruções

O módulo `leitorInstrucao.py` é responsável por carregar os arquivos de instrução no formato JSON.

```python
import pandas as pnd

def lerJsonMovimento():
    nomeArquivo = input("Digite o nome do arquivo: \n")
    df = pnd.read_json(nomeArquivo + ".instrucao")
    return df
```

#### Funcionamento

1. O usuário fornece o nome do arquivo de instrução (sem a extensão).
2. O módulo carrega o arquivo JSON correspondente usando a biblioteca pandas.
3. Retorna um DataFrame contendo as instruções a serem executadas.

### 2. Parser de Comando

O módulo `parserComando.py` é responsável por interpretar os comandos inseridos pelo usuário no modo manual.

```python
def lerComando():
    comando = input('Digite o comando: ')
    arrayComando = comando.split('|')
    return arrayComando
```

#### Funcionamento

1. O usuário insere um comando ou uma sequência de comandos separados por `|`.
2. O módulo divide a entrada em comandos individuais.
3. Retorna um array contendo os comandos a serem executados.

### 3. Seletor de Comandos

O módulo `seletorComandos.py` é responsável por executar os comandos interpretados pelo parser de comando.

```python
def rodarComando(device, comando):
    #Pega a referência da posição atual do dobot
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
        case "moveTo":
            x = float(input("Insira a posição x \n"))
            y = float(input("Insira a posição y \n"))
            z = float(input("Insira a posição z \n"))
            device.move_to(x,y,z,r=0, wait=True)
```

#### Funcionamento

1. Recebe o dispositivo Dobot e o comando a ser executado.
2. Obtém a posição atual do robô.
3. Executa o comando correspondente:
   - `moveX`: Move o robô ao longo do eixo X por uma distância especificada.
   - `moveY`: Move o robô ao longo do eixo Y por uma distância especificada.
   - `moveZ`: Move o robô ao longo do eixo Z por uma distância especificada.
   - `suck`: Ativa a função de sucção (pegar).
   - `unsuck`: Desativa a função de sucção (soltar).
   - `moveTo`: Move o robô para coordenadas específicas (X, Y, Z).

## Demonstração do Sistema

<iframe src="https://drive.google.com/file/d/181uzLO_xXnsi6oZOncw6nzCQ3yxtpY4Z/preview" width="960" height="720" allow="autoplay"></iframe>


### Criação de Sequência de Movimentos

&emsp;No começo do vídeo, vemos nosso software de gravação das instruções para o Dobot. Com cada input, o usuário define se a próxima etapa da instrução é um movimento do braço ou uma alteração no estado do bico sugador. Para o caso do movimento (1), a posição do braço é registrada automaticamente, enquanto para a alteração da sucção (2) é necessário declarar o estado desejado (1 para sugando, 0 para soltando).

### Execução de Sequência em Modo de Instrução

&emsp;No modo de instrução do script principal, o arquivo gravado na etapa anterior é lido pelo software e realiza as ações na mesma sequência da gravação.

### Controle Manual do Robô

&emsp;Já no modo de controle manual, o usuário deve utilizar uma série de comandos já definidos no sistema para controlar o robô de forma mais precisa. Entre algumas das opções estão: Mover em um eixo certa quantidade de unidades, mover até uma posição [X,Y,Z] e alterar o estado de sucção do bico. Além disso, o usuário pode encadear comandos na mesma linha usando o sinal "|" separando os comandos, permitindo que uma sequência de comandos seja inserida manualmente de uma só vez.