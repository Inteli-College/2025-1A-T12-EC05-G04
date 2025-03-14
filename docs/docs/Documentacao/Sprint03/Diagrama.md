---
title: Diagrama de Blocos
slug: /diagrama-de-blocos/modelagem
sidebar_position: 3
---

&emsp;Um diagrama de blocos é uma ferramenta utilizada para visualizar cada parte do sistema como um bloco e mostram como acontecem as interações entre eles, semelhante a um fluxograma. Esses diagramas oferecem uma visão geral de sistemas altamente conectados, facilitando o entendimento, a inclusão ou exclusão de componentes.

&emsp;Diferente da arquitetura do sistema, que foi realizada anteriormente e está disponível [aqui](../Sprint01/arquitetura/propostaDeArquitetura.md), este diagrama tem como foco detalhar os componentes periféricos que compõem o sistema e como estão sendo integrados. Abaixo, é possível visualizar o diagrama realizado pelo grupo Hígia, que demonstra como os elementos periféricos se comunicam com o sistema atual. Vale ressaltar que os blocos pontilhados ainda não foram implementados, mas serão nas próximas semanas.

<div align="center">
![Diagrama de Blocos](/../../media/diagramablocos.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Para o projeto com o HC Unicamp, onde o objetivo é automatizar a montagem e separação das fitas de medicamentos, o principal componente é o manipulador robótico *Dobot Magicitan Lite*, que irá tornar esse processo possível. No entanto, componentes adicionais são fundamentais para deixar o sistema completo e garantir que a tarefa do robô seja realizada de maneira eficiente e viável, como sensores QR Code e sensores infravermelhos. 

&emsp;Para garantir que a regra de negócio - apenas os medicamentos corretos sejam incluídos nos kits, minimizando erros de montagem - seja atendida, estão sendo implementados sensores capazes de realizar leituras de códigos e detecção infravermelha, conforme descrito no requisito funcional 3. 

<div align="center">
![Diagrama de Blocos](/../../media/diagramablocos2.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;O sensor QR Code utilizado é o *MH-ET Live*. Ele foi escolhido para ler os códigos dos medicamentos que o robô pega, para certificar de que foi o remédio correto foi selecionado e enviando os dados ao banco de dados. Dessa forma, o sistema atualiza o status atual da montagem - podendo ser visto na tela ‘HOME’ da interface (descrita mais detalhadamente [aqui](../Sprint02/UX/wireframe.md)) - além de gerenciar o estoque e os relatórios. O sensor estará fisicamente acoplado ao robô, mas não terá conexão direta com ele. A comunicação será com o microcomputador *Raspberry Pi 5* via cabo USB Serial. Após a leitura de um código de medicamento, os dados serão enviados ao Raspberry Pi, que então os encaminhará para a API *Flask* via *WebSocket*. A API repassará essas informações para o banco de dados, que, por sua vez, atualizará o front-end. Caso ocorra algum erro de leitura, como a identificação de um medicamento incorreto ou ausência de leitura, mensagens de erro serão enviadas ao microcomputador para tratamento adequado.

&emsp;O sensor infravermelho, embora ainda não tenha sido implementado, será um adicional relevante para o sistema, uma vez que permitirá a detecção de distâncias. Ele será utilizado para verificar se o robô conseguiu pegar o remédio, medindo a distância entre a posição do medicamento e o bico sugador do robô. Se essa distância for pequena, significa que a pegada foi bem-sucedida;  caso contrário, o robô não conseguiu pegar o medicamento. Isso contribuirá para aumentar a eficiência do processo e enviar dados ao microcontrolador para atualização do status da montagem, do estoque e dos relatórios. O modelo exato do sensor infravermelho ainda não foi definido, mas provavelmente será o *tcrt5000*. Esse sensor funciona a partir de um circuito elétrico, onde será conectado aos pinos GPIO do Raspberry Pi, utilizando uma entrada e uma alimentação 5V, permitindo que o sensor permaneça ligado continuamente. A comunicação entre o sensor e o microcomputador será via cabo.

&emsp;O principal componente de comunicação do sistema é o Raspberry Pi 5, que gerencia toda a lógica de instrução (movimentação) do manipulador robótico. No código ainda em desenvolvimento,  será incluída a lógica para leitura do QR Code e da distância medida pelo sensor infravermelho. Isso garantirá que as mensagens e os dados, tanto de sucesso quanto de erro, sejam devidamente enviados ao banco de dados e ao front-end. O microcomputador se comunica com o servidor via protocolo *WebSocket*, que, por sua vez, interage com o banco de dados e o front-end por meio do protocolo *HTTP*. O banco de dados está sendo desenvolvido no *PostgreSQL*, e a aplicação web, que ainda não foi iniciada, será construída utilizando o framework *React*.

&emsp;A elaboração do diagrama de blocos foi essencial para a equipe ter uma visão ampla e ampla do sistema, compreendendo com mais profundidade e clareza como os componentes estão se comunicando e interagindo entre si. Além disso, tem sido uma ferramenta valiosa para facilitar a adição de novos componentes e realizar ajustes nos existentes, conforme necessário.
