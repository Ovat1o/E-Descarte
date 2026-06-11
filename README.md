# É-Descarte — Documentação linha a linha

Este documento explica **cada linha de cada arquivo** do projeto. A ideia é que você consiga entender o código inteiro mesmo sem experiência prévia em Python, e que consiga explicar qualquer parte dele numa apresentação.

---

## Índice

1. [Conceitos básicos que se repetem](#0-conceitos-básicos-que-se-repetem)
2. [Como o projeto está organizado (arquitetura MVC)](#1-como-o-projeto-está-organizado)
3. [`main.py`](#2-mainpy)
4. [Pasta `models/`](#3-pasta-models)
   - [`models/electronic.py`](#31-modelselectronicpy)
   - [`models/user.py`](#32-modelsuserpy)
   - [`models/discard.py`](#33-modelsdiscardpy)
5. [Pasta `controllers/`](#4-pasta-controllers)
   - [`controllers/electronic_controller.py`](#41-controllerselectronic_controllerpy)
   - [`controllers/user_controller.py`](#42-controllersuser_controllerpy)
   - [`controllers/discard_controller.py`](#43-controllersdiscard_controllerpy)
6. [Pasta `views/`](#5-pasta-views)
   - [`views/menu.py`](#51-viewsmenupy)
   - [`views/eletronics_page.py`](#52-viewseletronics_pagepy)
   - [`views/user_page.py`](#53-viewsuser_pagepy)
   - [`views/discard_page.py`](#54-viewsdiscard_pagepy)
7. [Pasta `data/` e os arquivos `__init__.py`](#6-pasta-data-e-os-init__py)
8. [O caminho completo de um descarte (juntando tudo)](#7-o-caminho-completo-de-um-descarte)

---

## 0. Conceitos básicos que se repetem

Antes de ir arquivo por arquivo, vale fixar alguns conceitos que aparecem o tempo todo. Se você entender estes, 80% do código fica óbvio.

**Comentário (`#`)** — Tudo que vem depois de `#` numa linha é ignorado pelo Python. Serve só pra explicar o código pra humanos.

**Variável** — Um nome que guarda um valor. `nome = "Tales"` guarda o texto "Tales" na variável `nome`.

**Função (`def`)** — Um bloco de código com nome, que só roda quando você "chama" ele. `def listar():` cria a função `listar`; `listar()` executa ela. Funções podem receber dados (parâmetros) e devolver dados (`return`).

**String** — Texto, sempre entre aspas: `"iPhone 13"`. Tudo que é lido de um arquivo de texto chega como string, mesmo que pareça número (`"40"` é texto, não o número 40).

**`int()`** — Converte texto em número inteiro. `int("40")` vira `40`. Necessário pra fazer contas, porque `"40" * 2` daria `"4040"` (texto repetido), enquanto `40 * 2` dá `80`.

**Lista (`[]`)** — Uma sequência ordenada de itens: `[1, 2, 3]`. Pode crescer e diminuir.

**Dicionário (`{}`)** — Uma coleção de pares "chave: valor": `{"nome": "Tales", "pontos": 80}`. Você acessa um valor pela chave: `usuario["nome"]` devolve `"Tales"`. É como uma ficha com campos preenchidos.

**`if` / `elif` / `else`** — Decisão. "Se tal condição, faça isso; senão se outra condição, faça aquilo; senão, faça isso outro."

**`for ... in ...`** — Repetição sobre uma coleção. "Para cada item nesta lista, faça isso."

**`while`** — Repetição enquanto uma condição for verdadeira. "Enquanto isso for verdade, continue repetindo."

**`return`** — Encerra a função e devolve um valor pra quem chamou. Depois de um `return`, nada mais na função executa.

**`None`** — O "nada" do Python. Representa ausência de valor. Funções de busca devolvem `None` quando não encontram nada.

**f-string** — Um texto com o `f` antes das aspas, que permite inserir variáveis dentro de `{}`. Se `nome = "Tales"`, então `f"Olá {nome}"` produz `"Olá Tales"`.

**Tupla `(a, b)`** — Como uma lista, mas fixa. Usamos no padrão `(sucesso, mensagem)` pra uma função devolver duas coisas ao mesmo tempo.

---

## 1. Como o projeto está organizado

O projeto segue o padrão **MVC** (Model–View–Controller), que separa o código em três responsabilidades. A regra mental é:

> **A View conversa com o usuário. O Controller pensa. O Model guarda.**

- **Model** (`models/`) — Só mexe nos arquivos `.txt`. Lê e grava dados. Não fala com o usuário, não decide regras.
- **Controller** (`controllers/`) — A lógica/regras. Valida dados, calcula pontos, decide se uma operação pode acontecer. Não fala com o usuário e não mexe diretamente em arquivo (pede pro Model fazer).
- **View** (`views/`) — A interface. Só `input()` (pergunta) e `print()` (mostra). Não tem regra de negócio nem mexe em arquivo.

Por que separar assim? Porque se amanhã você trocar os `.txt` por um banco de dados, só os Models mudam. Se trocar o menu de terminal por um site, só as Views mudam. Cada parte tem um motivo único pra mudar.

O fluxo de uma ação sempre desce e sobe por essas camadas:

```
Usuário → View → Controller → Model → arquivo .txt
                                  ↓
Usuário ← View ← Controller ← Model ← (dados lidos)
```

---

## 2. `main.py`

Este é o arquivo que você executa pra iniciar o programa (`python main.py`). Ele é minúsculo de propósito: a única função dele é dar a partida.

```python
1  from views.menu import startApp
2
3  def main():
4      startApp()
5
6
7  if __name__ == "__main__":
8      main()
```

**Linha 1** — `from views.menu import startApp`. Importa (traz pra cá) a função `startApp`, que está dentro do arquivo `menu.py`, dentro da pasta `views`. O ponto (`views.menu`) é como o Python navega entre pastas e arquivos. Depois desta linha, podemos usar `startApp()` aqui.

**Linha 3** — `def main():`. Define uma função chamada `main`. Ela não recebe parâmetros (parênteses vazios). É uma convenção comum ter uma função `main` como ponto de organização do programa.

**Linha 4** — `startApp()`. Dentro de `main`, chama a função que liga o menu principal. É aqui que o programa de fato começa a interagir.

**Linha 7** — `if __name__ == "__main__":`. Essa linha parece estranha mas tem um propósito claro. Todo arquivo Python tem uma variável automática chamada `__name__`. Quando você roda o arquivo diretamente (`python main.py`), o Python coloca `"__main__"` nessa variável. Quando o arquivo é importado por outro, `__name__` recebe o nome do arquivo. Então esta linha significa: "só execute o que está abaixo se este arquivo foi rodado diretamente, não se ele foi importado". É uma boa prática que evita que o programa dispare sozinho quando não deveria.

**Linha 8** — `main()`. Chama a função `main`, que por sua vez chama `startApp()`. É a faísca que liga tudo.

---

## 3. Pasta `models/`

Os três arquivos desta pasta seguem quase a mesma estrutura. Vou explicar o primeiro (`electronic.py`) em detalhe total, e nos outros dois vou focar nas diferenças, pra você não ler a mesma explicação três vezes.

### 3.1 `models/electronic.py`

Responsabilidade: ler e gravar eletrônicos no arquivo `data/electronics.txt`. Cada linha do arquivo tem o formato `id,nome,pontos` — por exemplo `1,iPhone 13,40`.

```python
1  # models/electronic.py
2  # Camada de dados (Model) da entidade Eletronico.
3  # Responsabilidade: ler e escrever em data/electronics.txt.
4  # NAO contem input() nem regras de negocio - so persistencia.
5
6  CAMINHO = "./data/electronics.txt"
```

**Linhas 1-4** — Comentários. Documentam o papel do arquivo. Não executam nada.

**Linha 6** — `CAMINHO = "./data/electronics.txt"`. Cria uma variável que guarda o caminho do arquivo. Está em MAIÚSCULAS porque é uma convenção em Python pra indicar "constante" — um valor que não muda durante a execução. A vantagem de guardar numa variável: se o caminho mudar, você edita só aqui. O `./` significa "a partir da pasta onde o programa foi iniciado".

#### Função `_ler_linhas()` — o coração do arquivo

```python
9   def _ler_linhas():
10      # Le o arquivo e devolve uma lista de dicionarios.
11      # Formato de cada linha: id,nome,pontos
12      eletronicos = []
13      try:
14          with open(CAMINHO, "r", encoding="utf-8") as arquivo:
15              for linha in arquivo:
16                  linha = linha.strip()
17                  if not linha:
18                      continue
19                  partes = linha.split(",")
20                  if len(partes) != 3:
21                      continue  # ignora linhas mal formatadas
22                  eletronicos.append({
23                      "id": int(partes[0]),
24                      "nome": partes[1],
25                      "pontos": int(partes[2]),
26                  })
27      except FileNotFoundError:
28          # se o arquivo nao existe ainda, retorna lista vazia
29          return []
30      return eletronicos
```

Todas as outras funções deste arquivo dependem desta. Ela transforma o texto cru do arquivo numa lista de dicionários organizada.

**Linha 9** — `def _ler_linhas():`. Define a função. O underline (`_`) no começo do nome é uma convenção que sinaliza "função interna, de uso só dentro deste arquivo". Outros arquivos não deveriam chamá-la diretamente.

**Linha 12** — `eletronicos = []`. Cria uma lista vazia. Ela vai sendo preenchida conforme lemos cada linha do arquivo.

**Linha 13** — `try:`. Começa um bloco de proteção. Significa "tente executar isto; se acontecer um erro específico, eu trato em vez de deixar o programa quebrar". O erro tratado está na linha 27.

**Linha 14** — `with open(CAMINHO, "r", encoding="utf-8") as arquivo:`. Abre o arquivo. Três detalhes:
- `"r"` = modo *read* (leitura). Só vamos ler, não escrever.
- `encoding="utf-8"` garante que acentos (á, ç, ã) sejam lidos corretamente.
- `with ... as arquivo` é a forma correta de abrir arquivos: o `with` garante que o arquivo seja **fechado automaticamente** no final, mesmo se der erro no meio. O arquivo aberto passa a ser acessível pelo nome `arquivo`.

**Linha 15** — `for linha in arquivo:`. Percorre o arquivo linha por linha. A cada volta do loop, a variável `linha` contém o texto de uma linha.

**Linha 16** — `linha = linha.strip()`. O `.strip()` remove espaços em branco e o caractere invisível de quebra de linha (`\n`) das duas pontas do texto. Sem isso, o `\n` no final atrapalharia a conversão dos pontos pra número.

**Linhas 17-18** — `if not linha: continue`. Se depois do strip a linha ficou vazia (era uma linha em branco), `not linha` é verdadeiro, e `continue` pula imediatamente pra próxima volta do loop, ignorando esta linha. Protege contra linhas vazias no arquivo.

**Linha 19** — `partes = linha.split(",")`. O `.split(",")` quebra o texto em pedaços toda vez que encontra uma vírgula, devolvendo uma lista. A linha `"1,iPhone 13,40"` vira `["1", "iPhone 13", "40"]`.

**Linhas 20-21** — `if len(partes) != 3: continue`. O `len()` conta quantos itens há na lista. Se não houver exatamente 3 pedaços, a linha está malformada (faltando ou sobrando vírgula), então pulamos com `continue`. O `!=` significa "diferente de".

**Linhas 22-26** — Monta um dicionário e o adiciona à lista com `.append()`. O `.append(x)` põe `x` no final da lista. Aqui o `x` é o dicionário `{"id": ..., "nome": ..., "pontos": ...}`. Repare:
- `int(partes[0])` — converte o primeiro pedaço (o ID) pra número. `partes[0]` é o primeiro item da lista (em Python a contagem começa no zero).
- `partes[1]` — o nome fica como texto mesmo, não precisa converter.
- `int(partes[2])` — converte o terceiro pedaço (os pontos) pra número.

Resultado: a linha `"1,iPhone 13,40"` vira o dicionário `{"id": 1, "nome": "iPhone 13", "pontos": 40}`.

**Linhas 27-29** — `except FileNotFoundError: return []`. Esta é a parte "se der erro" do `try`. Se o arquivo não existir (`FileNotFoundError`), em vez de quebrar, a função devolve uma lista vazia `[]`. Faz sentido: "não tem arquivo" equivale a "não tem nenhum eletrônico ainda".

**Linha 30** — `return eletronicos`. Devolve a lista completa de dicionários pra quem chamou a função. Esta linha só roda se a leitura deu certo (se tivesse dado erro, teríamos saído no `return []` da linha 29).

#### Função `_proximo_id()` — gera o ID automaticamente

```python
33  def _proximo_id():
34      # Gera o proximo ID com base no maior ID existente.
35      eletronicos = _ler_linhas()
36      if not eletronicos:
37          return 1
38      return max(e["id"] for e in eletronicos) + 1
```

**Linha 35** — `eletronicos = _ler_linhas()`. Lê todos os eletrônicos existentes, reaproveitando a função anterior.

**Linhas 36-37** — `if not eletronicos: return 1`. Se a lista está vazia (nenhum eletrônico cadastrado ainda), o primeiro ID será `1`.

**Linha 38** — `return max(e["id"] for e in eletronicos) + 1`. Aqui acontecem três coisas numa linha só:
- `e["id"] for e in eletronicos` é uma *generator expression*: produz o ID de cada eletrônico, um por um.
- `max(...)` pega o maior desses IDs.
- `+ 1` soma um, dando o próximo ID livre.

Se os IDs existentes são 1, 2 e 3, o maior é 3 e o próximo será 4. Isso evita que você precise controlar IDs manualmente.

#### Funções de consulta

```python
41  def listar():
42      # Devolve todos os eletronicos cadastrados.
43      return _ler_linhas()
44
45
46  def buscar_por_id(id_busca):
47      # Devolve o eletronico com o ID informado, ou None.
48      for e in _ler_linhas():
49          if e["id"] == id_busca:
50              return e
51      return None
52
53
54  def buscar_por_nome(nome_busca):
55      # Devolve uma lista de eletronicos cujo nome contem o texto buscado.
56      nome_busca = nome_busca.lower()
57      return [e for e in _ler_linhas() if nome_busca in e["nome"].lower()]
```

**Linhas 41-43** — `listar()`. A mais simples: só repassa o resultado de `_ler_linhas()`. Existe pra dar um nome claro e público à ação de "listar tudo".

**Linhas 46-51** — `buscar_por_id(id_busca)`. Recebe um ID e procura.
- Linha 48: percorre cada eletrônico.
- Linha 49: `if e["id"] == id_busca` — o `==` compara se são iguais (diferente do `=`, que atribui valor). Se o ID bate...
- Linha 50: `return e` — devolve esse eletrônico na hora e encerra a função.
- Linha 51: `return None` — só é alcançada se o loop terminou sem achar. Devolve `None` ("não encontrei").

**Linhas 54-57** — `buscar_por_nome(nome_busca)`. Busca por texto parcial.
- Linha 56: `nome_busca = nome_busca.lower()` — converte a busca pra minúsculas, pra que "iphone" ache "iPhone".
- Linha 57: uma *list comprehension*. Leia da direita pra esquerda: "para cada `e` em `_ler_linhas()`, **se** o texto buscado estiver contido no nome (também em minúsculas), inclua `e` na lista resultante". O `in` aqui verifica se um texto está dentro de outro: `"phone" in "iphone 13"` é verdadeiro. Devolve uma lista (pode haver vários resultados).

#### Função `salvar()` — grava um novo eletrônico

```python
60  def salvar(nome, pontos):
61      # Cria um novo eletronico, gera o ID e grava no arquivo.
62      novo = {"id": _proximo_id(), "nome": nome, "pontos": pontos}
63      with open(CAMINHO, "a", encoding="utf-8") as arquivo:
64          arquivo.write(f"{novo['id']},{novo['nome']},{novo['pontos']}\n")
65      return novo
```

**Linha 60** — `def salvar(nome, pontos):`. Recebe dois parâmetros: o nome e os pontos do eletrônico a criar.

**Linha 62** — Monta o dicionário do novo eletrônico. O ID é preenchido automaticamente chamando `_proximo_id()`.

**Linha 63** — `open(CAMINHO, "a", ...)`. Atenção ao modo `"a"` (*append*, anexar): ele adiciona ao **final** do arquivo sem apagar o que já existe. (Se fosse `"w"`, de *write*, apagaria todo o conteúdo antes de escrever.)

**Linha 64** — `arquivo.write(f"{novo['id']},{novo['nome']},{novo['pontos']}\n")`. Escreve a nova linha no arquivo. A f-string monta o texto no formato `id,nome,pontos`. O `\n` no final é a quebra de linha — sem ele, o próximo registro grudaria neste.

**Linha 65** — `return novo`. Devolve o dicionário criado (já com o ID), pra que a camada de cima possa mostrar "cadastrado com ID 3".

---

### 3.2 `models/user.py`

Tem a mesma estrutura do anterior, mas guarda usuários no formato `id,nome,email,senha,pontos` e ganha duas funções a mais: uma pra reescrever o arquivo inteiro e outra pra creditar pontos. Vou focar no que é diferente.

```python
9   def _ler_linhas():
10      usuarios = []
11      try:
12          with open(CAMINHO, "r", encoding="utf-8") as arquivo:
13              for linha in arquivo:
14                  linha = linha.strip()
15                  if not linha:
16                      continue
17                  partes = linha.split(",")
18                  if len(partes) != 5:
19                      continue
20                  usuarios.append({
21                      "id": int(partes[0]),
22                      "nome": partes[1],
23                      "email": partes[2],
24                      "senha": partes[3],
25                      "pontos": int(partes[4]),
26                  })
27      except FileNotFoundError:
28          return []
29      return usuarios
```

**Linha 18** — `if len(partes) != 5`. Aqui esperamos **5** pedaços (id, nome, email, senha, pontos), não 3 como no eletrônico. É a única diferença estrutural na leitura.

**Linhas 20-26** — O dicionário tem 5 campos. Note que `senha` (partes[3]) fica como texto, e só `id` e `pontos` viram número com `int()`.

O `_proximo_id()` (linhas 32-36) é idêntico ao do eletrônico, só muda o nome da variável (`usuarios` em vez de `eletronicos`).

#### A função nova: `_reescrever()`

```python
39  def _reescrever(usuarios):
40      # Reescreve o arquivo inteiro. Usado quando precisamos atualizar
41      # um registro existente (ex: creditar pontos).
42      with open(CAMINHO, "w", encoding="utf-8") as arquivo:
43          for u in usuarios:
44              arquivo.write(f"{u['id']},{u['nome']},{u['email']},{u['senha']},{u['pontos']}\n")
```

Por que esta função existe? Porque o modo `"a"` (anexar) só adiciona linhas novas — não dá pra usar pra **alterar** uma linha existente. Quando um usuário ganha pontos, precisamos reescrever o arquivo todo com o valor atualizado.

**Linha 42** — Abre o arquivo em modo `"w"` (*write*): isso **apaga todo o conteúdo** e começa do zero.

**Linhas 43-44** — Percorre a lista de usuários (já com os dados atualizados em memória) e regrava cada um. O resultado é o arquivo inteiro reescrito com os valores novos.

As funções `listar()`, `buscar_por_id()` e `buscar_por_email()` (linhas 47-63) seguem exatamente a mesma lógica das equivalentes do eletrônico. O `buscar_por_email` compara e-mails em minúsculas (`.lower()`) dos dois lados pra não diferenciar maiúsculas.

#### `salvar()` — note o ponto de partida dos pontos

```python
66  def salvar(nome, email, senha):
67      novo = {
68          "id": _proximo_id(),
69          "nome": nome,
70          "email": email,
71          "senha": senha,
72          "pontos": 0,
73      }
74      with open(CAMINHO, "a", encoding="utf-8") as arquivo:
75          arquivo.write(f"{novo['id']},{novo['nome']},{novo['email']},{novo['senha']},{novo['pontos']}\n")
76      return novo
```

**Linha 72** — `"pontos": 0`. Todo usuário novo começa com **zero** pontos. Os pontos só sobem depois, via descarte. O resto é igual ao `salvar` do eletrônico, só com mais campos.

#### `creditar_pontos()` — soma pontos e persiste

```python
79  def creditar_pontos(id_usuario, quantidade):
80      # Soma pontos ao saldo do usuario e reescreve o arquivo.
81      usuarios = _ler_linhas()
82      alvo = None
83      for u in usuarios:
84          if u["id"] == id_usuario:
85              u["pontos"] += quantidade
86              alvo = u
87              break
88      if alvo is not None:
89          _reescrever(usuarios)
90      return alvo
```

**Linha 81** — Lê todos os usuários pra uma lista em memória.

**Linha 82** — `alvo = None`. Cria uma variável pra guardar o usuário encontrado. Começa como `None` ("ainda não achei").

**Linha 83** — Percorre os usuários.

**Linha 84** — Quando acha o usuário com o ID certo...

**Linha 85** — `u["pontos"] += quantidade`. O `+=` significa "some isto ao valor atual". Equivale a `u["pontos"] = u["pontos"] + quantidade`. Como `u` é o dicionário dentro da lista `usuarios`, alterar `u` altera a lista também.

**Linha 86** — `alvo = u`. Guarda referência ao usuário alterado.

**Linha 87** — `break`. Encerra o loop imediatamente — já achamos quem queríamos, não precisa continuar procurando.

**Linha 88** — `if alvo is not None:`. Só reescreve o arquivo se de fato encontramos o usuário. O `is not None` verifica que a variável não é o "nada".

**Linha 89** — `_reescrever(usuarios)`. Grava a lista inteira (com os pontos atualizados) de volta no arquivo. Sem esta linha, o ponto subiria só na memória e se perderia quando o programa fechasse.

**Linha 90** — Devolve o usuário atualizado (ou `None`, se não encontrou).

---

### 3.3 `models/discard.py`

Guarda os descartes no formato `id,id_usuario,id_eletronico,quantidade,pontos_gerados,data_hora`. A novidade aqui é o uso de data e hora.

```python
6   from datetime import datetime
```

**Linha 6** — `from datetime import datetime`. Importa a ferramenta `datetime` (do módulo de mesmo nome), que vem junto com o Python e serve pra trabalhar com datas e horas. Usaremos pra carimbar o momento de cada descarte.

A função `_ler_linhas()` (linhas 11-32) é igual em espírito às anteriores; só muda que espera **6** pedaços por linha (linha 20) e monta um dicionário com 6 campos. Note na linha 28 que `data_hora` fica como texto — não convertemos pra número.

`_proximo_id()` (35-39) e `listar()` (42-43) são idênticos em lógica aos outros models.

#### `listar_por_usuario()` — filtra os descartes de uma pessoa

```python
46  def listar_por_usuario(id_usuario):
47      return [d for d in _ler_linhas() if d["id_usuario"] == id_usuario]
```

**Linha 47** — Uma list comprehension que devolve só os descartes cujo `id_usuario` bate com o informado. É assim que mostramos "meus descartes" sem misturar com os de outras pessoas.

#### `salvar()` — registra o descarte com data/hora

```python
50  def salvar(id_usuario, id_eletronico, quantidade, pontos_gerados):
51      agora = datetime.now().strftime("%d/%m/%Y %H:%M")
52      novo = {
53          "id": _proximo_id(),
54          "id_usuario": id_usuario,
55          "id_eletronico": id_eletronico,
56          "quantidade": quantidade,
57          "pontos_gerados": pontos_gerados,
58          "data_hora": agora,
59      }
60      with open(CAMINHO, "a", encoding="utf-8") as arquivo:
61          arquivo.write(
62              f"{novo['id']},{novo['id_usuario']},{novo['id_eletronico']},"
63              f"{novo['quantidade']},{novo['pontos_gerados']},{novo['data_hora']}\n"
64          )
65      return novo
```

**Linha 51** — `agora = datetime.now().strftime("%d/%m/%Y %H:%M")`. Duas etapas:
- `datetime.now()` pega o momento atual (data e hora completas).
- `.strftime("%d/%m/%Y %H:%M")` formata esse momento como texto legível. Os códigos significam: `%d` = dia, `%m` = mês, `%Y` = ano com 4 dígitos, `%H` = hora, `%M` = minuto. O resultado fica tipo `"10/06/2026 19:12"`.

**Linhas 52-59** — Monta o dicionário do descarte, com o ID automático e o carimbo de tempo.

**Linhas 60-64** — Grava no arquivo (modo `"a"`, anexar). Repare numa técnica de Python nas linhas 62-63: duas strings escritas uma embaixo da outra, sem operador entre elas, são automaticamente **coladas** numa só. Quebramos em duas linhas só pra não ficar uma linha gigante no editor; o conteúdo gravado é uma linha única no arquivo. O `\n` (só no final) garante a quebra de linha entre registros.

**Linha 65** — Devolve o descarte criado, pra view poder dizer "você ganhou X pontos".

---

## 4. Pasta `controllers/`

Os controllers ficam no meio: recebem dados já prontos da view, aplicam as regras (validações, cálculos) e chamam os models. **Não têm `input()` nem `print()`** — não falam com o usuário diretamente. Eles devolvem resultados pra view decidir o que mostrar.

Um padrão importante aqui é o retorno em **tupla `(sucesso, conteúdo)`**: a primeira posição é `True` ou `False` (deu certo?), e a segunda é o dado criado (se deu certo) ou a mensagem de erro (se não deu). A view lê esses dois valores e escolhe a mensagem.

### 4.1 `controllers/electronic_controller.py`

```python
6   from models import electronic
7
8
9   def listar_eletronicos():
10      return electronic.listar()
11
12
13  def buscar_por_id(id_busca):
14      return electronic.buscar_por_id(id_busca)
15
16
17  def buscar_por_nome(nome_busca):
18      return electronic.buscar_por_nome(nome_busca)
19
20
21  def cadastrar_eletronico(nome, pontos):
22      # Valida os dados antes de salvar.
23      # Retorna uma tupla (sucesso, resultado_ou_mensagem).
24      nome = nome.strip()
25      if not nome:
26          return (False, "O nome do eletronico nao pode ser vazio.")
27      if pontos <= 0:
28          return (False, "Os pontos devem ser um numero maior que zero.")
29      novo = electronic.salvar(nome, pontos)
30      return (True, novo)
```

**Linha 6** — `from models import electronic`. Importa o model de eletrônico. Daqui pra frente, `electronic.listar()` chama a função `listar` daquele arquivo.

**Linhas 9-18** — Três funções "de passagem": `listar_eletronicos`, `buscar_por_id` e `buscar_por_nome` só repassam a chamada pro model. Pode parecer redundante, mas mantém a regra arquitetural: a view sempre fala com o controller, nunca direto com o model. Se amanhã precisar de uma regra nessas operações (por exemplo, esconder eletrônicos inativos), o lugar certo já está pronto.

**Linha 21** — `cadastrar_eletronico(nome, pontos)`. Aqui mora a regra de verdade.

**Linha 24** — `nome = nome.strip()`. Tira espaços das pontas do nome digitado, pra que `"  "` (só espaços) seja detectado como vazio.

**Linhas 25-26** — `if not nome:`. Se o nome ficou vazio, devolve `(False, mensagem)` — operação recusada, com o motivo. Note: nenhum `print` aqui; só devolvemos a mensagem pra view exibir.

**Linhas 27-28** — `if pontos <= 0:`. Pontos têm que ser positivos. O `<=` significa "menor ou igual a". Se for zero ou negativo, recusa.

**Linha 29** — Se passou pelas validações, manda o model salvar.

**Linha 30** — `return (True, novo)`. Sucesso: devolve `True` e o eletrônico criado.

### 4.2 `controllers/user_controller.py`

```python
4   from models import user
7   def cadastrar_usuario(nome, email, senha):
8       nome = nome.strip()
9       email = email.strip()
10      if not nome:
11          return (False, "O nome nao pode ser vazio.")
12      if "@" not in email:
13          return (False, "E-mail invalido.")
14      if len(senha) < 3:
15          return (False, "A senha deve ter pelo menos 3 caracteres.")
16      if user.buscar_por_email(email) is not None:
17          return (False, "Ja existe um usuario com esse e-mail.")
18      novo = user.salvar(nome, email, senha)
19      return (True, novo)
```

**Linhas 8-9** — Limpa espaços das pontas do nome e do e-mail.

**Linhas 10-11** — Recusa se o nome estiver vazio.

**Linhas 12-13** — `if "@" not in email:`. Validação simples de e-mail: se não tiver um `@`, não é um e-mail válido. É uma checagem básica, não perfeita, mas suficiente pro projeto.

**Linhas 14-15** — `if len(senha) < 3:`. A senha precisa ter pelo menos 3 caracteres. `len()` conta o número de caracteres do texto.

**Linhas 16-17** — `if user.buscar_por_email(email) is not None:`. Pergunta ao model se já existe alguém com esse e-mail. Se a busca **não** devolveu `None`, significa que achou alguém — então o e-mail está em uso e recusamos. Isso evita dois usuários com o mesmo e-mail.

**Linhas 18-19** — Passou em tudo: salva e devolve sucesso.

```python
22  def login(email, senha):
23      encontrado = user.buscar_por_email(email)
24      if encontrado is None:
25          return (False, "Usuario nao encontrado.")
26      if encontrado["senha"] != senha:
27          return (False, "Senha incorreta.")
28      return (True, encontrado)
```

**Linha 23** — Busca o usuário pelo e-mail.

**Linhas 24-25** — Se não achou ninguém (`is None`), o login falha com "usuário não encontrado".

**Linhas 26-27** — Se achou, compara a senha guardada com a digitada. O `!=` é "diferente de". Se forem diferentes, recusa com "senha incorreta".

**Linha 28** — E-mail existe e senha bate: login aprovado, devolve o usuário (que a view vai usar pra montar a área logada).

```python
31  def consultar_saldo(id_usuario):
32      encontrado = user.buscar_por_id(id_usuario)
33      if encontrado is None:
34          return None
35      return encontrado["pontos"]
```

**Linhas 31-35** — Busca o usuário pelo ID e devolve só o número de pontos. Se não achar, devolve `None`. Buscamos de novo no arquivo (em vez de confiar no valor que a view já tem) pra garantir que o saldo mostrado seja o mais atual, inclusive depois de um descarte.

### 4.3 `controllers/discard_controller.py`

Este é o controller mais importante, porque ele **orquestra** três models ao mesmo tempo: verifica usuário e eletrônico, calcula pontos, registra o descarte e credita os pontos.

```python
6   from models import discard
7   from models import user
8   from models import electronic
9
10
11  def registrar_descarte(id_usuario, id_eletronico, quantidade):
12      # Valida tudo, calcula pontos e atualiza usuario.
13      # Retorna (sucesso, resultado_ou_mensagem).
14      if quantidade <= 0:
15          return (False, "A quantidade deve ser maior que zero.")
16
17      usuario = user.buscar_por_id(id_usuario)
18      if usuario is None:
19          return (False, "Usuario nao encontrado.")
20
21      eletronico = electronic.buscar_por_id(id_eletronico)
22      if eletronico is None:
23          return (False, "Eletronico nao encontrado.")
24
25      pontos_gerados = eletronico["pontos"] * quantidade
26
27      registro = discard.salvar(id_usuario, id_eletronico, quantidade, pontos_gerados)
28      user.creditar_pontos(id_usuario, pontos_gerados)
29
30      return (True, registro)
```

**Linhas 6-8** — Importa os **três** models, porque um descarte envolve as três entidades.

**Linhas 14-15** — Recusa quantidade zero ou negativa.

**Linhas 17-19** — Confere se o usuário existe. Se não, recusa. (É uma rede de segurança: o usuário deveria existir porque está logado, mas validamos mesmo assim.)

**Linhas 21-23** — Confere se o eletrônico escolhido existe. Se o usuário digitou um ID que não existe, recusa.

**Linha 25** — `pontos_gerados = eletronico["pontos"] * quantidade`. O cálculo central do sistema: pontos por unidade vezes a quantidade descartada. 2 iPhones de 40 pontos = 80 pontos. O `*` é multiplicação.

**Linha 27** — Pede ao model de descarte pra registrar a operação (com a data/hora gerada lá dentro).

**Linha 28** — Pede ao model de usuário pra somar os pontos no saldo. São **duas** ações em dois arquivos diferentes, coordenadas aqui pelo controller — é exatamente esse o papel de "orquestrar".

**Linha 30** — Devolve sucesso com o registro do descarte.

```python
33  def listar_descartes_do_usuario(id_usuario):
34      return discard.listar_por_usuario(id_usuario)
```

**Linhas 33-34** — Repassa pro model a busca dos descartes de um usuário específico.

---

## 5. Pasta `views/`

As views são a única camada que conversa com o usuário: usam `input()` pra perguntar e `print()` pra mostrar. Elas **não** têm regras de negócio nem mexem em arquivo — pra isso chamam os controllers. Todas usam o mesmo padrão de menu: um loop `while` que mostra opções e roteia a escolha.

### 5.1 `views/menu.py`

O menu principal, ponto de entrada da interface.

```python
5   from views.eletronics_page import navigate_electronics
6   from views.user_page import navigate_user
7
8
9   def startApp():
10      print("Bem-vindo ao programa E-descarte!")
11      print("Este programa ajuda a calcular o impacto ambiental do descarte de residuos eletronicos.")
12
13      rodando = True
14      while rodando:
15          print("\n--- Menu Principal ---")
16          print("[1] Area de eletronicos")
17          print("[2] Area do usuario (cadastro / login / descarte)")
18          print("[0] Sair")
19          escolha = input("Digite sua escolha: ").strip()
20
21          if escolha == "1":
22              navigate_electronics()
23          elif escolha == "2":
24              navigate_user()
25          elif escolha == "0":
26              print("Saindo do programa. Ate mais!")
27              rodando = False
28          else:
29              print("Opcao invalida. Por favor, tente novamente.")
```

**Linhas 5-6** — Importa as funções que abrem os submenus de eletrônicos e de usuário.

**Linhas 10-11** — Mensagens de boas-vindas, mostradas uma vez só (estão fora do loop).

**Linha 13** — `rodando = True`. Cria uma variável "interruptor" que controla o loop. Enquanto for `True`, o menu continua aparecendo.

**Linha 14** — `while rodando:`. "Enquanto `rodando` for verdadeiro, repita o bloco abaixo." É isto que faz o menu reaparecer depois de cada ação, em vez de o programa encerrar.

> **Por que `while` e não recursão?** A versão original chamava `startApp()` de novo dentro dela mesma a cada opção inválida. Isso empilha chamadas indefinidamente e pode estourar a memória ("stack overflow") se o usuário errar muitas vezes. O `while` repete sem empilhar nada — é a forma correta.

**Linha 15** — `print("\n--- Menu Principal ---")`. O `\n` no começo é uma quebra de linha, que dá um espaço em branco antes do título pra separar visualmente das mensagens anteriores.

**Linhas 16-18** — Mostra as opções disponíveis.

**Linha 19** — `escolha = input("Digite sua escolha: ").strip()`. O `input(...)` mostra o texto e espera o usuário digitar e apertar Enter; o que ele digitar fica guardado em `escolha`. O `.strip()` remove espaços acidentais das pontas, pra que `" 1 "` seja entendido como `"1"`.

**Linhas 21-22** — Se digitou "1", chama o submenu de eletrônicos. (Comparamos com `"1"` entre aspas porque o `input` sempre devolve texto, nunca número.)

**Linhas 23-24** — Se digitou "2", chama o submenu de usuário.

**Linhas 25-27** — Se digitou "0", mostra a despedida e faz `rodando = False`. Isso quebra a condição do `while`, e o loop termina na próxima verificação — encerrando o programa de forma limpa.

**Linhas 28-29** — `else:` — qualquer outra coisa digitada cai aqui e mostra "opção inválida". Como estamos num `while`, o menu simplesmente aparece de novo.

### 5.2 `views/eletronics_page.py`

Submenu de eletrônicos. Repare que toda a lógica de arquivo que existia aqui na versão original foi removida — agora a view só conversa com o usuário e chama o controller.

```python
5   from controllers import electronic_controller
8   def navigate_electronics():
9       rodando = True
10      while rodando:
11          print("\n--- Area de Eletronicos ---")
12          print("[1] Listar todos os eletronicos")
13          print("[2] Cadastrar novo eletronico")
14          print("[3] Buscar eletronico por ID")
15          print("[4] Buscar eletronico por nome")
16          print("[0] Voltar")
17          escolha = input("Digite sua escolha: ").strip()
18
19          if escolha == "1":
20              listar_eletronicos()
21          elif escolha == "2":
22              cadastrar_eletronico()
23          elif escolha == "3":
24              buscar_por_id()
25          elif escolha == "4":
26              buscar_por_nome()
27          elif escolha == "0":
28              rodando = False
29          else:
30              print("Opcao invalida. Tente novamente.")
```

**Linha 5** — Importa o controller de eletrônico.

**Linhas 8-30** — Mesma estrutura de menu com `while` do arquivo anterior. Cada opção chama uma função local (definidas logo abaixo) que cuida daquela tela. A opção "0" faz `rodando = False`, encerrando este submenu e voltando ao menu principal.

```python
33  def listar_eletronicos():
34      eletronicos = electronic_controller.listar_eletronicos()
35      if not eletronicos:
36          print("Nenhum eletronico cadastrado.")
37          return
38      print("\nEletronicos cadastrados:")
39      for e in eletronicos:
40          print(f"  [{e['id']}] {e['nome']} - {e['pontos']} pontos/unidade")
```

**Linha 34** — Pede a lista ao controller (que pede ao model).

**Linhas 35-37** — Se a lista estiver vazia, avisa e usa `return` pra sair da função imediatamente (não faz sentido tentar listar nada).

**Linha 38** — Título da listagem.

**Linhas 39-40** — Percorre cada eletrônico e o imprime formatado. A f-string monta uma linha tipo `  [1] iPhone 13 - 40 pontos/unidade`.

```python
43  def cadastrar_eletronico():
44      nome = input("Nome do eletronico: ")
45      try:
46          pontos = int(input("Pontos gerados por unidade: "))
47      except ValueError:
48          print("Pontos deve ser um numero inteiro.")
49          return
50
51      sucesso, resultado = electronic_controller.cadastrar_eletronico(nome, pontos)
52      if sucesso:
53          print(f"Eletronico cadastrado com sucesso! ID {resultado['id']}.")
54      else:
55          print(f"Erro: {resultado}")
```

**Linha 44** — Pergunta o nome.

**Linhas 45-49** — Pergunta os pontos e tenta convertê-los pra número com `int(...)`. Se o usuário digitar algo que não é número (tipo "abc"), o `int()` dispara um `ValueError`, capturado pelo `except` na linha 47, que avisa o erro e sai com `return`. Isso evita que o programa quebre por uma digitação errada.

**Linha 51** — `sucesso, resultado = ...`. Chama o controller e **desempacota** a tupla devolvida em duas variáveis de uma vez: `sucesso` recebe o `True`/`False`, e `resultado` recebe o eletrônico criado ou a mensagem de erro.

**Linhas 52-55** — Se deu certo, mostra o ID criado; senão, mostra a mensagem de erro que veio do controller. É aqui que a separação fica clara: o controller **decidiu** se deu certo; a view só **mostra** o resultado.

```python
58  def buscar_por_id():
59      try:
60          id_busca = int(input("ID do eletronico: "))
61      except ValueError:
62          print("ID deve ser um numero inteiro.")
63          return
64      e = electronic_controller.buscar_por_id(id_busca)
65      if e is None:
66          print("Eletronico nao encontrado.")
67      else:
68          print(f"  [{e['id']}] {e['nome']} - {e['pontos']} pontos/unidade")
```

**Linhas 59-63** — Pede o ID e converte pra número, com a mesma proteção `try/except` contra texto inválido.

**Linha 64** — Busca via controller.

**Linhas 65-68** — Se voltou `None`, não achou; senão, mostra o eletrônico encontrado.

```python
71  def buscar_por_nome():
72      nome_busca = input("Nome (ou parte do nome): ")
73      resultados = electronic_controller.buscar_por_nome(nome_busca)
74      if not resultados:
75          print("Nenhum eletronico encontrado.")
76          return
77      print("\nResultados:")
78      for e in resultados:
79          print(f"  [{e['id']}] {e['nome']} - {e['pontos']} pontos/unidade")
```

**Linha 72** — Pede o texto de busca (não precisa de `int`, pois é texto).

**Linha 73** — Busca via controller, que pode devolver vários resultados.

**Linhas 74-79** — Se a lista veio vazia, avisa; senão, imprime cada resultado, igual à listagem.

### 5.3 `views/user_page.py`

Cuida de cadastro, login e da "área logada" — o menu que aparece depois que o usuário entra.

```python
4   from controllers import user_controller
5   from views import discard_page
8   def navigate_user():
9       rodando = True
10      while rodando:
11          print("\n--- Area do Usuario ---")
12          print("[1] Cadastrar")
13          print("[2] Fazer login")
14          print("[0] Voltar")
15          escolha = input("Digite sua escolha: ").strip()
16
17          if escolha == "1":
18              cadastrar()
19          elif escolha == "2":
20              usuario = fazer_login()
21              if usuario is not None:
22                  area_logada(usuario)
23          elif escolha == "0":
24              rodando = False
25          else:
26              print("Opcao invalida. Tente novamente.")
```

**Linha 4** — Importa o controller de usuário.

**Linha 5** — Importa a view de descarte, porque a área logada vai oferecer "registrar descarte" e "ver descartes", que ficam naquele arquivo.

**Linhas 8-26** — Menu com `while`, igual em estrutura aos outros. A parte interessante:

**Linhas 19-22** — Quando o usuário escolhe login: `fazer_login()` devolve o usuário (se deu certo) ou `None` (se falhou). A linha 21 verifica: **só** se o login funcionou (`usuario is not None`), abrimos a área logada passando esse usuário. Se falhou, o menu simplesmente reaparece.

```python
29  def cadastrar():
30      nome = input("Nome: ")
31      email = input("E-mail: ")
32      senha = input("Senha: ")
33      sucesso, resultado = user_controller.cadastrar_usuario(nome, email, senha)
34      if sucesso:
35          print(f"Usuario cadastrado com sucesso! ID {resultado['id']}.")
36      else:
37          print(f"Erro: {resultado}")
```

**Linhas 30-32** — Coleta os três dados.

**Linha 33** — Manda pro controller, que valida tudo, e desempacota a resposta.

**Linhas 34-37** — Mostra sucesso (com ID) ou o erro que o controller devolveu (e-mail repetido, senha curta etc.).

```python
40  def fazer_login():
41      email = input("E-mail: ")
42      senha = input("Senha: ")
43      sucesso, resultado = user_controller.login(email, senha)
44      if sucesso:
45          print(f"Bem-vindo(a), {resultado['nome']}!")
46          return resultado
47      print(f"Erro: {resultado}")
48      return None
```

**Linhas 41-43** — Coleta e-mail e senha e chama o controller de login.

**Linhas 44-46** — Se deu certo, dá as boas-vindas e **devolve o usuário** (`return resultado`) pra quem chamou (a função `navigate_user`, que vai usá-lo na área logada).

**Linhas 47-48** — Se chegou aqui, o login falhou (o `return` da linha 46 não foi alcançado). Mostra o erro e devolve `None`.

```python
51  def area_logada(usuario):
52      logado = True
53      while logado:
54          print(f"\n--- Logado como {usuario['nome']} ---")
55          print("[1] Consultar saldo de pontos")
56          print("[2] Registrar descarte")
57          print("[3] Ver meus descartes")
58          print("[0] Logout")
59          escolha = input("Digite sua escolha: ").strip()
60
61          if escolha == "1":
62              saldo = user_controller.consultar_saldo(usuario["id"])
63              print(f"Saldo atual: {saldo} pontos.")
64          elif escolha == "2":
65              discard_page.registrar_descarte(usuario)
66          elif escolha == "3":
67              discard_page.listar_meus_descartes(usuario)
68          elif escolha == "0":
69              logado = False
70          else:
71              print("Opcao invalida. Tente novamente.")
```

**Linha 51** — `area_logada(usuario)`. Recebe o usuário logado como parâmetro. Assim, todas as ações aqui dentro sabem quem é a pessoa.

**Linhas 52-53** — Outro loop `while`, controlado pela variável `logado`. Este é um menu "dentro" do anterior.

**Linha 54** — O título mostra o nome de quem está logado, usando `usuario['nome']`.

**Linhas 61-63** — Opção saldo: pede ao controller o saldo atual (passando o ID do usuário) e mostra. Buscar de novo garante que, se a pessoa acabou de fazer um descarte, o número esteja atualizado.

**Linhas 64-67** — Opções de descarte: delega pras funções da view de descarte, passando o usuário inteiro.

**Linhas 68-69** — Logout: faz `logado = False`, saindo da área logada e voltando ao menu de usuário. O usuário continua existindo no arquivo; só encerramos a "sessão" na tela.

### 5.4 `views/discard_page.py`

As telas de descarte. Recebem sempre o usuário logado como parâmetro (vindo da área logada).

```python
5   from controllers import discard_controller
6   from controllers import electronic_controller
9   def registrar_descarte(usuario):
10      # Mostra os eletronicos disponiveis para o usuario escolher.
11      eletronicos = electronic_controller.listar_eletronicos()
12      if not eletronicos:
13          print("Nenhum eletronico cadastrado para descartar.")
14          return
15
16      print("\nEletronicos disponiveis:")
17      for e in eletronicos:
18          print(f"  [{e['id']}] {e['nome']} - {e['pontos']} pontos/unidade")
19
20      try:
21          id_eletronico = int(input("ID do eletronico a descartar: "))
22          quantidade = int(input("Quantidade: "))
23      except ValueError:
24          print("ID e quantidade devem ser numeros inteiros.")
25          return
26
27      sucesso, resultado = discard_controller.registrar_descarte(
28          usuario["id"], id_eletronico, quantidade
29      )
30      if sucesso:
31          print(f"Descarte registrado! Voce ganhou {resultado['pontos_gerados']} pontos.")
32      else:
33          print(f"Erro: {resultado}")
```

**Linhas 5-6** — Importa **dois** controllers: o de descarte (pra registrar) e o de eletrônico (pra mostrar a lista de opções antes de escolher).

**Linha 9** — `registrar_descarte(usuario)`. Recebe o usuário logado.

**Linhas 11-14** — Antes de tudo, mostra os eletrônicos existentes. Se não houver nenhum, não dá pra descartar — avisa e sai.

**Linhas 16-18** — Lista os eletrônicos disponíveis com seus IDs, pra o usuário saber qual número digitar.

**Linhas 20-25** — Pede o ID do eletrônico e a quantidade, convertendo ambos pra número dentro de um `try`. Repare que duas conversões ficam no mesmo bloco: se qualquer uma falhar (texto inválido), o `except` pega e sai. O Enter de cada `input` separa as duas perguntas.

**Linhas 27-29** — Chama o controller de descarte passando três coisas: o ID do usuário logado (`usuario["id"]`), o ID do eletrônico e a quantidade. A chamada está quebrada em várias linhas só por legibilidade.

**Linhas 30-33** — Mostra o resultado: se deu certo, informa quantos pontos foram ganhos (lendo `resultado['pontos_gerados']`); senão, mostra o erro.

```python
36  def listar_meus_descartes(usuario):
37      descartes = discard_controller.listar_descartes_do_usuario(usuario["id"])
38      if not descartes:
39          print("Voce ainda nao fez nenhum descarte.")
40          return
41      print("\nSeus descartes:")
42      for d in descartes:
43          eletronico = electronic_controller.buscar_por_id(d["id_eletronico"])
44          nome = eletronico["nome"] if eletronico else "?"
45          print(
46              f"  [{d['id']}] {d['quantidade']}x {nome} -> "
47              f"{d['pontos_gerados']} pontos ({d['data_hora']})"
48          )
```

**Linha 37** — Pede ao controller só os descartes deste usuário (passando o ID dele).

**Linhas 38-40** — Se não houver nenhum, avisa e sai.

**Linha 42** — Percorre cada descarte.

**Linha 43** — Para cada descarte, busca o eletrônico correspondente pelo ID. Por quê? Porque o descarte guarda só o `id_eletronico`, não o nome. Buscamos o nome pra deixar a tela legível ("2x iPhone 13" em vez de "2x eletrônico 1").

**Linha 44** — `nome = eletronico["nome"] if eletronico else "?"`. Isto é um *if* em formato de uma linha (operador ternário). Significa: "se `eletronico` existe, use o nome dele; senão, use `?`". A proteção cobre o caso raro de um eletrônico ter sido apagado depois que o descarte foi feito.

**Linhas 45-48** — Imprime o descarte formatado, de novo usando duas strings coladas: algo como `  [1] 2x iPhone 13 -> 80 pontos (10/06/2026 19:12)`. O `->` é só um enfeite visual entre o item e os pontos.

---

## 6. Pasta `data/` e os `__init__.py`

**`data/electronics.txt`, `data/users.txt`, `data/discard.txt`** — Não são código; são os arquivos de texto que funcionam como "banco de dados" do projeto. Cada linha é um registro, com os campos separados por vírgula. Por exemplo, `electronics.txt` começa com:

```
1,iPhone 13,40
2,Notebook Samsung,100
```

Os models leem e escrevem nesses arquivos. Eles persistem os dados entre execuções: o que você cadastrar continua lá quando fechar e reabrir o programa.

**`models/__init__.py`, `controllers/__init__.py`, `views/__init__.py`** — São arquivos **vazios**, mas a presença deles é o que faz o Python tratar cada pasta como um "pacote" importável. É por causa deles que `from models import electronic` funciona. Sem esses arquivos, os imports entre pastas quebrariam. Você não precisa escrever nada dentro deles.

---

## 7. O caminho completo de um descarte

Pra fechar, vale ver como todas as camadas conversam numa ação real. Imagine que o Tales, logado, descarta 2 iPhones (que valem 40 pontos cada):

1. **View (`user_page.area_logada`)** — Tales digita "2" (registrar descarte). A view chama `discard_page.registrar_descarte(usuario)`.

2. **View (`discard_page`)** — Mostra os eletrônicos, pergunta o ID (1) e a quantidade (2), converte pra número, e chama `discard_controller.registrar_descarte(1, 1, 2)` (id do usuário, id do eletrônico, quantidade).

3. **Controller (`discard_controller`)** — Valida a quantidade, confirma que o usuário existe (chamando `user.buscar_por_id`), confirma que o eletrônico existe (`electronic.buscar_por_id`), e calcula: `40 * 2 = 80` pontos.

4. **Model (`discard`)** — O controller chama `discard.salvar(...)`, que gera a data/hora, monta o registro e grava uma nova linha em `discard.txt`.

5. **Model (`user`)** — O controller chama `user.creditar_pontos(1, 80)`, que lê os usuários, soma 80 ao saldo do Tales e reescreve `users.txt`.

6. **De volta à View** — O controller devolve `(True, registro)`. A `discard_page` lê isso e imprime "Descarte registrado! Você ganhou 80 pontos."

Repare que a **view nunca tocou num arquivo** e o **model nunca falou com o Tales**. Cada camada fez só a sua parte, e o controller costurou tudo. É essa disciplina que torna o código fácil de entender, testar e mudar.

---

*Documento gerado para o projeto É-Descarte. Cada número de linha corresponde exatamente ao código nos arquivos do projeto.*