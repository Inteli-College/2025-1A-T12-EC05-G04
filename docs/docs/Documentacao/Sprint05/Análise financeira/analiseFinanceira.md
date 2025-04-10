---
title: Análise financeira do projeto
slug: s5/analise-financeira/analise-financeira
sidebar_position: 1
---

# Análise financeira do projeto

&emsp;Nesta seção, será apresentada a análise financeira do projeto. Realizar essa avaliação é indispensável para determinar a viabilidade econômica e estimar o retorno sobre investimento (ROI), reduzindo os riscos de prejuízos ou gastos desnecessários. Isso envolve examinar diversos aspectos que impactam direta ou indiretamente a implementação do projeto em um cenário real, como preços dos equipamentos, custos diretos e indiretos, despesas operacionais e impostos .

&emsp;Efetivamente, o projeto é voltado para um contexto educacional e o foco é automatizar a montagem de fitas de medicamentos por meio do uso de robôs. Portanto, foram utilizados componentes como Raspberry Pi Pico, sensores simples  e o robô Dobot. Para a transição ao contexto industrial, o ideal é migrar para uma solução mais robusta, utilizando componentes mais adequados e eficientes como CLPs, sensores industriais e manipuladores mecânicos de maior precisão, preferível para ambientes hospitalares.

## Protótipo educacional

&emsp;O protótipo do projeto foi desenvolvido ao longo de 10 semanas e o foco dele foi para o contexto educacional. A seguir estão listados todos os recursos usados para criar o protótipo, com valores reais ou estimados.

Item | Tipo | Especificação | Quantidade | Custo Unitário (R$) | Custo Total (R$)
--- | --- | --- | --- | --- | ---
Microcontrolador | Material | Raspberry Pi Pico | 1 | 40,00 | 40,00
Microcomputador | Material | Raspberry Pi 5 8GB | 1 | 800,00 | 800,00
Sensor Infravermelho | Material | TCRT5000 | 1 | 2,00 | 2,00
Sensor QRcode | Material | MH-ET Live | 1 | 260,00 | 260,00
Manipulador robótico | Material | Dobot Magician Lite | 1 | 6.030,00 | 6.030,00
Caixa de proteção | Material | Caixa feita em impressão 3D para proteção do Raspberry Pi 5 | 1 | 50,00 | 50,00
Fios | Material | Fios jumper fêmea-fêmea | 5 | 1,00 | 5,00
VSCode | Ferramenta | IDE para desenvolvimento de código | - | - | 0,00
Dbeaver | Ferramenta | Software para gestão e interação com SGBDs | - | - | 0,00
Render | Ferramenta | Site para deploy temporário do banco de dados | - | - | 0,00

&emsp;Para esse protótipo foram considerados somente gastos em recursos como equipamentos e mão de obra. No entanto, ele não reflete as exigências e condições reais de um ambiente industrial. Para viabilizar a escalabilidade e a implementação nesse contexto, é necessário o desenvolvimento de um novo protótipo industrial, com componentes robustos e mais adequados.

## Contexto industrial

&emsp;Como mencionado anteriormente, ao transicionar o projeto para o contexto industrial, algumas modificações são necessárias para viabilizar a implementação e escalabilidade. Será preciso adotar uma solução mais robusta, que inclua CLPs (Controladores Lógicos Programáveis), sensores industriais mais precisos e manipuladores robóticos industriais. Esses componentes garantem mais confiabilidade, segurança e desempenho adequados. 

&emsp;Para uma análise financeira mais completa, aspectos como despesas operacionais, custos diretos e indiretos, tributos e os conceitos de CAPEX e OPEX, são fundamentais para determinar se o projeto é viável economicamente ou não.

### Custos diretos e indiretos:

&emsp;Os custos são todos os gastos relacionados diretamente à produção ou entrega do produto principal que é oferecido. Os custos diretos são gastos que, como o nome sugere, estão associados diretamente ao produto e que podem ser mensuráveis sem dificuldades. Já os custos indiretos são aqueles que estão relacionados à atividade principal do projeto, mas que não podem ser diretamente atribuídos a um produto ou serviço específico. Os custos associados ao projeto são os seguintes:

- Manipulador robótico industrial
- CLP
- Sensores industriais
- Softwares e licenças
- Cabos, conectores e acessórios
- Manutenção
- Treinamento da equipe operacional 
- Energia elétrica da sala de produção
- Salário dos funcionários
- Depreciação dos equipamentos

### Despesas:

&emsp;As despesas são os gastos que não estão atrelados à linha de produção, mas são necessários para manter a operação funcionando. As despesas que associadas ao projeto são:

- luguel de um espaço específico para a produção
- Contas de água
- Contas de luz
- Internet
- Seguros

### Tributos e Impostos:

&emsp;Aqui serão listados todos os valores obrigatórios que a empresa paga ao governo. A sua avaliação é importante pois eles afetam o custo real dos equipamentos e serviços, impactam na escolha de fornecedores e afetam diretamente a precificação e o ROI. Os tributos associados ao projeto são:

- IPI (Imposto sobre Produtos Industrializados): aparece na compra de equipamentos como os manipuladores robóticos, sensores, CLPs, entre outros. 
- ICMS (Imposto sobre Circulação de Mercadorias e Serviços): é um imposto estadual que aparece sempre que há venda, transporte ou circulação de mercadorias. 
- PIS/COFINS (Programas de Integração Social / Contribuição para o Financiamento da Seguridade Social):
- II (Imposto de Importação): aparece ao importar produtos, como robôs. 
- ISS (Imposto sobre Serviços): aparece na contratação de prestação de serviços, como os de manutenção e treinamento. 

### CAPEX e OPEX:

&emsp;Após a identificação dos custos, despesas e tributos envolvidos no projeto, torna-se necessário colocá-los sob uma perspectiva financeira de longo e curto prazo. Para isso, pode-se aplicar a divisão entre CAPEX (Capital Expenditure) e OPEX (Operational Expenditure), conceitos importantes para a gestão de investimentos.

#### CAPEX: Investimentos em Bens de Capitais
	
&emsp;Esses gastos existem para manter ou expandir o escopo das operações, indicando o quanto do capital está sendo comprometido com a aquisição de bens materiais, como máquinas e hardwares. No contexto desse projeto, são considerados CAPEX:

- Manipulador robótico
- CLPs
- Sensores industriais
- Cabos, conectores e acessórios
- Custos de instalação e integração dos sistemas
- Tributos sobre aquisição de equipamentos
- Treinamento vinculado à implantação


#### OPEX:  Despesas Operacionais 

&emsp;Esses são os gastos associados às despesas em atividades rotineiras, como despesas tributárias, salários e pagamentos, ou seja, são os investimentos de curto prazo em bens operacionais. Para o projeto, fazem parte do OPEX:

- Energia elétrica consumida 
- Manutenção de equipamentos
- Salários
- Tributos sobre serviços e operações
- Softwares e licenças























