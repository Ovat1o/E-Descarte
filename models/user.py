# models/user.py
# Camada de dados (Model) da entidade Usuario.
# Responsabilidade: ler e escrever em data/users.txt.
# Formato de cada linha: id,nome,email,senha,pontos

CAMINHO = "./data/users.txt"


def _ler_linhas():
    usuarios = []
    try:
        with open(CAMINHO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(",")
                if len(partes) != 5:
                    continue
                usuarios.append({
                    "id": int(partes[0]),
                    "nome": partes[1],
                    "email": partes[2],
                    "senha": partes[3],
                    "pontos": int(partes[4]),
                })
    except FileNotFoundError:
        return []
    return usuarios


def _proximo_id():
    usuarios = _ler_linhas()
    if not usuarios:
        return 1
    return max(u["id"] for u in usuarios) + 1


def _reescrever(usuarios):
    # Reescreve o arquivo inteiro. Usado quando precisamos atualizar
    # um registro existente (ex: creditar pontos).
    with open(CAMINHO, "w", encoding="utf-8") as arquivo:
        for u in usuarios:
            arquivo.write(f"{u['id']},{u['nome']},{u['email']},{u['senha']},{u['pontos']}\n")


def listar():
    return _ler_linhas()


def buscar_por_id(id_busca):
    for u in _ler_linhas():
        if u["id"] == id_busca:
            return u
    return None


def buscar_por_email(email_busca):
    email_busca = email_busca.lower()
    for u in _ler_linhas():
        if u["email"].lower() == email_busca:
            return u
    return None


def salvar(nome, email, senha):
    novo = {
        "id": _proximo_id(),
        "nome": nome,
        "email": email,
        "senha": senha,
        "pontos": 0,
    }
    with open(CAMINHO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{novo['id']},{novo['nome']},{novo['email']},{novo['senha']},{novo['pontos']}\n")
    return novo


def creditar_pontos(id_usuario, quantidade):
    # Soma pontos ao saldo do usuario e reescreve o arquivo.
    usuarios = _ler_linhas()
    alvo = None
    for u in usuarios:
        if u["id"] == id_usuario:
            u["pontos"] += quantidade
            alvo = u
            break
    if alvo is not None:
        _reescrever(usuarios)
    return alvo
