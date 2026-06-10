from views.eletronics_page import navigateEletronics

def startApp():
    print("Bem-vindo ao programa E-descarte!")
    print("Este programa ajuda a calcular o impacto ambiental do descarte de resíduos eletrônicos.")
    print("Vamos começar! Digite 1 para navegar para a area de eletronicos; 2 para fazer login; 3 para sair.")
    userInput = str(input("Digite sua escolha: "))
    router(userInput)



def router(userInput):
    if userInput == "1":
        print("Você escolheu ir para a area de eletronicos.")
        # Navegar para a view de descarte eletronico
        navigateEletronics()
    elif userInput == "2":
        print("Você escolheu fazer login.")
        # Aqui você pode adicionar a lógica para o processo de login.
    elif userInput == "3":
        print("Saindo do programa. Até mais!")
        exit()
    else:
        print("Opção inválida. Por favor, tente novamente.")
        startApp()