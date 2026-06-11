# E-descarte

O **E-descarte** é uma aplicação de linha de comando (CLI) desenvolvida em Python que visa incentivar e calcular o impacto ambiental do descarte de resíduos eletrônicos. Através de um sistema gamificado de pontuação, os usuários podem registrar os eletrônicos descartados e acumular pontos.

O projeto foi construído utilizando a arquitetura **MVC (Model-View-Controller)** para garantir a separação de responsabilidades e facilitar a manutenção do código.

---

## Funcionalidades

* **Gestão de Usuários:** Cadastro, login e consulta de saldo de pontos.
* **Catálogo de Eletrônicos:** Listagem, busca (por ID ou nome) e cadastro de novos tipos de eletrônicos, incluindo a definição de quantos pontos cada unidade gera ao ser descartada.
* **Registro de Descartes:** Permite que usuários logados registrem o descarte de eletrônicos, calculando e creditando automaticamente os pontos gerados em suas contas.
* **Histórico:** Visualização de todos os descartes realizados pelo usuário logado, incluindo data e hora.

---

## Arquitetura do Projeto

O sistema está dividido em três camadas principais (MVC), além de seu arquivo de entrada principal (`main.py`):

### 1. Models (`/models`)
Responsáveis pela camada de dados e persistência. O armazenamento é feito em arquivos de texto simples (`.txt`) localizados na pasta `data/`.
* `user.py`: Gerencia leitura, gravação, busca e atualização de saldo no arquivo `users.txt`.
* `electronic.py`: Gerencia leitura, gravação e busca no arquivo `electronics.txt`.
* `discard.py`: Registra o histórico de transações de descarte no arquivo `discard.txt`.

### 2. Controllers (`/controllers`)
Contêm as regras de negócio do sistema. Recebem os dados das *Views*, realizam as validações necessárias (ex: senhas curtas, e-mails inválidos, quantidades nulas) e se comunicam com os *Models*.
* `user_controller.py`: Lida com autenticação e validação de cadastro.
* `electronic_controller.py`: Valida o cadastro e coordena as buscas de eletrônicos.
* `discard_controller.py`: Orquestra a transação de descarte, garantindo que o eletrônico existe e atualizando os pontos do usuário corretamente.

### 3. Views (`/views`)
Camada de interface com o usuário (CLI). Lida exclusivamente com entradas (`input()`) e saídas (`print()`), sem conter lógica de negócios.
* `menu.py`: Ponto de entrada da interface, direcionando para as áreas de Eletrônicos ou Usuário.
* `user_page.py`: Menus de cadastro, login e área logada.
* `eletronics_page.py`: Menus de navegação, listagem e busca do catálogo de eletrônicos.
* `discard_page.py`: Telas para realizar um novo descarte e listar o histórico.

---

## Estrutura de Diretórios

```text
├── .gitignore           # Ignora arquivos desnecessários no Git (ex: __pycache__, .venv)
├── main.py              # Ponto de entrada (Entry point) da aplicação
├── controllers/
│   ├── discard_controller.py
│   ├── electronic_controller.py
│   └── user_controller.py
├── data/
│   ├── discard.txt      # (Gerado automaticamente)
│   ├── electronics.txt  # (Gerado automaticamente)
│   └── users.txt        # (Gerado automaticamente)
├── models/
│   ├── discard.py
│   ├── electronic.py
│   └── user.py
└── views/
    ├── discard_page.py
    ├── eletronics_page.py
    ├── menu.py
    └── user_page.py
```

---

## Como Executar

### Pré-requisitos
* Python 3.x instalado em sua máquina.

### Passos para rodar
1. Clone o repositório ou baixe os arquivos fonte.
2. Certifique-se de que a pasta `data/` existe na raiz do projeto. Caso não exista, crie-a, pois os *Models* precisarão desse diretório para gravar os arquivos `.txt`.
    ```bash
    mkdir data
    ```
3. Execute o programa através do arquivo principal (`main.py`):
    ```bash
    python main.py
    ```

---

## Controle de Versão (.gitignore)
O projeto acompanha um arquivo `.gitignore` abrangente configurado para evitar o versionamento indevido de:
* Arquivos compilados do Python (`__pycache__/`, `*.pyc`).
* Ambientes virtuais (`.venv`, `env/`, `venv/`).
* Arquivos temporários e configurações locais de IDEs (`.vscode/`, `.idea/`).
* Logs e artefatos de testes (`.pytest_cache/`, `htmlcov/`).
