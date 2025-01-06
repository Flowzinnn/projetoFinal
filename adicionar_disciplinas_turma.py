import os
from cadastro import turmas, disciplinas

def clearScreen():                          
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para adicionar disciplinas em turmas
def addSubjectsToClass():
    clearScreen()
    print("\n=== Adicionar disciplinas em Turmas ===")

    if not turmas:
        print("Nenhuma turma cadastrada. Cadastre uma turma antes de continuar.")
        input("Pressione Enter para continuar...")
        return

    if not disciplinas:
        print("Nenhuma disciplina cadastrada. Cadastre disciplinas antes de continuar.")
        input("Pressione Enter para continuar...")
        return

    # Listar turmas disponíveis
    print("\nTurmas disponíveis:")
    for i, turma in enumerate(turmas, 1):
        print(f"{i} - {turma['nome']} (Código: {turma['codigo']})")

    while True:
        classOption = input("\nDigite o número da turma que deseja editar (ou 0 para cancelar): ").strip()
        if classOption == "0":
            print("Operação cancelada.")
            input("Pressione Enter para continuar...")
            return

        if classOption.isdigit() and 1 <= int(classOption) <= len(turmas):
            selectedClass = turmas[int(classOption) - 1]
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Listar disciplinas disponíveis
    print("\nDisciplinas disponíveis para adicionar:")
    for i, disciplina in enumerate(disciplinas, 1):
        print(f"{i} - {disciplina['nome']} (ID: {disciplina['disciplinaId']})")

    while True:
        subjectOption = input("\nDigite o número da disciplina que deseja adicionar (ou 0 para finalizar): ").strip()
        if subjectOption == "0":
            break

        if subjectOption.isdigit() and 1 <= int(subjectOption) <= len(disciplinas):
            selectedSubject = disciplinas[int(subjectOption) - 1]

            if selectedSubject in selectedClass['disciplinas']:
                print(f"A disciplina {selectedSubject['nome']} já está associada a esta turma.")
            else:
                selectedClass['disciplinas'].append(selectedSubject)
                print(f"Disciplina {selectedSubject['nome']} adicionada com sucesso!")
        else:
            print("Opção inválida. Tente novamente.")

    print("\nAtualização concluída.")
    input("Pressione Enter para continuar...")
