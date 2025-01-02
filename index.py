import os
import time
from cadastro import cadastroSubMenu  # Submenu de cadastro importado corretamente
from consulta import consultar
from matricula import matricular_aluno
from administracao import administracao_menu

# Função para exibir a mensagem inicial
def startSchool_message():
    print("""
    ░██████╗░█████╗░██╗░░██╗░█████╗░░█████╗░██╗░░░░░  ░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗
    ██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░░░░░  ██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║1
    ╚█████╗░██║░░╚═╝███████║██║░░██║██║░░██║██║░░░░░  ╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║
    ░╚═══██╗██║░░██╗██╔══██║██║░░██║██║░░██║██║░░░░░  ░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║
    ██████╔╝╚█████╔╝██║░░██║╚█████╔╝╚█████╔╝███████╗  ██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║
    ╚═════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝  ╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝
    """)
    time.sleep(1.5)  # Aguarda 1.5 segundos
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela

# Função para encerrar o programa
def endProgram():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Sessão encerrada.")
    exit()

# Menu principal
def selectOption():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela ao exibir o menu principal
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastro")
        print("2 - Consultar Informações")
        print("3 - Matrículas")
        print("4 - Administração")
        print("5 - Sair")

        try:
            mode = int(input("Selecione uma opção: ").strip())
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela imediatamente após a escolha

            match mode:
                case 1:
                    cadastroSubMenu()  # Chama o submenu de cadastro
                case 2:
                    consultar()  # Consultar informações
                case 3:
                    matricular_aluno()  # Matrícula
                case 4:
                    administracao_menu()  # Administração
                case 5:
                    endProgram()  # Finaliza o programa
                case _:
                    print("Opção inválida! Por favor, tente novamente.")
                    input("Pressione Enter para continuar...")
                    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela após mensagem de erro
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela após mensagem de erro



# Início do programa
if __name__ == "__main__":
    startSchool_message()
    selectOption()
