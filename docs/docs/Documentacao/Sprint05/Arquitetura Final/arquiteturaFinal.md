---
title: Arquitetura Final da Solução
slug: /arquitetura-final/arquitetura-da-solucao
sidebar_position: 2
---

# Considerações

&emsp;Durante as últimas sprints do projeto (4 e 5), a arquitetura sofreu mudanças mínimas e somente um novo componente foi adicionado. Dessa forma, esta seção pretende apresentar a arquitetura final do sistema de automação, seus componentes e como os mesmos se conectam entre si.

# Detalhamento da Arquitetura da Solução Final

&emsp;A arquitetura diz respeito a quais componentes fazem parte do sistema e como se conectam, além de quais protocolos de comunicação podem utilizar. Dentro do contexto do projeto de automação para a farmácia do Hospital de Clínicas da Unicamp, o objetivo foi criar um sistema robótico de montagem que permitisse a utilização fácil por farmacêuticos e técnicos de farmácia por meio de uma interface visual, além de verificações de segurança sobre os remédios que estavam na montagem. Abaixo, encontra-se o diagrama de arquitetura final desenvolvido pelo grupo Hígia:

<div align="center">
![Arquitetura Final](/../../media/arquitetura-final.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;O sistema de automação para criação de kits de remédio desenvolvido pelo grupo Hígia pode ser dividida em duas partes principais: a parte física, com o manipulador robótico e seus periféricos; e a aplicação web, com o servidor, o banco de dados e o front-end.

## Módulo físico de automação

&emsp;O módulo físico de automação concentra os componentes físicos do sistema que permitem a automação do processo de montagem dos kits de remédio, sendo eles: o manipulador robótico, os sensores de QRCode e infravermelho e os microcontroladores.

<div align="center">
![Arquitetura Final](/../../media/arquitetura-final-fisico.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Abaixo, encontram-se especificações sobre cada componente e sua utilidade no sistema:

| **Componente** | **Descrição** | **Papel na Arquitetura** |
|----------------|--------------|--------------------------|
| **Raspberry Pi 5** | Microcontrolador que gerencia as conexões e o envio de dados dos sensores ao servidor por meio do protocolo WebSocket. | Responsável por se comunicar com o leitor de QRcode e com o manipulador robótico, processar os dados e enviá-los ao protocolo. |
| **Raspberry Pi Pico** | Microcontrolador que recebe as informações do sensor infravermelho e as envia para o Raspberry Pi 5 | Responsável por se comunicar o sensor infravermelho via GPIO e enviar dados ao Raspberry Pi Pico via USB-Serial |
| **Dobot Magician Lite** | Manipulador robótico que pega, transporta e solta os medicamentos para montagem da fita médica. | Permite a automação do processo de separação e montagem das fitas de medicamentos. |
| **Sensor TCRT5000** | Sensor que detecta a presença do remédio durante os movimentos do robô por meio da luz infravermelha. | Permite saber a posição do medicamento para precisão do robô e detectar caso o robô deixe o medicamento cair ou não consiga pegá-lo. |
| **Sensor MH-ET Live** | Sensor para ler identificações dos remédios por meio de QRCode. | Valida informações dos medicamentos como tipo, dose e validade. |

&emsp;Dessa forma, o módulo físico foi desenvolvido e pensado para maior eficiência nos protocolos de comunicação e atendimento dos requisitos funcionais e não funcionais do projeto. Espera-se que o manipulador robótico consiga sempre realizar as montagens das fitas de medicamentos e que o microcontrolador principal consiga validar o rótulo do medicamento, além de verificar possíveis erros como soltar o remédio em uma coordenada incorreta.

## Aplicação Web

&emsp;A aplicação web do sistema permite a interação dos usuários com o manipulador robótico sem a necessidade de interação direta com o robô, além de permitir uma interface visual mais clara. Ademais, é possível conectar e coletar dados do manipulador e mostrá-los ao usuário de forma mais entendível. Nesse corte, estão presentes o servidor, o front-end e o banco de dados.

<div align="center">
![Arquitetura Final](/../../media/arquitetura-final-web.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Abaixo, encontram-se especificações sobre cada componente e sua utilidade no sistema:

| **Componente** | **Descrição** | **Papel na Arquitetura** |
|----------------|--------------|--------------------------|
| **Servidor Flask** | Servidor que conecta o módulo físico com o restante da aplicação web. | Permite o recebimento e validação de dados do módulo físico e o envio dos dados tanto ao front-end quanto ao banco de dados, além de gerenciar as rotas e a autenticação de usuários no front-end. Interage com o módulo físico via Web Socket. |
| **Front-end em React** | Interface visual do sistema | Permite interações mais fáceis ao usuário e o acompanhamento do status do sistema, além de permitir que o usuário interaja e inicie processos no módulo físico. Interage com o servidor via HTTP. |
| **Banco de dados PostgreSQL** | Banco de dados estruturado em tabelas que recebe os dados da aplicação e do módulo físico. | Permite o armazenamento e a consulta posterior dos dados sobre montagens, medicamentos e usuários. Interage com o servidor via Queries. |

&emsp;Dessa forma, a aplicação web foi projetada e desenvolvida ao pensar nas melhores formas de demonstrar o status atual do sistema robótico a usuários com pouca instrução sobre como manipular o robô. Assim, espera-se que o usuário tenha uma experiência fluida ao utilizar o sistema e isso parte de sua interação com a interface visual da aplicação web.