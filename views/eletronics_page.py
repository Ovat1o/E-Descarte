# views/eletronics_page.py
# Camada de interface (View) de Eletronico.
# So cuida de input() e print(). Chama o controller para a logica.

from controllers import electronic_controller


def navigate_electronics():
    rodando = True
    while rodando:
        print("\n--- Area de Eletronicos ---")
        print("[1] Listar todos os eletronicos")
        print("[2] Cadastrar novo eletronico")
        print("[3] Buscar eletronico por ID")
        print("[4] Buscar eletronico por nome")
        print("[0] Voltar")
        escolha = input("Digite sua escolha: ").strip()

        if escolha == "1":
            listar_eletronicos()
        elif escolha == "2":
            cadastrar_eletronico()
        elif escolha == "3":
            buscar_por_id()
        elif escolha == "4":
            buscar_por_nome()
        elif escolha == "0":
            rodando = False
        else:
            print("Opcao invalida. Tente novamente.")


def listar_eletronicos():
    eletronicos = electronic_controller.listar_eletronicos()
    if not eletronicos:
        print("Nenhum eletronico cadastrado.")
        return
    print("\nEletronicos cadastrados:")
    for e in eletronicos:
        print(f"  [{e['id']}] {e['nome']} - {e['pontos']} pontos/unidade")


def cadastrar_eletronico():
    nome = input("Nome do eletronico: ")
    try:
        pontos = int(input("Pontos gerados por unidade: "))
    except ValueError:
        print("Pontos deve ser um numero inteiro.")
        return

    sucesso, resultado = electronic_controller.cadastrar_eletronico(nome, pontos)
    if sucesso:
        print(f"Eletronico cadastrado com sucesso! ID {resultado['id']}.")
    else:
        print(f"Erro: {resultado}")


def buscar_por_id():
    try:
        id_busca = int(input("ID do eletronico: "))
    except ValueError:
        print("ID deve ser um numero inteiro.")
        return
    e = electronic_controller.buscar_por_id(id_busca)
    if e is None:
        print("Eletronico nao encontrado.")
    else:
        print(f"  [{e['id']}] {e['nome']} - {e['pontos']} pontos/unidade")


def buscar_por_nome():
    nome_busca = input("Nome (ou parte do nome): ")
    resultados = electronic_controller.buscar_por_nome(nome_busca)
    if not resultados:
        print("Nenhum eletronico encontrado.")
        return
    print("\nResultados:")
    for e in resultados:
        print(f"  [{e['id']}] {e['nome']} - {e['pontos']} pontos/unidade")
