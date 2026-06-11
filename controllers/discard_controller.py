# controllers/discard_controller.py
# Camada de regra de negocio (Controller) de Descarte.
# Orquestra usuario + eletronico: calcula pontos, registra o descarte
# e credita os pontos no usuario.

from models import discard
from models import user
from models import electronic


def registrar_descarte(id_usuario, id_eletronico, quantidade):
    # Valida tudo, calcula pontos e atualiza usuario.
    # Retorna (sucesso, resultado_ou_mensagem).
    if quantidade <= 0:
        return (False, "A quantidade deve ser maior que zero.")

    usuario = user.buscar_por_id(id_usuario)
    if usuario is None:
        return (False, "Usuario nao encontrado.")

    eletronico = electronic.buscar_por_id(id_eletronico)
    if eletronico is None:
        return (False, "Eletronico nao encontrado.")

    pontos_gerados = eletronico["pontos"] * quantidade

    registro = discard.salvar(id_usuario, id_eletronico, quantidade, pontos_gerados)
    user.creditar_pontos(id_usuario, pontos_gerados)

    return (True, registro)


def listar_descartes_do_usuario(id_usuario):
    return discard.listar_por_usuario(id_usuario)
