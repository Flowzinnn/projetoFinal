import os
from cadastro import alunos, turmas

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def enrollStudent():
    clearScreen()
    print("\n--- Matricular Aluno em Turma ---")

    # Verificar se existem alunos cadastrados
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado. Cadastre um aluno antes de continuar.")
        input("\nPressione Enter para continuar...")
        return

    # Verificar se existem turmas cadastradas
    if len(turmas) == 0:
        print("Nenhuma turma cadastrada. Cadastre uma turma antes de continuar.")
        input("\nPressione Enter para continuar...")
        return

    # Pedir o nome e o ID do aluno para matrícula
    while True:
        studentName = input("Digite o nome do aluno (ou 0 para cancelar): ").strip()
        if studentName == "0":
            print("Matrícula cancelada.")
            input("\nPressione Enter para continuar...")
            return

        studentId = input("Digite o ID do aluno (ou 0 para cancelar): ").strip()
        if studentId == "0":
            print("Matrícula cancelada.")
            input("\nPressione Enter para continuar...")
            return

        # Localizar o aluno com base no nome e ID
        selectedStudent = next(
            (aluno for aluno in alunos if aluno["nome"] == studentName and aluno["alunoId"] == studentId),
            None
        )

        if selectedStudent:
            print(f"Aluno encontrado: {selectedStudent['nome']} (ID: {selectedStudent['alunoId']})")
            break
        else:
            print("Aluno não encontrado. Verifique o nome e o ID e tente novamente.")

    # Exibir turmas disponíveis
    print("\n--- Turmas Disponíveis ---")
    for i, turma in enumerate(turmas, 1):
        print(f"{i} - {turma['nome']} (Código: {turma['codigo']})")

    # Selecionar a turma
    while True:
        classChoice = input("Selecione o número da turma (ou 0 para cancelar): ").strip()
        if classChoice == "0":
            print("Matrícula cancelada.")
            input("\nPressione Enter para continuar...")
            return

        if classChoice.isdigit() and 1 <= int(classChoice) <= len(turmas):
            selectedClass = turmas[int(classChoice) - 1]
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Verificar se o aluno já está matriculado na turma
    if selectedStudent in selectedClass["alunos"]:
        print(f"O aluno {selectedStudent['nome']} já está matriculado na turma {selectedClass['nome']}.")
    else:
        selectedClass["alunos"].append(selectedStudent)
        print(f"Aluno {selectedStudent['nome']} matriculado na turma {selectedClass['nome']} com sucesso!")

    input("\nPressione Enter para continuar...")
