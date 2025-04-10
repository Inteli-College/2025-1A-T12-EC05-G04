---
title: Tela de Emergência
slug: /interface-final/emergencia
sidebar_position: 6
---

## Funcionalidade

&emsp;A tela de emergência permite que o operador registre manualmente no banco de dados a retirada de um medicamento do estoque em situações em que o processo não passou pelo robô.

&emsp;Nessa tela, é possível informar o HC do paciente, seu nome, a data, o leito e selecionar o medicamento retirado. O registro de aprovação é automaticamente atribuído ao usuário que está realizando o pedido de emergência.

<div align="center">
![Emergência](../../../../../media/docsInterfaceFinal/emergencia/Emergencia.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Na area de seleção de remedios, quando selecionado, o operador consegue escolher a quantidade de remedios removidos do estoque a base da quantidade disponivel.

<div align="center">
![Remedio](../../../../../media/docsInterfaceFinal/emergencia/Remedio.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

## Integração

&emsp;Para viabilizar o funcionamento da tela de emergência, realizamos a integração com a API desenvolvida em Flask, que acessa um banco de dados PostgreSQL para fornecer e registrar as informações necessárias.

&emsp;No carregamento da tela, buscamos os remédios disponíveis por meio da rota `GET /lista/emergencia`, que consulta diretamente os dados do estoque no banco. Esses dados alimentam a interface para seleção e quantificação dos medicamentos a serem retirados.

&emsp;Ao digitar o HC do paciente, uma chamada à rota `GET /pacientes/validar/:hc` é feita automaticamente, permitindo que os dados do paciente (nome e leito) sejam preenchidos com base nas informações reais armazenadas no banco de dados.

&emsp;Por fim, ao confirmar o pedido, enviamos os dados do formulário para a rota `POST /lista/emergencia/forms`. Essa requisição registra no banco o histórico da retirada de medicamentos em situação de emergência, associando o pedido ao enfermeiro responsável.

&emsp;Toda a comunicação com o backend utiliza o padrão `application/json` e é realizada com a biblioteca Axios, garantindo que os dados sejam sempre atualizados diretamente do servidor, sem armazenamento local no navegador.
