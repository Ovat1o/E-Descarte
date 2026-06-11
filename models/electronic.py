# models/electronic.py
# Camada de dados (Model) da entidade Eletronico.
# Responsabilidade: ler e escrever em data/electronics.txt.
# NAO contem input() nem regras de negocio - so persistencia.

CAMINHO = "./data/electronics.txt"


def _ler_linhas():
    # Le o arquivo e devolve uma lista de dicionarios.
    # Formato de cada linha: id,nome,pontos
    eletronicos = []
    try:
        with open(CAMINHO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(",")
                if len(partes) != 3:
                    continue  # ignora linhas mal formatadas
                eletronicos.append({
                    "id": int(partes[0]),
                    "nome": partes[1],
                    "pontos": int(partes[2]),
                })
    except FileNotFoundError:
        # se o arquivo nao existe ainda, retorna lista vazia
        return []
    return eletronicos


def _proximo_id():
    # Gera o proximo ID com base no maior ID existente.
    eletronicos = _ler_linhas()
    if not eletronicos:
        return 1
    return max(e["id"] for e in eletronicos) + 1


def listar():
    # Devolve todos os eletronicos cadastrados.
    return _ler_linhas()


def buscar_por_id(id_busca):
    # Devolve o eletronico com o ID informado, ou None.
    for e in _ler_linhas():
        if e["id"] == id_busca:
            return e
    return None


def buscar_por_nome(nome_busca):
    # Devolve uma lista de eletronicos cujo nome contem o texto buscado.
    nome_busca = nome_busca.lower()
    return [e for e in _ler_linhas() if nome_busca in e["nome"].lower()]


def salvar(nome, pontos):
    # Cria um novo eletronico, gera o ID e grava no arquivo.
    novo = {"id": _proximo_id(), "nome": nome, "pontos": pontos}
    with open(CAMINHO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{novo['id']},{novo['nome']},{novo['pontos']}\n")
    return novo
