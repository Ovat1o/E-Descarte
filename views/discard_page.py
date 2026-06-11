# views/discard_page.py
# Camada de interface (View) de Descarte.
# Recebe o usuario ja logado (vindo de user_page) para registrar o descarte.

from controllers import discard_controller
from controllers import electronic_controller


def registrar_descarte(usuario):
    # Mostra os eletronicos disponiveis para o usuario escolher.
    eletronicos = electronic_controller.listar_eletronicos()
    if not eletronicos:
        print("Nenhum eletronico cadastrado para descartar.")
        return

    print("\nEletronicos disponiveis:")
    for e in eletronicos:
        print(f"  [{e['id']}] {e['nome']} - {e['pontos']} pontos/unidade")

    try:
        id_eletronico = int(input("ID do eletronico a descartar: "))
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("ID e quantidade devem ser numeros inteiros.")
        return

    sucesso, resultado = discard_controller.registrar_descarte(
        usuario["id"], id_eletronico, quantidade
    )
    if sucesso:
        print(f"Descarte registrado! Voce ganhou {resultado['pontos_gerados']} pontos.")
    else:
        print(f"Erro: {resultado}")


def listar_meus_descartes(usuario):
    descartes = discard_controller.listar_descartes_do_usuario(usuario["id"])
    if not descartes:
        print("Voce ainda nao fez nenhum descarte.")
        return
    print("\nSeus descartes:")
    for d in descartes:
        eletronico = electronic_controller.buscar_por_id(d["id_eletronico"])
        nome = eletronico["nome"] if eletronico else "?"
        print(
            f"  [{d['id']}] {d['quantidade']}x {nome} -> "
            f"{d['pontos_gerados']} pontos ({d['data_hora']})"
        )
