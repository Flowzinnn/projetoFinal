import os
import time
from cadastro import registrationSubMenu
from consulta import consultationSubMenu
from matricula import enrollStudent
from administracao import administrationMenu

# Função para exibir a mensagem inicial
def startSchoolMessage():
    print("""
          
    ░██████╗░█████╗░██╗░░██╗░█████╗░░█████╗░██╗░░░░░  ░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗
    ██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░░░░░  ██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║
    ╚█████╗░██║░░╚═╝███████║██║░░██║██║░░██║██║░░░░░  ╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║
    ░╚═══██╗██║░░██╗██╔══██║██║░░██║██║░░██║██║░░░░░  ░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║
    ██████╔╝╚█████╔╝██║░░██║╚█████╔╝╚█████╔╝███████╗  ██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║
    ╚═════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝  ╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝
    
    """)
    time.sleep(1.5)  # Aguarda 1.5 segundos
    os.system('cls' if os.name == 'nt' else 'clear')  

# Função para encerrar o programa
def endProgram():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
    print("Sessão encerrada.")  # Mensagem de encerramento
    exit()  # Finaliza a execução do programa

# Menu principal
def selectOption():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastro")
        print("2 - Consultar Informações")
        print("3 - Matrículas")
        print("4 - Administração")
        print("5 - Sair")

        try:
            mode = int(input("Selecione uma opção: ").strip())  
            os.system('cls' if os.name == 'nt' else 'clear')  

            match mode:
                case 1:
                    registrationSubMenu()  # Chama o submenu de cadastro
                case 2:
                    consultationSubMenu()  # Chama o submenu de consultas
                case 3:
                    enrollStudent()  # Função de matrículas
                case 4:
                    administrationMenu()  # Chama o menu de administração
                case 5:
                    endProgram()  # Finaliza o programa
                case _:
                    print("Opção inválida! Por favor, tente novamente.")  
                    input("Pressione Enter para continuar...")
                    os.system('cls' if os.name == 'nt' else 'clear')  
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")  
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')  
            
# Início do programa
if __name__ == "__main__":
    startSchoolMessage()  
    selectOption()  
