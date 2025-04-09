---
title: Verificação de Requisitos
slug: /arquitetura-final/requisitos
sidebar_position: 2
---

## Verificação dos Requisitos

No início do projeto, definimos requisitos funcionais e não funcionais com o objetivo de descrever as funcionalidades e comportamentos esperados do sistema. Agora, na entrega do MVP, realizamos uma verificação para identificar se cada requisito foi atendido totalmente, parcialmente ou não atendido. Junto a essa verificação, também detalhamos os próximos passos necessários para que os requisitos pendentes possam ser plenamente implementados.

Para simplificar a visualização da verificação, siga a seguinte tabela de referencia:

<div align="center">

|  |  |
| --- | --- |
| Requisito Atendido | ✅ |
| Requisito Parcialmente Atendido | ⚠ |
| Requisito Não Atendido | ⛔ |


</div>

## Requisitos Funcionais

<div align="center">

| Requisito | | Descrição | Regra de Negócio |
| --- | --- | --- | --- |
| **RF01** | ✅ | O sistema deve permitir a automação da separação de medicamentos com base nas prescrições eletrônicas. | O sistema deve garantir a seleção correta dos medicamentos prescritos, reduzindo erros de separação. |
| **RF02** | ⚠ | O sistema deve integrar-se ao sistema hospitalar para obter prescrições digitais e atualizar o estoque automaticamente. | A comunicação com o sistema hospitalar deve ser segura e confiável, garantindo integridade dos dados. |
| **RF03** | ✅ | O sistema deve possuir sensores para leitura de código de barras e detecção infravermelha. | A validação deve garantir que apenas medicamentos corretos sejam incluídos nos kits, minimizando erros de montagem. |
| **RF04** | ✅ | O sistema deve organizar os medicamentos na sequência necessária para cada paciente. | A organização da "Fita de Medicamentos" deve seguir as diretrizes médicas e farmacêuticas. |
| **RF05** | ✅ | O sistema deve permitir o rastreamento detalhado dos medicamentos. | Todas as movimentações devem ser registradas, garantindo segurança e conformidade com normas hospitalares. |
| **RF06** | ✅ | O sistema deve gerar relatórios detalhados de atividades e desempenho. | Os relatórios devem incluir tempo de montagem, taxa de erros e estatísticas de uso, podendo ser exportados para análise. |
| **RF07** | ⛔ | O sistema deve permitir diferentes níveis de acesso para usuários. | Apenas administradores podem realizar alterações críticas e ajustes na configuração do sistema. |
| **RF08** | ✅ | O sistema deve registrar um histórico detalhado de operações. | Todas as atividades, ajustes manuais e erros detectados devem ser registrados para auditoria e segurança. |
| **RF09** | ✅ | O sistema deve atualizar automaticamente o estoque da farmácia conforme os medicamentos são separados. | O estoque hospitalar deve ser atualizado em tempo real para evitar falhas na reposição de medicamentos. |
| **RF10** | ⚠ | O sistema deve emitir alertas e notificações para erros na separação de medicamentos ou baixa de estoque. | Alertas devem ser enviados aos responsáveis para correção rápida e prevenção de falhas críticas. |

<sub>Fonte: Material produzido pelos autores (2025).</sub>

</div>


## Requisitos Não Funcionais

<div align="center">

| Requisito | | Descrição | Regra de Negócio |
| --- | --- | --- | --- |
| **RNF01** | ✅ | O sistema deve garantir alta disponibilidade para evitar interrupções no processo hospitalar. | O tempo de inatividade não deve ultrapassar 1% ao mês, garantindo continuidade na operação. |
| **RNF02** | ✅ | O tempo de resposta do sistema para processar uma solicitação de separação de medicamentos deve ser otimizado. | O tempo máximo para validar e processar um pedido de medicamentos não pode exceder 5 segundos. |
| **RNF03** | ⚠ | A integração com o sistema hospitalar deve ser segura e confiável. | Deve utilizar padrões de segurança como **SSL/TLS** e autenticação de dois fatores para acessos administrativos. |
| **RNF04** | ✅ | O sistema deve armazenar logs de todas as operações realizadas. | Os logs devem ser mantidos por no mínimo **5 anos** para fins de auditoria e conformidade regulatória. |
| **RNF05** | ✅ | A interface homem-máquina (IHM) deve ser intuitiva e de fácil uso. | A IHM deve seguir diretrizes de **usabilidade** e acessibilidade para que qualquer operador possa utilizar o sistema sem treinamento extenso. |
| **RNF06** | ⚠ | O sistema deve suportar a escalabilidade para ser expandido para outros setores do hospital. | A arquitetura deve permitir a adição de novos módulos sem comprometer o desempenho do sistema. |
| **RNF07** | ✅ | O sistema deve garantir **rastreabilidade média** dos medicamentos. | Cada medicamento separado deve ser registrado com **data, hora e responsável pela operação** para rastreamento completo. |
| **RNF08** | ✅ | A comunicação entre os dispositivos do sistema deve ter **baixa latência**. | O tempo máximo de comunicação entre sensores e sistema central não deve exceder **1000ms**. |
| **RNF09** | ⚠ | A solução deve ser compatível com os dispositivos já utilizados pelo hospital. | Deve suportar leitura de **códigos de barras**, integração com **RFID** e operar nos sistemas utilizados pelo hospital. |
| **RNF10** | ✅ | O sistema deve fornecer uma interface amigável para monitoramento e ajustes em tempo real. | A interface deve ser acessível apenas para usuários autorizados e deve garantir usabilidade intuitiva. |

<sub>Fonte: Material produzido pelos autores (2025).</sub>

</div>

# Provas de Atendimento

Para comprovar que os requisitos marcados como atendidos foram de fato implementados, gravamos um vídeo demonstrando o funcionamento do sistema. Nele, é possível visualizar o sistema em ação, evidenciando o cumprimento de cada um dos requisitos validados.




# Proximos Passos

Com os requisitos verificados, elaboramos uma tabela com os próximos passos para cada requisito que foi apenas parcialmente atendido ou não atendido. O objetivo é explicar os motivos por trás da parcialidade ou da ausência de atendimento, além de indicar o caminho inicial para a implementação desses requisitos, caso sejam necessários em etapas futuras.

<div align="center">

| Requisito |   | Próximos Passos |
|-----------|---|------------------|
| **RF02**  | ⚠ | Como não dispomos de informações suficientes para integrar diretamente com a infraestrutura do hospital, deixamos o sistema aberto para compatibilidade com diversos bancos de dados e sistemas. Assim que as especificações forem definidas, será necessário implementar os conectores adequados para a integração. |
| **RF07**  | ⛔ | Atualmente, o sistema possui apenas um tipo de usuário (o operador). Caso haja necessidade de um acesso mais restrito, será preciso adaptar o banco de dados para incluir níveis de permissão e criar no frontend uma versão simplificada das telas e rotas para esse novo perfil de usuário. |
| **RF10**  | ⚠ | O sistema já envia alertas de erro ao operador, mas ainda não possui alertas de baixo estoque. Para implementá-los, basta adicionar verificações no banco de dados que disparem notificações ao atingir quantidades mínimas predefinidas. |
| **RNF03** | ⚠ | Atualmente, as senhas são armazenadas com hash, garantindo segurança básica. Caso seja necessário reforçar a segurança, recursos adicionais como autenticação de dois fatores deverão ser implementados. |
| **RNF06** | ⚠ | Devido à falta de informações e ao escopo atual do projeto, as integrações estão limitadas a aplicações organizacionais. Para expandir para outras áreas, serão necessárias adaptações específicas conforme os novos requisitos. |
| **RNF09** | ⚠ | O sistema suporta leitura por QR Code e proximidade. Caso o hospital utilize outro método, como RFID, será necessário implementar esse novo tipo de leitura no robô. |

<sub>Fonte: Material produzido pelos autores (2025).</sub>

</div>

