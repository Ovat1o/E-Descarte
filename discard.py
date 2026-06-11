# models/discard.py
# Camada de dados (Model) da entidade Descarte.
# Responsabilidade: ler e escrever em data/discard.txt.
# Formato de cada linha: id,id_usuario,id_eletronico,quantidade,pontos_gerados,data_hora

from datetime import datetime

CAMINHO = "./data/discard.txt"


def _ler_linhas():
    descartes = []
    try:
        with open(CAMINHO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(",")
                if len(partes) != 6:
                    continue
                descartes.append({
                    "id": int(partes[0]),
                    "id_usuario": int(partes[1]),
                    "id_eletronico": int(partes[2]),
                    "quantidade": int(partes[3]),
                    "pontos_gerados": int(partes[4]),
                    "data_hora": partes[5],
                })
    except FileNotFoundError:
        return []
    return descartes


def _proximo_id():
    descartes = _ler_linhas()
    if not descartes:
        return 1
    return max(d["id"] for d in descartes) + 1


def listar():
    return _ler_linhas()


def listar_por_usuario(id_usuario):
    return [d for d in _ler_linhas() if d["id_usuario"] == id_usuario]


def salvar(id_usuario, id_eletronico, quantidade, pontos_gerados):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    novo = {
        "id": _proximo_id(),
        "id_usuario": id_usuario,
        "id_eletronico": id_eletronico,
        "quantidade": quantidade,
        "pontos_gerados": pontos_gerados,
        "data_hora": agora,
    }
    with open(CAMINHO, "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{novo['id']},{novo['id_usuario']},{novo['id_eletronico']},"
            f"{novo['quantidade']},{novo['pontos_gerados']},{novo['data_hora']}\n"
        )
    return novo
