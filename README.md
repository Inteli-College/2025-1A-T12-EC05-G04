# Sistema de Controle para Robô Manipulador Dobot

Este repositório contém o sistema de controle para o robô manipulador Dobot, desenvolvido como parte do projeto de automação. O sistema permite o controle programático do robô através de uma interface de linha de comando (CLI), possibilitando a movimentação do robô para um conjunto pré-definido de pontos e a execução de operações de sucção.

## Estrutura do Projeto

```
├── src/
│   ├── criadorMovimento.py       # Criação de sequências de ações
│   ├── lerMovimentoDobot.py      # Leitura de posições do robô
│   ├── movimentoDobotS2.py       # Controlador principal
│   └── modulosCodigo/            # Módulos auxiliares
│       ├── leitorInstrucao.py    # Leitor de arquivos de instrução
│       ├── parserComando.py      # Parser de comandos manuais
│       └── seletorComandos.py    # Executor de comandos
└── README.md                     # Este arquivo
```

## Requisitos

- Python 3.10+
- pydobot
- pandas
- pyserial

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/dobot-control-system.git
   cd dobot-control-system
   ```

2. Instale as dependências:
   ```bash
   pip install pydobot pandas pyserial
   ```

3. Conecte o robô Dobot ao computador via USB.

## Uso

### 1. Criador de Movimento

Este módulo permite criar sequências de ações para o Dobot e salvá-las em um arquivo `.instrucao`.

```bash
cd src
python criadorMovimento.py
```

Siga as instruções na tela para criar uma sequência de ações:
- Digite "1" para definir um movimento (as coordenadas atuais do robô serão capturadas)
- Digite "2" para definir uma ação de pegar/soltar (em seguida, digite "1" para pegar ou "0" para soltar)
- Ao final, informe um nome para o arquivo de instrução

### 2. Leitor de Posições

Este módulo permite ler e registrar as coordenadas atuais do robô Dobot.

```bash
cd src
python lerMovimentoDobot.py
```

As coordenadas são exibidas na tela e salvas no arquivo `posicao.txt`. Digite "s" para continuar lendo ou "n" para encerrar.

### 3. Controlador Principal

Este módulo é o componente central do sistema, responsável por executar os comandos armazenados em arquivos de instrução ou permitir o controle manual do robô.

```bash
cd src
python movimentoDobotS2.py
```

Escolha o modo de operação:
- **Modo de Instrução (1)**: Carrega e executa sequências de ações predefinidas
- **Modo Manual (2)**: Permite o controle direto do robô através de comandos

#### Comandos do Modo Manual

No modo manual, você pode utilizar os seguintes comandos:
- `moveX`: Move o robô ao longo do eixo X por uma distância especificada
- `moveY`: Move o robô ao longo do eixo Y por uma distância especificada
- `moveZ`: Move o robô ao longo do eixo Z por uma distância especificada
- `moveTo`: Move o robô para coordenadas específicas (X, Y, Z)
- `suck`: Ativa a função de sucção (pegar)
- `unsuck`: Desativa a função de sucção (soltar)
- `sair`: Sai do modo manual

Você pode encadear comandos utilizando o caractere `|`. Por exemplo:
```
moveX|suck|moveZ|moveTo|unsuck
```

## Solução de Problemas

### Permissões de Porta Serial (Linux)

Se você estiver enfrentando problemas de permissão ao acessar a porta serial no Linux, execute o seguinte comando:

```bash
sudo chmod 666 /dev/ttyACM0
```

Este comando já está incluído nos scripts, mas pode ser necessário executá-lo manualmente caso não tenha permissões suficientes.

### Erro no Match/Case

Se você estiver recebendo erros relacionados ao uso de `match/case`, certifique-se de que está usando Python 3.10 ou superior, pois esta funcionalidade foi introduzida nesta versão.