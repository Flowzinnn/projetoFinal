from cadastro import alunos, turmas
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def matricular_aluno():
    limpar_tela()
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
        nome_aluno = input("Digite o nome do aluno (ou 0 para cancelar): ").strip()
        if nome_aluno == "0":
            print("Matrícula cancelada.")
            input("\nPressione Enter para continuar...")
            return

        id_aluno = input("Digite o ID do aluno (ou 0 para cancelar): ").strip()
        if id_aluno == "0":
            print("Matrícula cancelada.")
            input("\nPressione Enter para continuar...")
            return

        # Localizar o aluno com base no nome e ID
        aluno_selecionado = next(
            (aluno for aluno in alunos if aluno["nome"] == nome_aluno and aluno["alunoId"] == id_aluno),
            None
        )

        if aluno_selecionado:
            print(f"Aluno encontrado: {aluno_selecionado['nome']} (ID: {aluno_selecionado['alunoId']})")
            break
        else:
            print("Aluno não encontrado. Verifique o nome e o ID e tente novamente.")

    # Exibir turmas disponíveis
    print("\n--- Turmas Disponíveis ---")
    for i, turma in enumerate(turmas, 1):
        print(f"{i} - {turma['nome']} (Código: {turma['codigo']})")

    # Selecionar a turma
    while True:
        escolha_turma = input("Selecione o número da turma (ou 0 para cancelar): ").strip()
        if escolha_turma == "0":
            print("Matrícula cancelada.")
            input("\nPressione Enter para continuar...")
            return

        if escolha_turma.isdigit() and 1 <= int(escolha_turma) <= len(turmas):
            turma_selecionada = turmas[int(escolha_turma) - 1]
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Verificar se o aluno já está matriculado na turma
    if aluno_selecionado in turma_selecionada["alunos"]:
        print(f"O aluno {aluno_selecionado['nome']} já está matriculado na turma {turma_selecionada['nome']}.")
    else:
        turma_selecionada["alunos"].append(aluno_selecionado)
        print(f"Aluno {aluno_selecionado['nome']} matriculado na turma {turma_selecionada['nome']} com sucesso!")

    input("\nPressione Enter para continuar...")
