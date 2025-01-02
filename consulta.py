from cadastro import alunos, professores, disciplinas, turmas
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal para consulta
def consultar():
    while True:
        limpar_tela()
        print("\n=== MENU DE CONSULTA ===")
        print("1 - Consultar Aluno")
        print("2 - Consultar Professor")
        print("3 - Consultar Disciplina")
        print("4 - Consultar Turma")
        print("5 - Voltar ao Menu Principal")

        try:
            opcao = int(input("Selecione uma opção: ").strip())
            limpar_tela()
            match opcao:
                case 1:
                    consultar_aluno()
                case 2:
                    consultar_professor()
                case 3:
                    consultar_disciplina()
                case 4:
                    consultar_turma()
                case 5:
                    break
                case _:
                    print("Opção inválida! Por favor, tente novamente.")
                    input("Pressione Enter para continuar...")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            input("Pressione Enter para continuar...")

# Funções de consulta específicas

def consultar_aluno():
    limpar_tela()
    print("=== Consulta de Aluno ===")
    termo = input("Digite o nome ou ID do aluno: ").strip()
    aluno = next((a for a in alunos if a['nome'] == termo or a['alunoId'] == termo), None)

    if aluno:
        while True:
            cpf = input("Confirme os 6 primeiros dígitos do CPF do aluno: ").strip()
            if cpf == aluno['cpf'][:6]:
                limpar_tela()
                print("\n=== Informações do Aluno ===")
                for key, value in aluno.items():
                    print(f"{key.capitalize()}: {value}")

                # Verificar em qual turma o aluno está matriculado
                turmas_aluno = [t['nome'] for t in turmas if aluno in t['alunos']]
                if turmas_aluno:
                    print("\nTurmas matriculadas:")
                    for turma in turmas_aluno:
                        print(f"- {turma}")
                else:
                    print("\nO aluno ainda não está matriculado em nenhuma turma.")
                break
            else:
                print("CPF incorreto! Tente novamente.")
    else:
        print("Aluno não encontrado.")

    input("\nPressione Enter para continuar...")

def consultar_professor():
    limpar_tela()
    print("=== Consulta de Professor ===")
    termo = input("Digite o nome ou ID do professor: ").strip()
    professor = next((p for p in professores if p['nome'] == termo or p['professorId'] == termo), None)

    if professor:
        while True:
            cpf = input("Confirme os 6 primeiros dígitos do CPF do professor: ").strip()
            if cpf == professor['cpf'][:6]:
                limpar_tela()
                print("\n=== Informações do Professor ===")
                for key, value in professor.items():
                    print(f"{key.capitalize()}: {value}")

                # Verificar disciplinas que o professor leciona
                disciplinas_professor = [d['nome'] for d in disciplinas if d.get('professor') == professor]
                if disciplinas_professor:
                    print("\nDisciplinas lecionadas:")
                    for disciplina in disciplinas_professor:
                        print(f"- {disciplina}")
                else:
                    print("\nO professor não está alocado em nenhuma disciplina.")

                # Verificar turmas que possuem disciplinas lecionadas pelo professor
                turmas_professor = [t['nome'] for t in turmas if any(d.get('professor') == professor for d in t['disciplinas'])]
                if turmas_professor:
                    print("\nTurmas associadas:")
                    for turma in turmas_professor:
                        print(f"- {turma}")
                else:
                    print("\nO professor não está associado a nenhuma turma.")
                break
            else:
                print("CPF incorreto! Tente novamente.")
    else:
        print("Professor não encontrado.")

    input("\nPressione Enter para continuar...")

def consultar_disciplina():
    limpar_tela()
    print("=== Consulta de Disciplina ===")
    termo = input("Digite o nome ou ID da disciplina: ").strip()
    disciplina = next((d for d in disciplinas if d['nome'] == termo or d['disciplinaId'] == termo), None)

    if disciplina:
        limpar_tela()
        print("\n=== Informações da Disciplina ===")
        print(f"Nome: {disciplina['nome']}")
        print(f"ID: {disciplina['disciplinaId']}")
        print(f"Carga Horária: {disciplina['cargaHoraria']}")

        professor = disciplina.get('professor')
        if professor:
            print(f"Professor responsável: {professor['nome']}")
        else:
            print("Nenhum professor alocado para esta disciplina.")
    else:
        print("Disciplina não encontrada.")

    input("\nPressione Enter para continuar...")

def consultar_turma():
    limpar_tela()
    print("=== Consulta de Turma ===")
    termo = input("Digite o nome ou ID da turma: ").strip()
    turma = next((t for t in turmas if t['nome'] == termo or t['codigo'] == termo), None)

    if turma:
        limpar_tela()
        print("\n=== Informações da Turma ===")
        print(f"Nome: {turma['nome']}")
        print(f"Código: {turma['codigo']}")

        print("\nDisciplinas alocadas:")
        for disciplina in turma['disciplinas']:
            print(f"- {disciplina['nome']}")

        professor_responsavel = next((disciplina['professor']['nome'] for disciplina in turma['disciplinas'] if disciplina.get('professor')), None)
        if professor_responsavel:
            print(f"\nProfessor responsável: {professor_responsavel}")
        else:
            print("\nNenhum professor alocado à turma.")

        print("\nAlunos matriculados:")
        for aluno in turma['alunos']:
            print(f"- {aluno['nome']}")
    else:
        print("Turma não encontrada.")

    input("\nPressione Enter para continuar...")
