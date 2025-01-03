import os
from cadastro import turmas, disciplinas

def limpar_tela():                          
    os.system('cls' if os.name == 'nt' else 'clear')  #Função

def adicionar_disciplinas_em_turma():
    limpar_tela()
    print("\n=== Adicionar Disciplinas em Turma ===")

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
        opcao_turma = input("\nDigite o número da turma que deseja editar (ou 0 para cancelar): ").strip()
        if opcao_turma == "0":
            print("Operação cancelada.")
            input("Pressione Enter para continuar...")
            return

        if opcao_turma.isdigit() and 1 <= int(opcao_turma) <= len(turmas):
            turma_selecionada = turmas[int(opcao_turma) - 1]
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Listar disciplinas disponíveis
    print("\nDisciplinas disponíveis para adicionar:")
    for i, disciplina in enumerate(disciplinas, 1):
        print(f"{i} - {disciplina['nome']} (ID: {disciplina['disciplinaId']})")

    while True:
        opcao_disciplina = input("\nDigite o número da disciplina que deseja adicionar (ou 0 para finalizar): ").strip()
        if opcao_disciplina == "0":
            break

        if opcao_disciplina.isdigit() and 1 <= int(opcao_disciplina) <= len(disciplinas):
            disciplina_selecionada = disciplinas[int(opcao_disciplina) - 1]

            if disciplina_selecionada in turma_selecionada['disciplinas']:
                print(f"A disciplina {disciplina_selecionada['nome']} já está associada a esta turma.")
            else:
                turma_selecionada['disciplinas'].append(disciplina_selecionada)
                print(f"Disciplina {disciplina_selecionada['nome']} adicionada com sucesso!")
        else:
            print("Opção inválida. Tente novamente.")

    print("\nAtualização concluída.")
    input("Pressione Enter para continuar...")
