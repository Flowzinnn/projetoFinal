import os
from cadastro import professores, disciplinas

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para alocação de professores em disciplinas
def allocateProfessors():
    clearScreen()
    print("\n=== Alocação de Professores ===")

    if not professores:
        print("Nenhum professor cadastrado. Cadastre professores antes de realizar a alocação.")
        input("\nPressione Enter para voltar ao menu anterior...")
        return

    print("\n--- Professores Disponíveis ---")
    for i, professor in enumerate(professores, start=1):
        print(f"{i} - {professor['nome']} (ID: {professor['professorId']})")

    while True:
        try:
            professorChoice = int(input("\nSelecione o número do professor: ").strip()) - 1
            if 0 <= professorChoice < len(professores):
                selectedProfessor = professores[professorChoice]
                break
            else:
                print("Opção inválida. Selecione um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    print("\n--- Disciplinas Disponíveis ---")
    for i, disciplina in enumerate(disciplinas, start=1):
        print(f"{i} - {disciplina['nome']} (ID: {disciplina['disciplinaId']})")

    while True:
        try:
            disciplineChoice = int(input("\nSelecione o número da disciplina: ").strip()) - 1
            if 0 <= disciplineChoice < len(disciplinas):
                selectedDiscipline = disciplinas[disciplineChoice]
                break
            else:
                print("Opção inválida. Selecione um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # Adicionando professor à lista de professores da disciplina
    if 'professores' not in selectedDiscipline:
        selectedDiscipline['professores'] = []

    if selectedProfessor not in selectedDiscipline['professores']:
        selectedDiscipline['professores'].append(selectedProfessor)
        print(f"\nProfessor {selectedProfessor['nome']} alocado com sucesso à disciplina {selectedDiscipline['nome']}!")
    else:
        print(f"\nO professor {selectedProfessor['nome']} já está alocado à disciplina {selectedDiscipline['nome']}.")

    input("\nPressione Enter para voltar ao menu anterior...")

