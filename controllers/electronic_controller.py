# controllers/electronic_controller.py
# Camada de regra de negocio (Controller) de Eletronico.
# Recebe dados ja prontos da view, valida e chama o model.
# NAO contem input() nem print().

from models import electronic


def listar_eletronicos():
    return electronic.listar()


def buscar_por_id(id_busca):
    return electronic.buscar_por_id(id_busca)


def buscar_por_nome(nome_busca):
    return electronic.buscar_por_nome(nome_busca)


def cadastrar_eletronico(nome, pontos):
    # Valida os dados antes de salvar.
    # Retorna uma tupla (sucesso, resultado_ou_mensagem).
    nome = nome.strip()
    if not nome:
        return (False, "O nome do eletronico nao pode ser vazio.")
    if pontos <= 0:
        return (False, "Os pontos devem ser um numero maior que zero.")
    novo = electronic.salvar(nome, pontos)
    return (True, novo)
