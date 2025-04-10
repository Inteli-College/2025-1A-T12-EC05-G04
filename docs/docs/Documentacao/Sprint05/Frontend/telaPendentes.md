---
title: Tela de Pendentes
slug: /interface-final/pendentes
sidebar_position: 3
---

## Funcionalidade

&emsp;A tela de Montagens Pendentes tem como função exibir os pedidos de montagem que aguardam execução. A partir dela, o operador pode iniciar uma montagem, acionando o processo do robô.


<div align="center">
![Pendentes](../../../../../media/docsInterfaceFinal/pendentes/Pendentes.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Ao selecionar uma montagem para iniciar, ela será destacada em verde, indicando que está em andamento.

<div align="center">
![Montando](../../../../../media/docsInterfaceFinal/pendentes/Montando.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;As demais montagens serão exibidas em cinza e ficarão desativadas até que a montagem em andamento seja concluída.

<div align="center">
![Montando](../../../../../media/docsInterfaceFinal/pendentes/Desativado.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

## Integração

&emsp;A tela de Montagens Pendentes se conecta com o backend Flask por meio da rota `/montagem/pendentes`. Essa rota acessa o banco de dados PostgreSQL e retorna a lista de pedidos de montagem que ainda aguardam execução.

&emsp;As informações recebidas incluem o nome do paciente, número do HC, leito, data e identificador da montagem. Esses dados são utilizados para exibir dinamicamente os cards de montagem na interface.

&emsp;Toda a lógica de controle visual (como destacar a montagem ativa em verde e desabilitar as demais em cinza) é realizada no frontend, com base no estado interno da aplicação, sem necessidade de requisições adicionais ao backend durante a seleção.

&emsp;A atualização da interface ocorre automaticamente após o carregamento inicial, garantindo que o operador tenha uma visão atualizada das montagens disponíveis para execução.
