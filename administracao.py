import os
from alocar_professores import alocar_professores
from filtrar_professores import filtrar_professores
from adicionar_disciplinas_turma import adicionar_disciplinas_em_turma

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def administracao_menu():
    while True:
        limpar_tela()
        print("\n=== MENU DE ADMINISTRAÇÃO ===")
        print("1 - Alocação de Professores")
        print("2 - Filtrar Professores por Matéria")
        print("3 - Adicionar Disciplinas em Turma")
        print("4 - Voltar ao Menu Principal")

        try:
            mode = int(input("Selecione uma opção: ").strip())
            limpar_tela()
            match mode:
                case 1:  # Alocação de Professores
                    alocar_professores()
                case 2:  # Filtrar Professores por Matéria
                    filtrar_professores()
                case 3:  # Adicionar Disciplinas em Turma
                    adicionar_disciplinas_em_turma()
                case 4:  # Voltar ao Menu Principal
                    
                    break
                case _:
                    print("Opção inválida! Por favor, tente novamente.")
                    input("Pressione Enter para continuar...")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            input("Pressione Enter para continuar...")