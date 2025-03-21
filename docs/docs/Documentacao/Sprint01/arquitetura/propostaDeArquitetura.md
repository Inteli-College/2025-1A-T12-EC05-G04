---
title: Proposta de arquitetura do sistema
slug: /arquitetura-do-sistema/proposta-de-arquitetura
sidebar_position: 2
---

# Proposta de arquitetura do sistema

&emsp;Segundo a norma ISO/IEC/IEEE 42010, publicada em 2011 e atualizada em 2022, "a arquitetura de software são os conceitos fundamentais de um sistema, incluindo seus elementos, relacionamentos e os princípios para seu projeto e evolução". Essa definição exprime os principais aspectos da arquitetura de um software, ou seja, o projeto que contém os elementos e suas relações dentro do sistema. Dessa forma, a arquitetura embarca os princípios que regem a forma como todos os elementos do software se conectam, de forma detalhada e clara, pois é o esqueleto do sistema inteiro. Além disso, a arquitetura de um sistema abarca informações como os tipos de conexões e trocas de dados entre os componentes.

&emsp;Nesse primeiro momento, a equipe Hígia preocupou-se não em determinar aspectos e escolhas de tecnologias e/ou ferramentas, mas em desenvolver uma proposta de arquitetura agnóstica à tecnologia. Isso significa que não serão tratados os componentes como escolhas de dispositivos, linguagens de programação ou frameworks, mas como componentes-base que permitem a escolha das melhores tecnologias de acordo com o decorrer do projeto, desde que se adequem aos requisitos elicitados. Abaixo, encontra-se o diagrama de visão geral da arquitetura e seus respectivos cortes sobre cada uma das seções identificadas como separadas.

<div align="center">
![Visão geral da arquitetura](/../../media/propostaArquitetura/geral.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Para melhorar a visualização, foram realizados recortes de 3 seções da arquitetura. Além disso, foram elencados os tipos de conexão entre os elementos no quadro abaixo. É possível destacar conexões via cabo ou fio, ou seja, físicas; conexões via Rede, isso sendo Wi-Fi e WebSockets; conexões via requisições e endpoints de API; e conexões via queries no relacionamento com o banco de dados.

<div align="center">
![Conexões entre componentes](/../../media/propostaArquitetura/conexoes.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Dentro do recorte do módulo físico, foram destacados todos os elementos físicos do sistema, sendo eles: um robô (junto de periféricos acopláveis que permitam pegar e separar os remédios), um microcontrolador, um sensor infravermelho e um sensor leitor de QR code e códigos de barra. Nesse sentido, o microcontrolador será responsável por receber os dados e leituras dos dois sensores, que permitirão escanear a identificação das caixas de remédio e verificar se o robô foi capaz de pegar o remédio durante seus movimentos. O robô e seus periféricos acopláveis serão responsáveis pelos movimentos e mecanismos para a separação dos medicamentos. Além disso, as conexões são físicas por meio de fios e cabos entre os sensores e o microcontrolador e entre o robô e o servidor local. Entretanto, o microcontrolador poderá conectar-se ao servidor via rede Wi-Fi utilizando o protocolo WebSocket para comunicação bidirecional em tempo real.

&emsp;O protocolo WebSocket é uma tecnologia que possibilita comunicação em tempo real entre clientes e servidores através de um único canal de comunicação persistente. Diferente do HTTP, que segue o modelo de requisição-resposta, o WebSocket permite a troca contínua de mensagens entre os dispositivos conectados, sem a necessidade de reestabelecer conexões a cada transmissão. Essa característica é especialmente útil para aplicações que exigem baixa latência e transmissão instantânea de dados, como no caso da automação do robô. Dessa forma, o WebSocket foi escolhido por possibilitar uma comunicação eficiente e responsiva entre o microcontrolador e o servidor, garantindo a atualização em tempo real das leituras dos sensores e das ações do robô.

<div align="center">
![Módulo físico de separação](/../../media/propostaArquitetura/fisico.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;No recorte do back-end, foram destacados o servidor e o banco de dados. O servidor será responsável por receber as informações tanto do microcontrolador (como a base de WebSockets) quanto do robô e cruzá-las, permitindo que os próximos passos e movimentos do robô tenham a validação dos sensores conectados ao microcontrolador. Além disso, é necessário que o servidor receba as requisições do front-end e realize queries dentro do banco de dados a fim de responder às requisições da interface gráfica. O banco de dados será responsável por armazenar os dados de todo o sistema, mas principalmente os dados relacionados às movimentações do robô e status de montagem das fitas de remédios, dados dos medicamentos, dados dos pacientes e dados dos usuários do sistema.

<div align="center">
![Módulo físico de separação](/../../media/propostaArquitetura/backend.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Por fim, o front-end será a interface gráfica com a qual os usuários poderão interagir com o sistema. Ela se comunicará com o servidor via API e permitirá a visualização do status reportado ao servidor pelo microcontrolador, bem como o acesso diferenciado de acordo com o tipo de usuário.

<div align="center">
![Módulo físico de separação](/../../media/propostaArquitetura/frontend.jpg)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Na tabela abaixo, é possível encontrar uma representação mais concisa dos elementos da arquitetura.

| **Componente** | **Descrição** | **Papel na Arquitetura** |
|----------------|--------------|--------------------------|
| **Microcontrolador** | Microcontrolador que gerencia as conexões e o envio de dados dos sensores a base do protocolo WebSocket. | Responsável por se comunicar com os sensores, processar os dados e enviá-los ao protocolo. |
| **Robô** | Robô que pega, transporta e solta os medicamentos para montagem da fita médica. | Permite a automação do processo de separação e montagem das fitas de medicamentos. |
| **Sensor infravermelho** | Sensor que detecta a presença do remédio durante os movimentos do robô. | Permite saber a posição do medicamento para precisão do robô e detectar caso o robô deixe o medicamento cair ou não consiga pegá-lo. |
| **Sensor leitor de QRcode e código de barras** | Sensor para ler identificações dos remédios. | Valida informações dos medicamentos como tipo, dose e validade. |
| **WebSocket** | Protocolo WebSocket que recebe os dados enviados pelo microcontrolador. | Responsável pelo gerenciamento da transmissão dos dados entre o microcontrolador e o servidor. |
| **Servidor** | Servidor onde os dados e requisições tanto do módulo físico quanto do front-end são tratados | Serve como um ponto centralizado para o armazenamento dos dados coletados, além de permitir a pré-definição de restrições do sistema e tratamentos de possíveis erros. |
| **Front-end** | Interface gráfica para visualização do status de montagem das fitas de medicamentos e para validação de prescrições médicas. | Permite que os usuários acompanhem as informações coletadas e controlem o módulo físico, além de validarem prescrições médicas e enviarem as mesmas ao sistema. |
| **Banco de Dados** | Banco de dados para armazenar as informações processadas e estruturadas. | Armazena os dados do robô e dos sensores, dos usuários do sistema, dos medicamentos e dos pacientes do hospital. |

&emsp;Ao elaborar uma visão de arquitetura agnóstica à tecnologia, espera-se entender quais os requisitos e restrições antes que sejam escolhidos os dispositivos a serem utilizados. Dessa forma, é mais fácil de relacionar a visão arquitetural com a visão de negócios do projeto e permitir uma gama de opções de tecnologias para o desenvolvimento da solução, desde que possuam o necessário para serem admitidas na arquitetura definida.

## Como a arquitetura suporta os requisitos funcionais e não funcionais

&emsp;Além de ter detalhado e bem documentado o projeto da arquitetura, é necessário entender como essa mesma arquitetura dá o suporte necessário para que todos os requisitos - funcionais e não funcionais - sejam atendidos. Dessa forma, correlacionar cada componente com os requisitos que suporta dá á visão arquitetural a especificidade e clareza necessários ao projeto.

&emsp;Abaixo, encontra-se a tabela com a descrição dos requisitos funcionais suportados pela arquitetura.

| RF0# | Como a arquitetura o suporta |
| -------- |-------------------------- |
| RF01 | O controle das prescrições médicas aprovadas e da movimentação do robô pelo servidor permite que a separação de medicamentos seja automatizada de acordo com o necessário para cada prescrição.
| RF02 | A conexão via API permite a passagem de dados e informações entre o sistema a ser criado e o sistema hospitalar já existente.
| RF03 | A utilização de periféricos acopláveis ao robô e de um microcontrolador permite a inclusão de sensores no projeto.
| RF04 |  A utilização de um robô interligado ao servidor e ao banco de dados permite que os movimentos do robô sejam gerados em uma ordem pré-determinada por cada lista de separação atrelada a pacientes diferentes.
| RF05 | A utilização de sensores para leitura da embalagem permite saber qual remédio foi incluído em cada fita de medicamentos e quem verificou a fita antes da selagem.
| RF06 |  Uma das páginas do front-end será utilizada para exibição dos resultados de saída de remédios em cada fita de medicamentos nas últimas 24h, 3 dias e 7 dias.
| RF07 | O servidor fará a autenticação de usuário no front-end para diferenciar tarefas de farmacêuticos e técnicos de farmácia.
| RF08 | A cada fita de medicamentos separada e montada, os dados de movimentação do robô e dos sensores serão armazenados no banco de dados.
| RF09 | A cada fita de medicamentos separada e montada, o servidor fará a atualização do status no banco de dados do medicamento utilizado.
| RF10 | Caso erros sejam detectados pelos sensores de leitura e infravermelho, o usuário será alertado por meio do front-end sobre o erro ocorrido.

&emsp;Abaixo, encontra-se a tabela com a descrição dos requisitos não funcionais suportados pela arquitetura.

| RNF0# |  Como a arquitetura o suporta |
| -------- | -------------------------- |
| **RNF01** | A utilização do protocolo WebSocket permite o envio de dados mesmo em redes de baixa disponibilidade de internet. Além disso, a utilização de um microcontrolador permite guardar os dados da última fita montada e da próxima fita a ser montada caso quedas de internet ocorram.
| **RNF02** | A utilização de conexão física entre o robô e o servidor e de uma lista de separações pendentes permite que o sistema responda prontamente às solicitações de montagems de fitas de medicamento.
| **RNF03** | A utilização de sistema de autenticação e autorização para conexão com o sistema hospitalar permite que a integração com o sistema em desenvolvimento seja mais segura contra ataques e violações de dados.
| **RNF04** | A integração do módulo físico com o servidor e o banco de dados permite que cada fita montada seja registrada no sistema, além de log-in e log-outs de usuários.
| **RNF05** | O front-end permite que usuários se comuniquem rapidamente com o robô e possuirá funcionalidades claras para entender o que acontece em tempo real com a máquina e para parar o trabalho da mesma.
| **RNF06** | A construção do sistema se utilizando de protocolos de comunicação como WebSocket e APIs, além da separação de agentes dentro da arquitetura, permite que a adição de novos componentes ou réplicas do sistemas sejam feitas de forma facilitada para outros setores do hospital.
| **RNF07** | A utilização de sensores de leitura de código de barras e infravermelho permite saber para qual fita e paciente foi cada remédio.
| **RNF08** | A utilização de um protocolo de conexão com suporte à baixa disponibilidade de internet e de conexões físicas permite comunicações rápidas entre os componentes do sistema.
| **RNF09** | A solução pode ser utilizada em um computador único, conforme já utilizado na farmácia do HC da Unicamp.
| **RNF10** | O front-end utilizado possuirá convenções de linguagem conforme necessitado pelos usuários e convenções de design que permitam um fluxo de utilização intuitivo.

&emsp;Portanto. com o entendimento de como a arquitetura pode oferecer os componentes e aspectos necessários para que os requisitos sejam atendidos, o projeto de desenvolvimento da solução pode caminhar com maior solidez e as tecnologias utilizadas poderão ser escolhidas.