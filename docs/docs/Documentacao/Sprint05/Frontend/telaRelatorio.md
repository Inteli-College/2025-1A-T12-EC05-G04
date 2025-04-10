---
title: Tela de Relatorio (Não Integrada)
slug: /interface-final/relatorio
sidebar_position: 5
---

## Funcionalidade

&emsp;A tela de Relatório permite ao operador visualizar graficamente os dados de logs do robô, incluindo informações sobre horas trabalhadas, taxa de erro, tempo médio de montagem e tempo médio de resposta. Além disso, estão disponíveis gráficos relacionados ao uso das fitas ao longo do tempo e à quantidade de fitas movimentadas entre as alas do hospital.


<div align="center">
![Relatorio](../../../../../media/docsInterfaceFinal/relatorio/Relatorio.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Essas informações podem ser filtradas conforme a necessidade. Na área superior da tela, é possível selecionar os diferentes turnos para refinar os dados exibidos.

<div align="center">
![Turnos](../../../../../media/docsInterfaceFinal/relatorio/Turnos.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Também é possível restringir a visualização para um intervalo específico entre duas datas.

<div align="center">
![Data1](../../../../../media/docsInterfaceFinal/relatorio/Data1.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

<div align="center">
![Data2](../../../../../media/docsInterfaceFinal/relatorio/Data2.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

<br />

&emsp;O último filtro disponível permite especificar a ala do hospital que se deseja analisar.

<div align="center">
![Alas](../../../../../media/docsInterfaceFinal/relatorio/Alas.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Para remover todos os filtros aplicados, basta utilizar o botão localizado ao final da caixa de filtros.

<div align="center">
![LimparFiltros](../../../../../media/docsInterfaceFinal/relatorio/LimparFiltros.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

## Integração (Próximos Passos)

&emsp;Atualmente, a tela de Relatório funciona com dados estáticos simulados diretamente no frontend. Para finalizar sua implementação, precisamos realizar a integração com o backend Flask, que deve consultar os dados reais do banco PostgreSQL com base nos filtros selecionados pelo usuário.

&emsp;A integração pode ser feita da seguinte forma:

1. **Criação de Endpoint no Backend**:  
   Desenvolver uma rota `GET /relatorios` no backend Flask que aceite parâmetros de filtro como:
   - `turno`
   - `dataInicio`
   - `dataFim`
   - `ala`

   Essa rota deve consultar o banco e retornar um JSON contendo:
   - Total de horas trabalhadas
   - Taxa de erros
   - Tempo médio de montagem
   - Tempo médio de resposta
   - Dados para os gráficos de linha (fitas x tempo)
   - Dados para o gráfico de pizza (fitas por ala)

2. **Atualização da Tela (Frontend)**:  
   Adicionar um `useEffect` no componente `Relatorios` para escutar os filtros enviados pelo `SearchBarRelatorios` e fazer uma requisição `GET` para o endpoint criado no backend, passando os filtros como `query parameters`.

3. **Distribuição dos Dados**:
   - Os dados retornados devem ser repassados como props para os componentes `MetricasRobo` e `Graficos`, substituindo os dados simulados atualmente.
   - É necessário adaptar esses componentes para aceitar dados via props.

4. **Tratamento de Erros e Carregamento**:
   - Implementar mensagens de erro e estados de carregamento para melhorar a experiência do usuário durante a requisição dos dados.


Essa integração permitirá que a tela de relatório seja alimentada com dados reais e atualizados, refinados de acordo com os filtros aplicados pelo operador.
