---
title: Tela de Login
slug: /interface-final/login
sidebar_position: 1
---

## Funcionalidade

&emsp;A tela de login é a primeira interface exibida no site. Nela, o operador pode inserir suas credenciais previamente cadastradas para acessar sua conta, utilizando e-mail e senha.


<div align="center">
![Login](../../../../../media/docsInterfaceFinal/login/Login.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

## Integração

&emsp;A tela de login realiza a autenticação do operador por meio de uma requisição `POST` para a rota `/auth/login`, implementada no backend Flask. Os dados enviados incluem o e-mail e a senha informados no formulário.

&emsp;Após a autenticação bem-sucedida, fazemos uma segunda requisição `GET` para a rota `/auth/getUserName/:email` com o objetivo de buscar o nome e o identificador do operador. Esses dados são armazenados temporariamente no `localStorage` para uso nas demais telas do sistema.

&emsp;Caso ocorra algum erro de autenticação ou falha na conexão, mensagens apropriadas são exibidas ao usuário. Todo o processo utiliza o formato `application/json` para envio e recebimento das informações.
