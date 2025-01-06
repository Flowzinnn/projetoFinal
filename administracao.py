import os
from alocar_professores import allocateProfessors
from filtrar_professores import filterProfessors
from adicionar_disciplinas_turma import addSubjectsToClass

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def administrationMenu():
    while True:
        clearScreen()
        print("\n=== MENU DE ADMINISTRAÇÃO ===")
        print("1 - Alocação de Professores")
        print("2 - Filtrar Professores por Matéria")
        print("3 - Adicionar Disciplinas em Turma")
        print("4 - Voltar ao Menu Principal")

        try:
            mode = int(input("Selecione uma opção: ").strip())
            clearScreen()
            match mode:
                case 1:  # Alocação de Professores
                    allocateProfessors()
                case 2:  # Filtrar Professores por Matéria
                    filterProfessors()
                case 3:  # Adicionar Disciplinas em Turma
                    addSubjectsToClass()
                case 4:  # Voltar ao Menu Principal
                    break
                case _:
                    print("Opção inválida! Por favor, tente novamente.")
                    input("Pressione Enter para continuar...")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            input("Pressione Enter para continuar...")
