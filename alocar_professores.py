import os
from cadastro import professores, disciplinas

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def alocar_professores():
    limpar_tela()
    print("\n=== Alocação de Professores ===")

    if not professores:
        print("Nenhum professor cadastrado. Cadastre professores antes de realizar a alocação.")
        input("\nPressione Enter para voltar ao menu anterior...")
        return

    disciplinas_sem_professor = [d for d in disciplinas if d['professor'] is None]
    if not disciplinas_sem_professor:
        print("Todas as disciplinas já possuem professores alocados ou nenhuma disciplina foi cadastrada.")
        input("\nPressione Enter para voltar ao menu anterior...")
        return

    print("\n--- Professores Disponíveis ---")
    for i, professor in enumerate(professores, start=1):
        print(f"{i} - {professor['nome']} (ID: {professor['professorId']})")

    while True:
        try:
            escolha_professor = int(input("\nSelecione o número do professor: ").strip()) - 1
            if 0 <= escolha_professor < len(professores):
                professor_selecionado = professores[escolha_professor]
                break
            else:
                print("Opção inválida. Selecione um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    print("\n--- Disciplinas Disponíveis ---")
    for i, disciplina in enumerate(disciplinas_sem_professor, start=1):
        print(f"{i} - {disciplina['nome']} (ID: {disciplina['disciplinaId']})")

    while True:
        try:
            escolha_disciplina = int(input("\nSelecione o número da disciplina: ").strip()) - 1
            if 0 <= escolha_disciplina < len(disciplinas_sem_professor):
                disciplina_selecionada = disciplinas_sem_professor[escolha_disciplina]
                break
            else:
                print("Opção inválida. Selecione um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    disciplina_selecionada['professor'] = professor_selecionado
    print(f"\nProfessor {professor_selecionado['nome']} alocado com sucesso à disciplina {disciplina_selecionada['nome']}!")
    input("\nPressione Enter para voltar ao menu anterior...")
