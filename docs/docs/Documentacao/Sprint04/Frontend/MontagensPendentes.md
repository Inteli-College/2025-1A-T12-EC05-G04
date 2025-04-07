---
title: Tela de montagens pendentes
slug: tela-montagens-pendentes
sidebar_position: 3
---

## Visão Geral

&emsp;A página "Montagens Pendentes" exibe as listas de montagem que estão aguardando para serem iniciadas. Ela permite ao usuário visualizar as montagens pendentes e iniciar o processo para uma delas.

<div align="center">
![Página de Montagens Pendentes](/../../media/docsFrontend/montagem-completa.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

## Funcionalidades

**Sistema de Loop:**A cada lista de montagem no backend, um item de montagem é criado no na página de montagem pendentes, de forma que não é necessário adicionar cada um desses itens manualmente.

**Feedback Visual de Estado:** A interface utiliza cores e opacidade para indicar o estado das montagens:

- **Cinza Escuro** (Padrão): Montagem pendente e pronta para ser iniciada. O botão "INICIAR MONTAGEM" está ativo. Ao clicar neste botão, uma requisição é enviada ao backend para sinalizar o início do processo de montagem para aquele item específico. .
<div align="center">
![Página de Montagens Pendentes](/../../media/docsFrontend/montagem-cinza.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>


- **Verde**: A montagem que está atualmente em processo. Assim que a montagem for terminada, o item é removido da lista.
<div align="center">
![Página de Montagens Pendentes](/../../media/docsFrontend/montagem-fazendo.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>


- **Cinza Claro** (Baixa Opacidade): Montagens pendentes que estão temporariamente bloqueadas porque outra montagem já está em andamento. Assim que a montagem for finalizada, esse item volta a sua cor padrão.
<div align="center">
![Página de Montagens Pendentes](/../../media/docsFrontend/montagem-des.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>