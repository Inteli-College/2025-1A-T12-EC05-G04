---
title: Alterações finais
slug: s5/hardware/alteracoes
sidebar_position: 1
---

# O que ocorreu com o hardware/firmware esta sprint?

## Correções

&emsp;Durante os testes finais do hardware, percebemos uma quantidade de erros de movimentação considerável ao tentar movimentar o robô, em que ele parecia "não querer" se movimentar. Surpreendentemente, depois de um tempo de debugging e conversas com o professor, percebemos que o erro era relativamente simples: O braço não estava "calibrado". O que isso significa? O braço robótico possui um ponto de origem, ou seja, um ponto em que ele considera ser o "zero" de todas as suas movimentações. Quando o braço não está calibrado, ele não sabe onde está e, portanto, não consegue se movimentar corretamente. Para resolver isso, foi necessário fazer uma calibração do braço robótico, utilizando o software da própria fabricante: O Dobot Studio. Instruções serão dadas na sessão "Como iniciar o sistema".

&emsp;Além disso, ao implementar o callback das ações atuais do sistema, erros recorrentes aconteciam devido à formatação dos dados, mas foi facilmente corrigido.

## Alterações

&emsp;Visando a integração do Raspberry e Dobot com o servidor, realizamos algumas alterações nas mensagens enviadas pelo microcomputador pelo Web Socket. A principal mudança foi a adição do campo "id_montagem", que permite ao servidor identificar à qual montagem o callback atual pertence. Em uma situação futura, isso permitiria uma adaptação relativamente simplificada de um sistema com vários controladores, que cuidariam de diferentes montagens. Vale ressaltar que esta função *não* está implementada, mas seria possível em uma continuação futura do projeto.
