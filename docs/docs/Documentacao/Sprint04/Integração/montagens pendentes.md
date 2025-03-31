
# Montagens Pendentes

## 1. Comportamento no Back-End

### 1.1. Controller: `getPendentesMontagem`

```python
def getPendentesMontagem(self):
    try:
        pendentesMontagem = (
            db.session.query( 
                Montagem.id.label("id_montagem"),
                Paciente.nome.label("nome_paciente"),
                Paciente.HC.label("hc"),
                Paciente.Leito.label("leito"),
                Montagem.datetime.label("datetime")
            )
            .join(Lista, Montagem.id_lista == Lista.id) 
            .join(Paciente, Lista.id_paciente == Paciente.id)
            .filter(Montagem.status == 0)
            .order_by(Montagem.datetime.asc())
            .all()
        )
        montagens = [
            {
                "id": r.id_montagem,
                "nome_paciente": r.nome_paciente,
                "hc": r.hc,
                "leito": r.leito,
                "datetime": r.datetime
            }
            for r in pendentesMontagem
        ]
        return montagens, 200
    
    except Exception as e:
        return {"erro": str(e)}, 404
```

### 1.2. Endpoint

```python
@montagem_router_bp.route("/pendentes", methods=["GET"])
def router_getPendentes_montagem():
    res, status_code = montagem_controller.getPendentesMontagem()
    return jsonify(res), status_code
```

### 1.3. Rota HTTP: `/montagem/pendentes` [GET]

- **Controlador:** `MontagemController.getPendentesMontagem()`
- **Função:** Consulta todas as montagens com status `0` (pendente) e realiza joins com as tabelas `Paciente` e `Lista`.
- **Resposta:** Um array de objetos contendo:
  - `id`: Identificador da montagem.
  - `nome_paciente`: Nome do paciente.
  - `hc`: Código HC do paciente.
  - `leito`: Número do leito.
  - `datetime`: Data/hora da criação da montagem.

#### Exemplo de Resposta:

```json
[
  {
    "id": 12,
    "nome_paciente": "Maria Clara",
    "hc": "HC12345",
    "leito": "203A",
    "datetime": "2025-03-30T09:30:00"
  },
  {
    "id": 13,
    "nome_paciente": "João Pedro",
    "hc": "HC67890",
    "leito": "204B",
    "datetime": "2025-03-30T10:15:00"
  }
]
```

---

## 2. Comportamento no Front-End

### 2.1. Componente: `Pendentes`

- O componente `Pendentes` faz uma requisição HTTP (via `axios`) para o endpoint `/montagem/pendentes` assim que é montado (`useEffect`).
- Os dados recebidos são armazenados no estado local `montagens`.
- Cada item da lista de montagens é renderizado como um componente `MontagemItem`.

### 2.2. Fluxo da Página

#### 1. Inicialização
- `useEffect` dispara a requisição `GET`.
- A resposta é registrada no console para depuração.

#### 2. Atualização de Estado
- O estado `montagens` é preenchido com os dados retornados pela API.

#### 3. Renderização
- Se a lista estiver vazia, exibe o texto: **"Nenhuma montagem pendente encontrada."**
- Caso contrário, renderiza cada item com:
  - Nome do paciente
  - HC
  - Leito
  - Data/hora da montagem

### 2.3. Código Resumido da Integração

```javascript
useEffect(() => {
  axios.get("http://localhost:5000/montagem/pendentes")
    .then((res) => {
      setMontagens(res.data);
    })
    .catch((err) => {
      console.error("Erro ao buscar montagens:", err);
    });
}, []);
```

### Print tela Montagens Pendentes

<div align="center">
![Tela Montagens Pendentes](/../../media/montagensPendetesS4.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>