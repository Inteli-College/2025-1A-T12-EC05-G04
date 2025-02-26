---
title: Wireframe
slug: /mapa-de-fluxo/wireframe
sidebar_position: 2
---

# Wireframe

&emsp;Um wireframe é uma representação inicial da interface gráfica de um website ou aplicativo. Desenvolvido no estágio inicial dos projetos, é feito de forma rápida e com pouco investimento de recursos, pois sua finalidade é entender se a ideia e o fluxo da interface está de acordo com as regras de negócios do projeto e com as metas da empresa parceira.

&emsp;O grupo Hígia, após a etapa de UX Research durante a sprint 1 do projeto em parceria com o *Hospital de Clínicas da Unicamp* e baseando-se nas personas do produto, criou um wireframe que contempla tanto o usuário que estará em contato próximo com o braço robótico e os pedidos de separação de medicantos quanto o usuário que estará responsável por análises de métricas, gastos e relatórios de desempenho da farmácia hospitalar.

&emsp;O wireframe possui 6 telas, as quais possuem variantes para diferentes estados do robô ou do processo de montagem da fita de medicamentos. As telas principais desenvolvidas foram:

Tela | Utilidade ou funcionalidade
---- | ---------------------------
Tela de login | Tela de verificação e autenticação de usuários.
Tela Inicial | Tela de visualização do status do robô e da montagem das fitas médicas.
Tela de Montagens Pendentes | Tela para verificação e aprovação de fitas médicas para montagem.
Tela de Estoque | Tela de busca e verificação de remédios disponíveis no estoque da farmácia.
Tela de Relatórios | Tela de visualização de métricas e históricos.
Tela de Pedidos de Emergência | Tela para criação de pedidos de emergência manuais conforme necessidade do dia a dia da farmácia hospitalar.

Ao longo dessa seção de documentação, serão apresentadas todas as telas, mas a descrição será aprofundada nas telas primárias e que contêm maiores variantes, sendo elas a tela inicial e a tela de montagens pendentes.

## Tela de login

&emsp;A tela de login foi desenvolvida para permitir que somente usuários já cadastrados no sistema possam acessar o software de montagem de fitas da farmácia hospitalar. Dessa forma, é maior a segurança contra possíveis ataques que possam causar transtornos e parar a montagem automática das fitas de medicamentos.

<div align="center">
![Visão geral da arquitetura](/../../media/wireframe/login.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

## Tela Inicial

&emsp;A tela inicial, acessada logo após o login, é a interface por onde é possível acompanhar os passos do robô a cada etapa de montagem das fitas de medicamentos e o staus do robô. Essa tela foi desenvolvida em 4 variantes, pensando em possibilidades de estado do braço robótico, sendo elas:

- Robô desligado;
- Robô ligado, mas sem fitas em andamento;
- Robô ligado e montando uma fita;
- Robô ou sistema com erro.

### Variante 1 - Robô desligado

&emsp;Na primeira variante, o robô se encontra desligado e é necessário que o usuário o ligue de forma física apertando no botão Power. Nessa variante, os verificadores de status da montagem das fitas ficam ocultos e a única informação de status é o botão on/off que indica se o robô está ligado ou não. Além disso, uma instrução sobre como ligar o braço robótico aparece na tela.

<div align="center">
![Visão geral da arquitetura](/../../media/wireframe/home2.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

### Variante 2 - Robô ligado, mas sem fitas em andamento

<div align="center">
![Visão geral da arquitetura](/../../media/wireframe/home1.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

### Variante 3 - Robô ligado e montando uma fita

<div align="center">
![Visão geral da arquitetura](/../../media/wireframe/home0.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

### Variante 4 - Robô ou sistema com erro

<div align="center">
![Visão geral da arquitetura](/../../media/wireframe/home3.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

## Tela de Montagens Pendentes

## Tela de Estoque

## Tela de Relatórios

## Tela de Pedidos de Emergência
