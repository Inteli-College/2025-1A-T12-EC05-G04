---
title: Como iniciar o sistema
slug: como-iniciar
sidebar_position: 1
---
# Como iniciar o sistema
## Pré-requisitos
- Ter em mãos os materiais requeridos, listados na documentação.
- Ter o Raspberry Pi já funcional, com um sistema operacional instalado.
- Ter o código fonte do projeto, que pode ser baixado do repositório oficial.
- O servidor deve ter Python 3.12 e git instalados. São incluídos em distros Linux na maioria das vezes.
- Nota: Outras versões do Python podem funcionar, mas não foram testadas. O ideal é utilizar a versão 3.12.

## Passo a passo

- Conecte o Raspberry Pi Pico em um computador
- Utilizando o Thonny, instale o firmware do projeto. O arquivo está em src/firmware/picofirmware.py. Utilizando o Thonny, transfira o arquivo para o Pi Pico e renomeie-o para main.py.
- No computador do servidor, clone o código do projeto, crie um ambiente virtual e instale as dependências.
```bash
cd {diretório onde deseja clonar o repositório}
git clone {link de clonagem do repositório}
cd {diretório do repositório}
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Acesse a pasta do servidor do repositório:
```bash
cd {diretório do repositório}/src/backend/server_v1
```
- Inicie o servidor:
```bash
python app.py
```
- Com o Dobot em mãos, conecte um computador ao Dobot e instale o Dobot Studio. O software pode ser baixado do site oficial da fabricante. Após a instalação, conecte o Dobot ao computador e inicie o software. O Dobot deve estar conectado ao computador via USB.
- No Dobot Studio, clique em "Connect" e selecione a porta correta. O Dobot deve ser reconhecido pelo software.
- Clique em "Home", para garantir que o Dobot esteja na posição inicial. Isso é importante para garantir que o Dobot saiba onde está e possa se movimentar corretamente.
- No Raspberry Pi 5, conecte os sensores e o Dobot pelos cabos USB. Qualquer ordem de conexão deve funcionar, mas é necessário alterar as portas no código dependendo de como você conectou os dispositivos. O código atualmente está configurado para as conexões primeiro dos sensores, e depois do Dobot. Os sensores são intercambiáveis em ordem, já que ocupam nomes diferentes no sistema (ttyACMx e ttyUSBx, onde x é o index de conexão daquele dispositivo), enquanto o Dobot utiliza o ttyACMx junto do Pi Pico com o sensor de distância. Dessa forma, os sensores ocupam os espaços ttyACM0 e ttyUSB0, enquanto o Dobot ocupa o ttyACM1.
- No Raspberry Pi 5, clone o código do projeto, crie um ambiente virtual e instale as dependências.
```bash
cd {diretório onde deseja clonar o repositório}
git clone {link de clonagem do repositório}
cd {diretório do repositório}
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Acesse a pasta de cliente do repositório:
```bash
cd {diretório do repositório}/src/firmware```
- Com o servidor já ligado nos passos anteriores, inicie o cliente:
```bash
python3 main.py
```
