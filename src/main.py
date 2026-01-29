from menus import cadastrar, listar, buscar

def menu():
    """Exibe o menu principal e chama as funções apropriadas com base na escolha do usuário."""

    while True:
        print("Menu Principal")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Buscar")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
    
        if escolha == "1":
            cadastrar()
        elif escolha == "2":
            listar()
        elif escolha == "3":
            buscar()
        elif escolha == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida.")       
              
menu()