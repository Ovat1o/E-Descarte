def navigateElectronics():
    print("Navegando para a área de eletrônicos...")
    print("Selecione 1 para listar todos os eletronicos cadastrados; 2 para cadastrar um novo eletronico; 3 para buscar eletronico por ID; 4 para buscar eletronico por nome; 5 para encerrar.")
    userInput = str(input("Digite sua escolha: "))
    router(userInput)

def router(userInput):
    if userInput == "1":
        print("Você escolheu listar todos os eletronicos cadastrados.")
        listAllElectronics()
        # Aqui você pode adicionar a lógica para listar todos os eletronicos cadastrados.
    elif userInput == "2":
        print("Você escolheu cadastrar um novo eletronico.")
        # Aqui você pode adicionar a lógica para cadastrar um novo eletronico.
        addElectronic()
    elif userInput == "3":
        print("Você escolheu buscar eletronico por ID.")
        # Aqui você pode adicionar a lógica para buscar eletronico por ID.
    elif userInput == "4":
        print("Você escolheu buscar eletronico por nome.")
        # Aqui você pode adicionar a lógica para buscar eletronico por nome.
    elif userInput == "5":
        print("Você escolheu encerrar.")
        # Aqui você pode adicionar a lógica para encerrar.

def listAllElectronics():
    print("Listando todos os eletronicos cadastrados...")
    # Aqui você pode adicionar a lógica para listar todos os eletronicos cadastrados.

def addElectronic():
    print("Cadastrando um novo eletronico...")
    # Aqui você pode adicionar a lógica para cadastrar um novo eletronico.

    addedElectronics = []
    addingElectronic = True
    while addingElectronic:
        name = input("Digite o nome do eletronico: ")
        points = input("Digite os pontos gerados por unidade: ")
        # Aqui você pode adicionar a lógica para salvar o novo eletronico.
        addedElectronics.append((name, points))


        continueAdding = input("Deseja cadastrar outro eletronico? (sim/não): ")
        if continueAdding.lower() != 'sim':
            addingElectronic = False
        addEletronicsToFile(addedElectronics)

def addEletronicsToFile(addedElectronics):
    with open("./data/electronics.txt", "a") as file:
        for eletronico in addedElectronics:
            file.write(f"{eletronico[0]},{eletronico[1]}\n")

