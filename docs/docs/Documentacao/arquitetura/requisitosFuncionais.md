---
title: Requisitos Funcionais e Não Funcionais
slug: /arquitetura-do-sistema/requisitos-rf-rnf
sidebar_position: 2
---


## Requisitos Funcionais

Requisitos funcionais descrevem as funcionalidades e comportamentos esperados do sistema para atender às necessidades dos usuários e da organização. Eles definem **o que** o sistema deve fazer para cumprir seus objetivos, garantindo que as operações essenciais sejam realizadas de maneira eficiente. No contexto do projeto, os requisitos funcionais especificam as capacidades da solução automatizada para a separação de medicamentos, desde a integração com sistemas hospitalares até a rastreabilidade dos medicamentos.


| Requisito | Descrição | Regra de Negócio |
| --- | --- | --- |
| **RF01** | O sistema deve permitir a automação da separação de medicamentos com base nas prescrições eletrônicas. | O sistema deve garantir a seleção correta dos medicamentos prescritos, reduzindo erros de separação. |
| **RF02** | O sistema deve integrar-se ao sistema hospitalar para obter prescrições digitais e atualizar o estoque automaticamente. | A comunicação com o sistema hospitalar deve ser segura e confiável, garantindo integridade dos dados. |
| **RF03** | O sistema deve possuir sensores para leitura de código de barras, peso e detecção de volume. | A validação deve garantir que apenas medicamentos corretos sejam incluídos nos kits, minimizando erros de montagem. |
| **RF04** | O sistema deve organizar os medicamentos na sequência necessária para cada paciente. | A organização da "Fita de Medicamentos" deve seguir as diretrizes médicas e farmacêuticas. |
| **RF05** | O sistema deve permitir o rastreamento detalhado dos medicamentos. | Todas as movimentações devem ser registradas, garantindo segurança e conformidade com normas hospitalares. |
| **RF06** | O sistema deve gerar relatórios detalhados de atividades e desempenho. | Os relatórios devem incluir tempo de montagem, taxa de erros e estatísticas de uso, podendo ser exportados para análise. |
| **RF07** | O sistema deve permitir testes pilotos em ambiente hospitalar antes da implementação total. | Os testes devem ser realizados inicialmente na UTI para validação e ajustes conforme necessidade. |
| **RF08** | O sistema deve oferecer suporte para treinamento da equipe de farmácia. | O treinamento deve ser documentado e contar com materiais explicativos para garantir correta utilização. |
| **RF09** | O sistema deve permitir diferentes níveis de acesso para usuários. | Apenas administradores podem realizar alterações críticas e ajustes na configuração do sistema. |
| **RF10** | O sistema deve registrar um histórico detalhado de operações. | Todas as atividades, ajustes manuais e erros detectados devem ser registrados para auditoria e segurança. |
| **RF11** | O sistema deve atualizar automaticamente o estoque conforme os medicamentos são separados. | O estoque hospitalar deve ser atualizado em tempo real para evitar falhas na reposição de medicamentos. |
| **RF12** | O sistema deve emitir alertas e notificações para erros na separação de medicamentos ou baixa de estoque. | Alertas devem ser enviados aos responsáveis para correção rápida e prevenção de falhas críticas. |


Esses requisitos funcionais garantem que o sistema atenda às demandas operacionais do hospital, promovendo eficiência, segurança e rastreabilidade na administração de medicamentos. Eles estabelecem **as principais funcionalidades do sistema** permitindo sua usabilidade e integração geral com os processos hospitalares.

## Requisitos Não Funcionais

Diferente dos requisitos funcionais, os não funcionais especificam características do sistema que **não estão diretamente relacionadas às funcionalidades**, mas que são essenciais para seu desempenho, segurança, confiabilidade e experiência do usuário. Esses requisitos garantem que a automação da separação de medicamentos funcione de maneira estável, segura e escalável dentro do ambiente hospitalar.

| Requisito | Descrição | Regra de Negócio |
| --- | --- | --- |
| **RNF01** | O sistema deve garantir alta disponibilidade para evitar interrupções no processo hospitalar. | O tempo de inatividade não deve ultrapassar 1% ao mês, garantindo continuidade na operação. |
| **RNF02** | O tempo de resposta do sistema para processar uma solicitação de separação de medicamentos deve ser otimizado. | O tempo máximo para validar e processar um pedido de medicamentos não pode exceder 5 segundos. |
| **RNF03** | A integração com o sistema hospitalar deve ser segura e confiável. | Deve utilizar padrões de segurança como **SSL/TLS** e autenticação de dois fatores para acessos administrativos. |
| **RNF04** | O sistema deve armazenar logs de todas as operações realizadas. | Os logs devem ser mantidos por no mínimo **5 anos** para fins de auditoria e conformidade regulatória. |
| **RNF05** | A interface homem-máquina (IHM) deve ser intuitiva e de fácil uso. | A IHM deve seguir diretrizes de **usabilidade** e acessibilidade para que qualquer operador possa utilizar o sistema sem treinamento extenso. |
| **RNF06** | O sistema deve suportar a escalabilidade para ser expandido para outros setores do hospital. | A arquitetura deve permitir a adição de novos módulos sem comprometer o desempenho do sistema. |
| **RNF07** | O sistema deve garantir **rastreabilidade total** dos medicamentos. | Cada medicamento separado deve ser registrado com **data, hora e responsável pela operação** para rastreamento completo. |
| **RNF08** | A comunicação entre os dispositivos do sistema deve ter **baixa latência**. | O tempo máximo de comunicação entre sensores e sistema central não deve exceder **1000ms**. |
| **RNF09** | A solução deve ser compatível com os dispositivos já utilizados pelo hospital. | Deve suportar leitura de **códigos de barras**, integração com **RFID** e operar nos sistemas utilizados pelo hospital. |
| **RNF10** | O sistema deve fornecer uma interface amigável para monitoramento e ajustes em tempo real. | A interface deve ser acessível apenas para usuários autorizados e deve garantir usabilidade intuitiva. |


Garantindo que esses requisitos sejam atendidos isso ira assegurar que o sistema seja acessivel, seguro e eficiente dentro do ambiente instalado. Eles garantem **alto desempenho, disponibilidade, escalabilidade e conformidade**, permitindo que o sistema funcione de maneira fluida e sustentável no longo prazo de uso. Ao atender a esses requisitos, a automação da separação de medicamentos será capaz de operar com máxima eficiência e segurança dentro do hospital da Unicamp.
