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
- O servidor deve ter Python 3.12 e Git instalados. São incluídos em distros Linux na maioria das vezes.
- **Nota:** Outras versões do Python podem funcionar, mas não foram testadas. O ideal é utilizar a versão 3.12.

## Passo a passo

1. **Conecte o Raspberry Pi Pico a um computador.**

2. **Utilize o Thonny para instalar o firmware no Pi Pico.**  
   O arquivo está localizado em `src/firmware/picofirmware.py`.  
   Transfira esse arquivo para o Pi Pico e renomeie-o para `main.py`.

3. **No computador que atuará como servidor**, clone o repositório, crie um ambiente virtual e instale as dependências:

   ```bash
   cd {diretório onde deseja clonar o repositório}
   git clone {link de clonagem do repositório}
   cd {diretório do repositório}
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Acesse a pasta do servidor:**

   ```bash
   cd {diretório do repositório}/src/backend/server_v1
   ```

5. **Inicie o servidor:**

   ```bash
   python app.py
   ```

6. **Com o Dobot em mãos**, conecte um computador ao Dobot e instale o *Dobot Studio*.  
   O software pode ser baixado do site oficial da fabricante.
   Ou pelo seguinte link de Google Drive: 
   - https://drive.google.com/file/d/1-_yOVLWJvR4Jj-MiRBpl-TO9SttbEtLD/view?usp=sharing
   
   Após a instalação, conecte o Dobot via USB e inicie o software.

7. **No Dobot Studio:**

   - Clique em **"Connect"** e selecione a porta correta.
   - Clique em **"Home"** para posicionar o Dobot corretamente.

8. **No Raspberry Pi 5:**

   - Conecte os sensores e o Dobot pelas portas USB.
   - A ordem de conexão não interfere, mas você deve ajustar as portas no código conforme necessário.

   > Por padrão:
   > - Os **sensores** ocupam `ttyACM0` e `ttyUSB0`
   > - O **Dobot** ocupa `ttyACM1`  
   > O Pi Pico com o sensor de distância também usa uma porta `ttyACMx`.

9. **No Raspberry Pi 5**, clone o projeto, crie um ambiente virtual e instale as dependências:

   ```bash
   cd {diretório onde deseja clonar o repositório}
   git clone {link de clonagem do repositório}
   cd {diretório do repositório}
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

10. **Acesse a pasta do cliente:**

    ```bash
    cd {diretório do repositório}/src/firmware
    ```

11. **Com o servidor já em execução, inicie o cliente:**

    ```bash
    python3 main.py
    ```

## Como iniciar a Interface

1. **Certifique-se de que os servidores necessários estejam em execução.**  
   Depois disso, abra um novo terminal e navegue até o diretório do frontend:

   ```bash
   cd {diretório do repositório}/src/frontend
   ```

2. **Instale as dependências do projeto** (somente na primeira vez ou quando houver mudanças no `package.json`):

   ```bash
   npm install
   ```

3. **Inicie a interface em modo de desenvolvimento:**

   ```bash
   npm run dev
   ```

   Isso iniciará o servidor local da interface. Normalmente, ele ficará disponível em `http://localhost:5173` ou similar (o terminal mostrará o link).
