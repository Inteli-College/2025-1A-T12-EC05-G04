---
title: Integração da Interface com Robô
slug: integracao-interface-e-robo
sidebar_position: 1
---

---

## Observação de Desenvolvimento (Sprint 04)

&emsp;Durante a **Sprint 04**, conseguimos estabelecer com sucesso a comunicação do robô com o servidor, permitindo que ele enviasse logs em tempo real para o sistema. Esses logs foram recebidos pelo back-end e conseguimos também simular a retransmição com sucesso à interface de usuário via WebSocket.

&emsp;**No entanto, a integração completa entre as duas partes ainda não foi finalizada**. Apesar do fluxo de dados robô → servidor → front-end estar funcional ele não voi testada para fazer o fluxo completo automaticametne.

---

## Integração entre Interface de Usuário e Sistema de Automação

&emsp;Este documento descreve o funcionamento da integração entre a interface de usuário desenvolvida em **React** e o sistema de automação implementado em **Python** utilizando **WebSockets** via **Flask-SocketIO** e protocolo **HTTP**.


### Arquitetura Utilizada: MVC + WebSocket

&emsp;A aplicação segue a arquitetura **MVC (Model-View-Controller)**, que separa as responsabilidades em três camadas principais:

- **Model (Modelos de Dados):** Representam entidades como `Montagem`, `Paciente` e `ErroMontagem`, com persistência via SQLAlchemy.
- **View (Interface de Usuário):** Desenvolvida em React, exibe dados e permite interação com o usuário final.
- **Controller (Controladores):** Manipulam as regras de negócio e realizam a ponte entre Model e View, através de rotas REST e eventos WebSocket.

&emsp;Além do padrão MVC, a aplicação utiliza **WebSocket** para comunicação em tempo real, permitindo que eventos e logs sejam trocados entre servidor e cliente sem a necessidade de recarregamentos ou polling.

---

### Comunicação via WebSocket

&emsp;A integração WebSocket é realizada por meio de eventos definidos no back-end e escutados no front-end. Alguns dos principais eventos são:



#### Benefícios da Abordagem

- **Baixa latência:** Comunicação em tempo real com WebSocket.
- **Clareza arquitetural:** O uso de MVC facilita a divisão de responsabilidades.
- **Interface dinâmica:** A UI se atualiza automaticamente com base em eventos recebidos.

&emsp;Essa base sólida garante um caminho claro para finalizar a integração completa entre interface e automação nas próximas sprints.
