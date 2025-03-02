---
title: Wireframe
slug: /mapa-de-fluxo/wireframe
sidebar_position: 2
---

# Wireframe

&emsp;Um wireframe é uma representação inicial da interface gráfica de um website ou aplicativo. Desenvolvido no estágio inicial dos projetos, é feito de forma rápida e com pouco investimento de recursos, pois sua finalidade é entender se a ideia e o fluxo da interface está de acordo com as regras de negócios do projeto e com as metas da empresa parceira.

&emsp;O grupo Hígia, após a etapa de UX Research durante a sprint 1 do projeto em parceria com o *Hospital de Clínicas da Unicamp* e baseando-se nas personas do produto, criou um wireframe que contempla tanto o usuário que estará em contato próximo com o manipulador robótico e os pedidos de separação de medicamentos quanto o usuário que estará responsável por análises de métricas, gastos e relatórios de desempenho da farmácia hospitalar. 

&emsp;Considerando que a concepção deste wireframe é agnóstica a qualquer tecnologia, nenhuma linguagem ou biblioteca foi utilizada neste momento, apenas a ferramenta Figma. No entanto, após validação com o parceiro, o desenvolvimento das telas será realizado em HTML e CSS ou em React com Tailwind.

&emsp;O wireframe possui 6 telas, as quais possuem variantes para diferentes estados do robô ou do processo de montagem da fita de medicamentos. As telas principais desenvolvidas foram:

Tela | Utilidade ou funcionalidade
---- | ---------------------------
Tela de login | Tela de verificação e autenticação de usuários.
Tela Inicial | Tela de visualização do status do robô e da montagem das fitas médicas.
Tela de Montagens Pendentes | Tela para verificação e aprovação de fitas médicas para montagem.
Tela de Estoque | Tela de busca e verificação de remédios disponíveis no estoque da farmácia.
Tela de Relatórios | Tela de visualização de métricas e históricos.
Tela de Pedidos de Emergência | Tela para criação de pedidos de emergência manuais conforme necessidade do dia a dia da farmácia hospitalar.

Ao longo dessa seção de documentação, serão apresentadas todas as telas, mas a descrição será aprofundada nas telas primárias e que contêm maiores variantes, sendo elas a tela inicial e a tela de montagens pendentes. Vale ressaltar que esse wireframe foi criado durante a sprint 2 e está em sua primeira versão, portanto, permanece sujeito a ajustes e aprimoramentos nas semanas que sucedem o atual projeto. 

## Tela de login

&emsp;A tela de login foi desenvolvida para permitir que somente usuários já cadastrados no sistema possam acessar o software de montagem de fitas da farmácia hospitalar. Dessa forma, é maior a segurança contra possíveis ataques que possam causar transtornos e parar a montagem automática das fitas de medicamentos.

<div align="center">
![Visão geral da arquitetura](/../../media/wireframe/login.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

## Tela Inicial

&emsp;A tela inicial, acessada logo após o login, é a interface por onde é possível acompanhar os passos do robô a cada etapa de montagem das fitas de medicamentos e o seu status atual. Essa tela foi desenvolvida em 4 variantes, pensando em possibilidades de estado do manipulador robótico, sendo elas:

- Robô desligado;
- Robô ligado, mas sem fitas em andamento;
- Robô ligado e montando uma fita;
- Robô ou sistema com erro.

### Variante 1 - Robô desligado

&emsp;Na primeira variante, o robô se encontra desligado e é necessário que o usuário o ligue de forma física apertando no botão Power. Nessa variante, os verificadores de status da montagem das fitas ficam ocultos e a única informação de status é o botão on/off que indica se o robô está ligado ou não. Além disso, uma instrução sobre como ligar o manipulador robótico aparece na tela.

<div align="center">
![Visão geral da arquitetura](/../../media/wireframe/home2.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

### Variante 2 - Robô ligado, mas sem fitas em andamento

&emsp;Na variante 2, o robô encontra-se ligado, mas não possui nenhuma fita aprovada para a montagem, ficando em estado de espera. Na seção de status, é mostrado que o robô está ligado, mas que não está montando nenhuma fita médica. Também, está presente a instrução para aprovar fitas para a montagem pelo robô na seção de listas pendentes.

<div align="center">
![Visão geral da arquitetura](/../../media/wireframe/home1.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

### Variante 3 - Robô ligado e montando uma fita

&emsp;Na terceira variante, o robô encontra-se ligado e com o processo de montagem em andamento. É possível ver informações da fita que está sendo montada como o nome do paciente, HC, leito e prontuário. Além disso, é possível avaliar as etapas de montagem com a seção de rastreabilidade, a qual indica em qual estágio de montagem o robô está para cada medicamento da lista de separação que deve ir para a fita médica. Existem 3 momentos de controle, sendo eles o momento de bipagem do QRcode/código de barras, o momento em que o robô pega o medicamento do bin e o momento em que o manipulador robótico solta o medicamento no local indicado. 

<div align="center">
![Visão geral da arquitetura](/../../media/wireframe/home0.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

### Variante 4 - Robô ou sistema com erro

&emsp;Na última variante, o usuário será avisado quando erros ocorrem no sistema ou no  robô. Possíveis erros como a queda de conexão com a internet, a soltagem do remédio em local inapropriado ou a perda de conexão direta com o manipulador robótico serão avisados diretamente ao usuário, de forma a auxiliá-lo a resolver o erro.

<div align="center">
![Visão geral da arquitetura](/../../media/wireframe/home3.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

## Tela de Montagens Pendentes

&emsp;A tela de **Montagens Pendentes** será destinada à exibição de uma lista de separação de medicamentos previamente triada pelo farmacêutico. Sua elaboração considerou dois aspectos que a equipe identificou como relevantes neste primeiro momento. Primeiro, a inferência de que o sistema estará integrado ao sistema hospitalar atual via API, permitindo que as prescrições médicas triadas pelos farmacêuticos sejam enviadas automaticamente para essa tela. Segundo, reconheceu-se que não seria eficiente, ou mesmo viável, programar o robô para realizar as montagens de forma constantemente automática, pelo menos até esta sprint. 

&emsp;Diante disso, foi criada essa lista de montagens pendentes. A ideia é que a pessoa responsável aprove manualmente o início do processo de separação. Essa validação tem o objetivo de evitar erros de montagem, como confusões entre as bandejas e fitas de diferentes pacientes. Após a aprovação de uma fita, o robô iniciará a montagem, e as demais ficarão bloqueadas até que o processo atual seja concluído. Para isso, a tela de **Montagens Pendentes** foi desenvolvida em duas variantes, contemplando dois cenários possíveis: 

1. Quando nenhuma fita está em processo de montagem.
2. Quando uma fita já está sendo montada.

### Variante 1 - Nenhuma fita em montagem

&emsp;Nessa variante, mostra-se a lista de montagens que estão pendentes, contendo apenas as prescrições já triadas pelo farmacêutico responsável. Ela irá aparecer dessa maneira quando nenhuma separação estiver sendo realizada pelo robô. O técnico terá que acessar essa tela através do menu lateral e escolher a fita que o robô deverá montar, garantindo um fluxo organizado e evitando erros nessa processo.

### Variante 2 - Fita em montagem

&emsp;Essa variante será exibida quando o robô já estiver em processo de montagem de uma fita. Após a aprovação do técnico, o sistema deverá bloquear todas as outras fitas, evitando que haja confusões na separação dos medicamentos e que ocorra qualquer mistura entre os kits de diferentes pacientes. 

&emsp;É importante relembrar que esta é a primeira versão do wireframe e, após uma conversa com o parceiro, foram identificados pontos de melhorias que serão implementados nas próximas semanas. Um dos aprimoramentos será a inclusão da opção de reorganizar a lista na primeira variante, permitindo que a equipe farmacêutica customize a fila conforme sua necessidade e desejo. Além disso, na segunda variante, será adicionada a possibilidade de ativar o modo automático de montagem. O técnico responsável poderá optar por essa funcionalidade quando julgar que não há risco de confusão entre as bandejas. Para isso, a lista poderá ser personalizada por meio de um checkbox, indicando quais fitas o manipulador seguirá para montagem automática. Esses aprimoramentos são pensados para garantir que a equipe farmacêutica, apesar de contarem com a ajuda do robô, continuem mantendo o controle sobre o processo de montagem, tornando-o mais eficiente e alinhado às necessidades operacionais.

## Tela de Estoque

## Tela de Relatórios

## Tela de Pedidos de Emergência
