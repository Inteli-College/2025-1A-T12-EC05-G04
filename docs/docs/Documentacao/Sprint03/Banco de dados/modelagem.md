---
title: Modelagem do Banco de Dados
slug: /banco-de-dados/modelagem
sidebar_position: 2
---

# O que é e qual é a importância da modelagem do banco de dados
&emsp;A modelagem dos dados consiste em criar uma estrutura ou esquema visual que represente os dados a serem armazenados e as relações entre os mesmos. Nesse sentido, foram definidos os modelos conceitual, lógico e físico, e o modelo físico será explorado a seguir. 

# Modelo físico

&emsp;O modelo físico representa as tabelas e suas colunas respectivas, bem como os tipos de dado, relações e restrições do banco de dados. A seguir, é possível visualizar o diagrama do modelo físico criado durante a sprint 3.

<div align="center">
![Modelo físico do banco de dados](/../../media/modelo_fisico.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>

&emsp;Para criar as tabelas no banco de dados, foi utilizado um script SQL dentro da ferramenta DBeaver. Nas próximas subseções, serão abordadas as especificidades de cada uma das 7 tabelas criadas.

## Usuario

&emsp;A tabela usuario foi criada a partir do seguinte comando SQL:

```sql
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    CPF VARCHAR(11) NOT NULL
);
```

&emsp;Essa tabela têm 5 colunas, sendo 1 primary key. Essa tabela guarda as inforamações identificação do usuários e dados de acesso à plataforma web.

## Paciente

&emsp;A tabela paciente foi criada a partir do seguinte comando SQL:

```sql
CREATE TABLE IF NOT EXISTS paciente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    HC VARCHAR(20) NOT NULL,
    Leito VARCHAR(25) NOT NULL
);
```
&emsp;Essa tabela têm 4 colunas, sendo 1 primary key. Essa tabela guarda as inforamações identificação do paciente e leito hospitalar.


## Montagem

&emsp;A tabela montagem foi criada a partir do seguinte comando SQL:


```sql
    CREATE TABLE IF NOT EXISTS montagem (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_lista INTEGER NOT NULL,
    data VARCHAR(10) NOT NULL,
    id_usuario INTEGER NOT NULL,
    status VARCHAR(1) NOT NULL,
    FOREIGN KEY (id_lista) REFERENCES lista(id),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
```
&emsp;Essa tabela têm 5 colunas, sendo 1 primary key e 2 foreign key. Essa tabela serão armazenadas informações referêntes as montagens enviadas ao sistema. As foreign key terão a função de ligar a montagem à lista de medicamentos do kit e ao usuário que aprovou a montagem, além disso apresenta a coluna `data`. Com essas dados conseguiremos guardar logs das montagens e monitorar quais usuários aprovaram cada montagem. A coluna `status` guardará um valor para identificação se a montagem finalizou com sucesso, está pendente ou terminou incompleta.


## Lista

&emsp;A tabela lista foi criada a partir do seguinte comando SQL:

```sql
    CREATE TABLE IF NOT EXISTS lista (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_montagem INTEGER NOT NULL,
    id_paciente INTEGER NOT NULL,
    id_remedio INTEGER NOT NULL,
    quantidade VARCHAR(10) NOT NULL,
    FOREIGN KEY (id_montagem) REFERENCES montagem(id),
    FOREIGN KEY (id_paciente) REFERENCES paciente(id),
    FOREIGN KEY (id_remedio) REFERENCES lote(id)
);
```

&emsp;Dessa forma, a tabela lista possui possui 5 colunas, sendo 1 primary key e 3 foreign keys. Essa tabela guarda informações sobre os remédios necessitados por uma lista que já está em montagem, de forma que permite mais de uma linha relacionada a um único `id_montagem`. O `id_paciente` é utilizado para conhecer o paciente que necessita dos remédios. O `id_remédio` e a `quantidade` dizem qual o lote de remédio necessitado e a quantidade do mesmo que deve ser retirada do estoque.

## Lote

&emsp;A tabela lote foi criada a partir do seguinte comando SQL:

```sql
    CREATE TABLE IF NOT EXISTS lote (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    remedio VARCHAR(100) NOT NULL,
    compostaAtivo VARCHAR(10) NOT NULL,
    dose VARCHAR(10) NOT NULL,
    validade VARCHAR(10) NOT NULL,
    quantidade VARCHAR(10) NOT NULL
);
```

&emsp;Dessa forma, a tabela Lote possui possui 6 colunas, sendo 1 primary key. A coluna `remedio` guarda o nome do medicamento, enquanto `comportoAtivo` guarda a identificação principal do remédio a partir do composto ativo que é feito. A `dose` diz respeito às diferentes doses e tamanhos de comprimidos que um medicamento pode ter, enquanto `validade` controla o tempo máximo que aquele remédio ainda tem no estoque. Por fim, a `quantidade` diz quantos comprimidos ainda existem para uso estoque.

## Erro de montagem

&emsp;A tabela erroMontagem foi criada a partir do seguinte comando SQL:

```sql
    CREATE TABLE IF NOT EXISTS erroMontagem (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_montagem INTEGER NOT NULL,
    mensagem VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_montagem) REFERENCES montagem(id)
);
```
&emsp; A tabela erroMontagem possui 3 colunas, sendo 1 primary key e 1 foreing key. Ela foi criada para armazenar possíveis erros de execução da montagem dos kits de medimentos, a nossa ideia inicial é que quando ocorrer algum problema de montagem o backend envie uma mensagem para o banco de dados que será salva na coluna `mensagem` e por meio dessa mensagem e o contagem do número de elementos da tabela possamos gerar relatóriso de metrificação do desempenho de trabalho do robô e mostrem as causas dos erros.

## Devolução

&emsp;A tabela devolucao foi criada a partir do seguinte comando SQL:

```sql
    CREATE TABLE IF NOT EXISTS devolucao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime VARCHAR(20) NOT NULL,
    id_remedio INTEGER NOT NULL,
    quantidade VARCHAR(10) NOT NULL,
    id_usuario INTEGER NOT NULL,
    FOREIGN KEY (id_remedio) REFERENCES lote(id),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
``` 

&emsp; A tabela erroMontagem possui 5 colunas, sendo 1 primary key e 2 foreing key. Ela servirá para salvar logs de devoluções do sistema, dessa forma conseguimeros retornar os medicamentos devolvidos à farmácia e monitorar essas devoluções por meio de relatórios.
