# É-Descarte — Documentação dos Módulos

---

## DATA

---

```
MÓDULO: Storage
Objetivo:
Armazenar todos os dados do sistema em listas de dicionários,
funcionando como o banco de dados da aplicação.
Funcionalidades:
1. Declarar as listas de cada entidade
2. Controlar a geração de IDs únicos
3. Popular o sistema com dados iniciais de teste
Exemplo:
usuarios      → lista de todos os usuários cadastrados
maquinas      → lista de todas as máquinas instaladas
descartes     → lista de todos os descartes realizados
recompensas   → lista de todos os prêmios disponíveis
estoque       → lista de prêmios por máquina
Aplicar:
- Listas
- Dicionários
- Funções
```

---

## REPOSITORIES

---

```
MÓDULO: usuario_repo
Objetivo:
Gerenciar os dados dos usuários do aplicativo.
Funcionalidades:
1. Criar usuário
2. Informar:
   - Nome
   - E-mail
   - CPF
   - Senha
   - Pontos acumulados
3. Buscar usuário por ID
4. Buscar usuário por e-mail
5. Buscar usuário por CPF
6. Listar todos os usuários ativos
7. Atualizar dados do usuário
8. Adicionar pontos ao saldo
9. Subtrair pontos do saldo
10. Desativar usuário (soft delete)
Exemplo:
Tales  → 200 pontos
Helo   → 80 pontos
Aplicar:
- Listas
- Dicionários
- Funções
- For (dentro do next())
- If / Else
```

---

```
MÓDULO: maquina_repo
Objetivo:
Gerenciar as máquinas de descarte instaladas nos pontos da cidade.
Funcionalidades:
1. Cadastrar máquina
2. Informar:
   - Código de identificação
   - Localização (nome do ponto)
   - Endereço completo
   - Status (ativa, inativa, manutenção)
   - Capacidade máxima
3. Buscar máquina por ID
4. Buscar máquina por código
5. Listar todas as máquinas
6. Listar apenas as máquinas ativas
7. Atualizar dados da máquina
8. Atualizar status da máquina
9. Desativar máquina
Exemplo:
MAQ-001 → Shopping RioMar    → ativa
MAQ-002 → Shopping Recife    → ativa
MAQ-003 → CESAR School       → ativa
MAQ-004 → Shopping Tacaruna  → inativa
Aplicar:
- Listas
- Dicionários
- Funções
- For (dentro do next())
- If / Else
- List comprehension
```

---

```
MÓDULO: tipo_eletronico_repo
Objetivo:
Gerenciar os tipos de resíduos eletrônicos aceitos pelas máquinas.
Funcionalidades:
1. Cadastrar tipo de eletrônico
2. Informar:
   - Nome do tipo
   - Pontos gerados por unidade
   - Descrição e condições de aceite
3. Buscar tipo por ID
4. Buscar tipo por nome
5. Listar todos os tipos
6. Listar apenas os tipos ativos
7. Atualizar tipo
8. Desativar tipo
Exemplo:
Celular   → 50 pontos por unidade
Tablet    → 80 pontos por unidade
Notebook  → 150 pontos por unidade
Fone      → 20 pontos por unidade
Cabo      → 10 pontos por unidade
Aplicar:
- Listas
- Dicionários
- Funções
- For (dentro do next())
- If / Else
- List comprehension
```

---

```
MÓDULO: recompensa_repo
Objetivo:
Gerenciar os prêmios que os usuários podem resgatar com seus pontos.
Funcionalidades:
1. Cadastrar recompensa
2. Informar:
   - Nome
   - Descrição
   - Custo em pontos
   - Categoria (snack, brinde, voucher)
3. Buscar recompensa por ID
4. Listar todas as recompensas
5. Listar recompensas ativas
6. Listar recompensas acessíveis pelo saldo do usuário
7. Atualizar recompensa
8. Desativar recompensa
Exemplo:
Pipoca        → 30 pontos  → snack
Refrigerante  → 50 pontos  → snack
Caixinha      → 100 pontos → brinde
Voucher 10%   → 200 pontos → voucher
Aplicar:
- Listas
- Dicionários
- Funções
- For (dentro do next())
- If / Else
- List comprehension
```

---

```
MÓDULO: estoque_repo
Objetivo:
Controlar a quantidade de cada recompensa disponível em cada máquina.
Funcionalidades:
1. Adicionar recompensa ao estoque de uma máquina
2. Informar:
   - ID da máquina
   - ID da recompensa
   - Quantidade disponível
3. Buscar item de estoque por máquina + recompensa
4. Listar estoque completo de uma máquina
5. Verificar se tem estoque disponível
6. Incrementar quantidade (abastecimento)
7. Decrementar quantidade (após resgate)
8. Remover recompensa do estoque de uma máquina
Exemplo:
MAQ-001 + Pipoca       → 20 unidades
MAQ-001 + Refrigerante → 15 unidades
MAQ-003 + Pipoca       → 30 unidades
MAQ-002 + Voucher 10%  → 5 unidades
Aplicar:
- Listas
- Dicionários
- Funções
- For (dentro do next())
- If / Else
- Operadores >= e +=  e -=
```

---

```
MÓDULO: descarte_repo
Objetivo:
Registrar cada ato de descarte realizado por um usuário em uma máquina.
Funcionalidades:
1. Registrar descarte
2. Informar:
   - Usuário responsável
   - Máquina utilizada
   - Tipo de eletrônico descartado
   - Quantidade descartada
   - Pontos gerados pela operação
   - Data e hora do descarte
   - Status (confirmado, cancelado)
3. Buscar descarte por ID
4. Listar todos os descartes
5. Listar descartes por usuário
6. Listar descartes por máquina
7. Cancelar descarte
Exemplo:
Tales  → MAQ-003 → 2 Celulares  → 100 pontos
Helo   → MAQ-001 → 1 Notebook   → 150 pontos
Aplicar:
- Listas
- Dicionários
- Funções
- For (dentro do next())
- If / Else
- List comprehension
- Módulo datetime
```

---

```
MÓDULO: resgate_repo
Objetivo:
Registrar cada troca de pontos por recompensa realizada pelo usuário.
Funcionalidades:
1. Registrar resgate
2. Informar:
   - Usuário que resgatou
   - Recompensa escolhida
   - Máquina onde foi retirada
   - Pontos utilizados na troca
   - Data e hora do resgate
   - Status (concluido, cancelado)
3. Buscar resgate por ID
4. Listar todos os resgates
5. Listar resgates por usuário
6. Cancelar resgate
Exemplo:
Tales  → Pipoca       → MAQ-003 → 30 pontos
Helo   → Refrigerante → MAQ-001 → 50 pontos
Aplicar:
- Listas
- Dicionários
- Funções
- For (dentro do next())
- If / Else
- List comprehension
- Módulo datetime
```

---

## SERVICES

---

```
MÓDULO: auth_service
Objetivo:
Gerenciar o cadastro e o login dos usuários no sistema.
Funcionalidades:
1. Cadastrar novo usuário
   - Validar se o e-mail já está em uso
   - Validar se o CPF já está em uso
   - Criar o usuário caso as validações passem
2. Realizar login
   - Buscar usuário pelo e-mail
   - Verificar se a senha confere
   - Retornar o usuário autenticado
Exemplo:
Cadastro → e-mail novo + CPF novo    → usuário criado
Cadastro → e-mail já cadastrado      → erro: e-mail em uso
Login    → e-mail + senha corretos   → acesso liberado
Login    → senha incorreta           → acesso negado
Aplicar:
- Funções
- If / Else
- Return com tupla (resultado, mensagem)
```

---

```
MÓDULO: descarte_service
Objetivo:
Orquestrar o registro de um descarte, aplicando todas as validações
e garantindo que os pontos sejam creditados corretamente.
Funcionalidades:
1. Validar se o usuário existe
2. Validar se a máquina está ativa
3. Validar se o tipo de eletrônico é aceito
4. Calcular os pontos gerados pelo descarte
5. Registrar o descarte via descarte_repo
6. Creditar os pontos no usuário via usuario_repo
7. Retornar o resultado e uma mensagem
Exemplo:
2 Celulares → 2 × 50 = 100 pontos creditados
1 Notebook  → 1 × 150 = 150 pontos creditados
Máquina inativa → operação bloqueada
Aplicar:
- Funções
- If / Else
- Multiplicação (*)
- Return com tupla (resultado, mensagem)
- Chamadas a múltiplos repositories
```

---

```
MÓDULO: resgate_service
Objetivo:
Orquestrar o resgate de uma recompensa, aplicando todas as validações
e garantindo que os pontos e o estoque sejam atualizados corretamente.
Funcionalidades:
1. Validar se o usuário existe
2. Validar se a máquina está ativa
3. Validar se a recompensa existe
4. Validar se o usuário tem pontos suficientes
5. Validar se há estoque disponível na máquina
6. Decrementar o estoque via estoque_repo
7. Debitar os pontos do usuário via usuario_repo
8. Registrar o resgate via resgate_repo
9. Retornar o resultado e uma mensagem
Exemplo:
200 pontos + Voucher disponível  → resgate concluído
80 pontos  + Voucher (200 pts)   → pontos insuficientes
Estoque zerado                   → recompensa indisponível
Aplicar:
- Funções
- If / Else
- Operador < (comparação de pontos)
- Return com tupla (resultado, mensagem)
- Chamadas a múltiplos repositories
```

---

## UTILS

---

```
MÓDULO: helpers
Objetivo:
Fornecer funções utilitárias reutilizáveis em qualquer parte do sistema.
Funcionalidades:
1. Limpar a tela do terminal
2. Exibir linha separadora
3. Exibir cabeçalho de seção
4. Capturar número inteiro com tratamento de erro
5. Confirmar ação com S/N
6. Pausar e aguardar o usuário pressionar Enter
Exemplo:
limpar_tela()          → apaga o terminal
separador()            → imprime "────────────────────"
cabecalho("Descartes") → imprime o título formatado
ler_inteiro("Opção: ") → garante que o input seja número
confirmar("Deseja sair?") → aguarda S ou N
Aplicar:
- Funções
- Import os
- Try / Except (ValueError)
- While
- If / Else
- f-strings
```

---

## VIEWS

---

```
MÓDULO: menu_principal
Objetivo:
Ser o ponto de entrada da interface, dando acesso ao menu do app
ou ao menu da máquina.
Funcionalidades:
1. Exibir as opções iniciais do sistema
2. Direcionar para o menu do app (usuário)
3. Direcionar para o menu da máquina (operador)
4. Encerrar o programa
Exemplo:
[1] Acessar como usuário
[2] Acessar como operador da máquina
[0] Sair
Aplicar:
- Funções
- While
- If / Elif / Else
- Input
- Print
- Break
```

---

```
MÓDULO: menu_app
Objetivo:
Interface completa do usuário do aplicativo — do cadastro até o resgate.
Funcionalidades:
1. Cadastrar novo usuário
2. Fazer login
3. Ver máquinas disponíveis
4. Ver tipos de eletrônicos e pontos por item
5. Registrar descarte
6. Consultar saldo de pontos
7. Ver recompensas disponíveis (filtradas pelo saldo)
8. Resgatar recompensa
9. Ver histórico de descartes
10. Ver histórico de resgates
11. Fazer logout
Exemplo:
Usuário faz login → escolhe "Registrar descarte" →
seleciona máquina + tipo + quantidade → pontos creditados
Usuário escolhe "Resgatar" → vê recompensas disponíveis
pelo seu saldo → confirma → prêmio dispensado
Aplicar:
- Funções
- While
- For
- If / Elif / Else
- Input
- Print
- Break
- Try / Except (ValueError)
- f-strings
- enumerate()
```

---

```
MÓDULO: menu_maquina
Objetivo:
Interface de operação da máquina física — identificação do usuário,
registro de descarte e dispensa de recompensas.
Funcionalidades:
1. Identificar usuário pelo CPF ou e-mail
2. Registrar descarte na máquina
3. Dispensar recompensa ao usuário
4. Consultar estoque atual da máquina
5. Exibir relatório de operações da máquina
6. Voltar ao menu principal
Exemplo:
Operador identifica usuário → seleciona tipo de eletrônico
→ informa quantidade → descarte registrado → pontos creditados
Usuário solicita resgate → operador seleciona recompensa
→ estoque decrementado → pontos debitados
Aplicar:
- Funções
- While
- For
- If / Elif / Else
- Input
- Print
- Break
- Try / Except (ValueError)
- f-strings
- enumerate()
```

---

## MAIN

---

```
MÓDULO: main
Objetivo:
Ser o ponto de entrada do programa — inicializar os dados e
abrir o menu principal.
Funcionalidades:
1. Chamar popular() para carregar os dados de teste
2. Chamar o menu principal para iniciar a aplicação
Aplicar:
- Import
- Chamada de funções
```