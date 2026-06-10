from models import user 

def cadastrar_usuario(nome, email, senha):
    nome = nome.strip()
    email = email.strip()
    if not nome:
        return(False, "O nome não pode ser vazio.")
    if "@" not in email:
        return(False, "E-mail invalido.")
    if len(senha) < 3:
        return(False, "A senha deve ter pelo menos 3 caracteres.")
    if user.buscar_por_email(email) is not None:
        return(False, "Já existe um usuário com esse e-mail.")
    novo = user.salvar(nome, email, senha)
    return (True, novo)

def login(email, senha):
    encontrado = user.buscar_por_email(email)
    if encontrado is None:
        return (False, "Usuário não encontrado.")
    if encontrado["senha"] != senha:
        return (False, "Senha incorreta.")
    return (True, encontrado)

def consultar_saldo(id_usuario):
    encontrado = user.buscar_por_id(id_usuario)
    if encontrado is None:
        return None
    return encontrado ["pontos"]