---
title: Tela de Estoque
slug: /interface-final/estoque
sidebar_position: 4
---

## Funcionalidade

&emsp;A função desta tela é listar os medicamentos em estoque de forma avançada, por meio de um sistema de pesquisa que permite ao operador consultar diretamente o banco de dados.

<div align="center">
![Estoque](../../../../../media/docsInterfaceFinal/estoque/Estoque.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Cada medicamento é exibido em uma caixa que apresenta seu nome, dose, validade, quantidade disponível e código de identificação.

<div align="center">
![Remedio](../../../../../media/docsInterfaceFinal/estoque/Remedio.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;A tela conta com uma área de pesquisa, na qual há um campo de texto para digitação e uma aba dropdown ao lado. Essa aba permite escolher se a busca será feita pelo nome do medicamento ou pelo seu código de registro.

<div align="center">
![Pesquisa](../../../../../media/docsInterfaceFinal/estoque/TipoDePesquisa.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Ao lado da área de pesquisa, há uma aba dropdown de filtragem. Com ela, o operador pode definir se os resultados devem ser ordenados por nome (ordem alfabética), código (ordem numérica), dose, validade ou quantidade de unidades.

<div align="center">
![Filtro](../../../../../media/docsInterfaceFinal/estoque/FiltroDeListagem.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Por fim, existe uma aba dropdown de ordenação, que define se os resultados serão exibidos em ordem crescente ou decrescente, com base no critério de filtragem selecionado anteriormente.

<div align="center">
![Ordem](../../../../../media/docsInterfaceFinal/estoque/OrdemDeListagem.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

## Integração

&emsp;Para possibilitar o funcionamento da tela de Estoque, integramos a aplicação com o backend utilizando uma requisição `GET` para a rota `/lotes/`, implementada em Flask. Essa rota acessa diretamente os dados armazenados em um banco de dados PostgreSQL e retorna as informações dos medicamentos em estoque.

&emsp;Os dados recebidos incluem o nome do remédio, dose, validade, quantidade disponível e código identificador, sendo utilizados para a renderização dinâmica da listagem na interface.

&emsp;Toda a lógica de busca, filtragem e ordenação é executada no frontend com base nos dados retornados inicialmente. Dessa forma, evitamos múltiplas requisições ao backend durante a navegação, garantindo fluidez e performance na exibição dos resultados.

&emsp;Essa comunicação garante que sempre trabalhemos com dados atualizados diretamente do banco, sem armazenamento local persistente no navegador.
