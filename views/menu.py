# views/menu.py
# Menu principal (View) - ponto de entrada da interface.
# Usa loop while (em vez de recursao) para nao estourar a pilha.

from views.eletronics_page import navigate_electronics
from views.user_page import navigate_user


def startApp():
    print("Bem-vindo ao programa E-descarte!")
    print("Este programa ajuda a calcular o impacto ambiental do descarte de residuos eletronicos.")

    rodando = True
    while rodando:
        print("\n--- Menu Principal ---")
        print("[1] Area de eletronicos")
        print("[2] Area do usuario (cadastro / login / descarte)")
        print("[0] Sair")
        escolha = input("Digite sua escolha: ").strip()

        if escolha == "1":
            navigate_electronics()
        elif escolha == "2":
            navigate_user()
        elif escolha == "0":
            print("Saindo do programa. Ate mais!")
            rodando = False
        else:
            print("Opcao invalida. Por favor, tente novamente.")
