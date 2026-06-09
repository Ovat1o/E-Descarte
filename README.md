# É-Descarte — Métodos e Estruturas por Bloco

---

## `data/storage.py`

| Estrutura | Onde usa |
|---|---|
| `list = []` | Declarar cada lista/tabela |
| `dict = {}` | Declarar o controlador de IDs `_ids` |
| `def` | Declarar a função `proximo_id()` e `popular()` |
| `dict[chave]` | Acessar e atualizar o contador de IDs |
| `lista.extend([...])` | Adicionar vários registros de uma vez no `popular()` |

---

## `repositories/`

Todos os repositories compartilham as mesmas estruturas. O que muda é só a lista que cada um manipula.

| Estrutura | Onde usa |
|---|---|
| `def` | Declarar cada função CRUD |
| `dict = {}` | Montar o dicionário do novo registro no `criar()` |
| `lista.append(dict)` | Adicionar o novo registro à lista no `criar()` |
| `next()` | Buscar um único registro na lista |
| `for` dentro do `next()` | Percorrer a lista pra encontrar o item |
| `if` dentro do `next()` | Filtrar pelo campo desejado (ex: `id`, `email`) |
| `None` como valor padrão | Retornar quando o registro não é encontrado |
| `if item:` | Verificar se o registro foi encontrado antes de agir |
| `item["campo"] = valor` | Atualizar um campo do dicionário (Update) |
| `item.update(campos)` | Atualizar vários campos de uma vez com `**kwargs` |
| `lista.remove(item)` | Remover o registro da lista (Delete físico) |
| `list comprehension` | Listar registros com filtro (ex: só os ativos) |
| `return` | Retornar o registro afetado ou `None` |

### Detalhando por função

**`criar()`**
- `def` → `dict = {}` → `lista.append()` → `return`

**`buscar_por_id()` / `buscar_por_email()` / etc.**
- `def` → `next((x for x in lista if condição), None)` → `return`

**`listar_todos()` / `listar_ativos()` / etc.**
- `def` → `list comprehension [x for x in lista if condição]` → `return`

**`atualizar()`**
- `def` → chama `buscar_por_id()` → `if item:` → `item.update(campos)` → `return`

**`deletar()`**
- `def` → chama `buscar_por_id()` → `if item:` → `item["ativo"] = False` ou `lista.remove(item)` → `return`

### Exclusivos do `estoque_repo.py`

| Estrutura | Onde usa |
|---|---|
| `is not None` | Verificar se existe estoque em `tem_estoque()` |
| `and` | Combinar duas condições (item existe + quantidade > 0) |
| `>=` | Verificar se tem quantidade suficiente antes de decrementar |

### Exclusivos do `usuario_repo.py`

| Estrutura | Onde usa |
|---|---|
| `+=` | Somar pontos em `adicionar_pontos()` |
| `-=` | Subtrair pontos em `subtrair_pontos()` |
| `if pontos >= custo` | Validar se tem pontos suficientes antes de subtrair |

---

## `services/`

| Estrutura | Onde usa |
|---|---|
| `def` | Declarar cada função de serviço |
| `import` | Importar os repositories necessários |
| `if not variavel:` | Validar se o registro existe |
| `if ... != "ativa":` | Validar status da máquina |
| `if ... < ...:` | Validar se o usuário tem pontos suficientes |
| `if not ... :` | Validar se tem estoque disponível |
| `*` (multiplicação) | Calcular pontos: `quantidade * pontos_por_item` |
| `return valor, mensagem` | Retornar uma tupla com o resultado e uma mensagem |
| Encadeamento de `if` | Cada validação antes de executar a operação |

### Fluxo padrão de um service

```
def executar_operacao(...):
    # 1. Validações (if not → return None, "mensagem de erro")
    # 2. Cálculos necessários
    # 3. Chamadas aos repositories na ordem certa
    # 4. return resultado, "mensagem de sucesso"
```

---

## `utils/helpers.py`

| Estrutura | Onde usa |
|---|---|
| `def` | Declarar cada função utilitária |
| `import os` | Limpar a tela do terminal |
| `os.system("cls")` | Limpar tela no Windows |
| `os.system("clear")` | Limpar tela no Linux/Mac |
| `print("-" * 40)` | Imprimir linha separadora |
| `str.strip()` | Remover espaços extras do input do usuário |
| `str.replace()` | Limpar formatação do CPF (ex: remover `.` e `-`) |
| `try / except ValueError` | Capturar erro quando o input não é um número |
| `int()` | Converter input de string pra inteiro |
| `f-string` | Formatar mensagens com variáveis |

---

## `views/`

| Estrutura | Onde usa |
|---|---|
| `def` | Declarar cada função de menu |
| `import` | Importar os services e helpers necessários |
| `while True` | Manter o menu aberto até o usuário sair |
| `print()` | Exibir opções e mensagens na tela |
| `input()` | Capturar escolha e dados do usuário |
| `if / elif / else` | Direcionar para a ação escolhida no menu |
| `break` | Sair do `while True` quando o usuário escolher voltar/sair |
| `try / except ValueError` | Tratar input inválido (ex: digitar letra no lugar de número) |
| `int()` | Converter a opção digitada em número |
| `for` | Listar itens na tela (máquinas, recompensas, histórico) |
| `enumerate()` | Listar itens numerados para o usuário escolher |
| `f-string` | Montar as linhas de exibição com dados das entidades |

### Fluxo padrão de um menu

```
def menu_alguma_coisa():
    while True:
        print("opções...")
        opcao = input("Escolha: ")

        if opcao == "1":
            # chama service ou outra função
        elif opcao == "2":
            # chama service ou outra função
        elif opcao == "0":
            break   # volta pro menu anterior
        else:
            print("Opção inválida.")
```

---

## `main.py`

| Estrutura | Onde usa |
|---|---|
| `import` | Importar `popular()` do storage e o menu principal |
| Chamada de função | `popular()` para carregar os dados de teste |
| Chamada de função | Chamar o menu principal para iniciar o programa |