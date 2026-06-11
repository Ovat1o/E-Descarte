CAMINHO = "./data/electronics.txt" #Está em maiúscula por ser uma constante


def _ler_linhas():
    #Lê o arquivo e devolve uma lista de dicionarios.
    #Formato de cada linha: id,nome,pontos

    eletronicos = [] #Cria lista vazia, que vai sendo preenchida

    try: #Inicia tratamento de exceção
        with open(CAMINHO, "r", encoding="utf-8") as arquivo: #Abre o arquivo no modo leitura ("r")
            for linha in arquivo: #Percorre o arquivo linha por linha
                linha = linha.strip() #Remove os espaços e caracteres em branco
                if not linha: #Se depois do strip a linha ficou vazia (era uma linha em branco)
                    continue
                partes = linha.split(",")
                if len(partes) != 3: #O len() conta quantos itens há na lista. Se não houver exatamente 3 pedaços, a linha está malformada
                    continue #Então pulamos
                eletronicos.append({ #Monta um dicionário e adiciona a lista
                    "id": int(partes[0]), #Converte ID para inteiro
                    "nome": partes[1], #Não há mudanças
                    "pontos": int(partes[2]), #Converte Pontos para inteiro
                }) #Resultado: a linha vira o dicionário Ex: "1,iPhone 13,40" vira {"id": 1, "nome": "iPhone 13", "pontos": 40}
    except FileNotFoundError:
        #Se o arquivo nao existe ainda, retorna lista vazia
        return [] #Em vez do código quebrar, a função devolve lista vazia
    return eletronicos #Devolve lista completa de dicionários, só roda se a leitura der certo


def _proximo_id(): 
    #Objetivo: gerar o proximo ID com base no maior ID existente
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
