# views/user_page.py
# Camada de interface (View) de Usuario: cadastro, login e area logada.

from controllers import user_controller
from views import discard_page


def navigate_user():
    rodando = True
    while rodando:
        print("\n--- Area do Usuario ---")
        print("[1] Cadastrar")
        print("[2] Fazer login")
        print("[0] Voltar")
        escolha = input("Digite sua escolha: ").strip()

        if escolha == "1":
            cadastrar()
        elif escolha == "2":
            usuario = fazer_login()
            if usuario is not None:
                area_logada(usuario)
        elif escolha == "0":
            rodando = False
        else:
            print("Opcao invalida. Tente novamente.")


def cadastrar():
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    sucesso, resultado = user_controller.cadastrar_usuario(nome, email, senha)
    if sucesso:
        print(f"Usuario cadastrado com sucesso! ID {resultado['id']}.")
    else:
        print(f"Erro: {resultado}")


def fazer_login():
    email = input("E-mail: ")
    senha = input("Senha: ")
    sucesso, resultado = user_controller.login(email, senha)
    if sucesso:
        print(f"Bem-vindo(a), {resultado['nome']}!")
        return resultado
    print(f"Erro: {resultado}")
    return None


def area_logada(usuario):
    logado = True
    while logado:
        print(f"\n--- Logado como {usuario['nome']} ---")
        print("[1] Consultar saldo de pontos")
        print("[2] Registrar descarte")
        print("[3] Ver meus descartes")
        print("[0] Logout")
        escolha = input("Digite sua escolha: ").strip()

        if escolha == "1":
            saldo = user_controller.consultar_saldo(usuario["id"])
            print(f"Saldo atual: {saldo} pontos.")
        elif escolha == "2":
            discard_page.registrar_descarte(usuario)
        elif escolha == "3":
            discard_page.listar_meus_descartes(usuario)
        elif escolha == "0":
            logado = False
        else:
            print("Opcao invalida. Tente novamente.")
