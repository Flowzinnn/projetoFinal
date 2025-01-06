import os
from cadastro import alunos, professores, disciplinas, turmas

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função do sub-menu de consulta
def consultationSubMenu():
    while True:
        clearScreen()
        print("\n=== MENU DE CONSULTA ===")
        print("1 - Consultar Aluno")
        print("2 - Consultar Professor")
        print("3 - Consultar Disciplina")
        print("4 - Consultar Turma")
        print("5 - Voltar ao Menu Principal")

        try:
            option = int(input("Selecione uma opção: ").strip())
            clearScreen()
            match option:
                case 1:
                    consultStudent()
                case 2:
                    consultTeacher()
                case 3:
                    consultDiscipline()
                case 4:
                    consultClass()
                case 5:
                    break
                case _:
                    print("Opção inválida! Por favor, tente novamente.")
                    input("Pressione Enter para continuar...")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            input("Pressione Enter para continuar...")

# Funções de consulta específicas:
# Aluno
def consultStudent():
    clearScreen()
    print("=== Consulta de Aluno ===")
    term = input("Digite o nome ou ID do aluno: ").strip()
    student = next((a for a in alunos if a['nome'] == term or a['alunoId'] == term), None)

    if student:
        while True:
            cpf = input("Confirme os 6 primeiros dígitos do CPF do aluno: ").strip()
            if cpf == student['cpf'][:6]:
                clearScreen()
                print("\n=== Informações do Aluno ===")
                for key, value in student.items():
                    print(f"{key.capitalize()}: {value}")

                # Verificar em qual turma o aluno está matriculado
                studentClasses = [t['nome'] for t in turmas if student in t['alunos']]
                if studentClasses:
                    print("\nTurmas matriculadas:")
                    for turma in studentClasses:
                        print(f"- {turma}")
                else:
                    print("\nO aluno ainda não está matriculado em nenhuma turma.")
                break
            else:
                print("CPF incorreto! Tente novamente.")
    else:
        print("Aluno não encontrado.")

    input("\nPressione Enter para continuar...")
    
# Professor
def consultTeacher():
    clearScreen()
    print("=== Consulta de Professor ===")
    term = input("Digite o nome ou ID do professor: ").strip()
    professor = next((p for p in professores if p['nome'] == term or p['professorId'] == term), None)

    if professor:
        while True:
            cpf = input("Confirme os 6 primeiros dígitos do CPF do professor: ").strip()
            if cpf == professor['cpf'][:6]:
                clearScreen()
                print("\n=== Informações do Professor ===")
                for key, value in professor.items():
                    print(f"{key.capitalize()}: {value}")

                # Verificar disciplinas que o professor leciona
                professorDisciplines = [
                    d['nome'] for d in disciplinas if 'professores' in d and professor in d['professores']
                ]
                if professorDisciplines:
                    print("\nDisciplinas lecionadas:")
                    for disciplina in professorDisciplines:
                        print(f"- {disciplina}")
                else:
                    print("\nO professor não está alocado em nenhuma disciplina.")

                # Verificar turmas que possuem disciplinas lecionadas pelo professor
                professorClasses = [
                    t['nome'] for t in turmas
                    if any('professores' in d and professor in d['professores'] for d in t['disciplinas'])
                ]
                if professorClasses:
                    print("\nTurmas associadas:")
                    for turma in professorClasses:
                        print(f"- {turma}")
                else:
                    print("\nO professor não está associado a nenhuma turma.")
                break
            else:
                print("CPF incorreto! Tente novamente.")
    else:
        print("Professor não encontrado.")

    input("\nPressione Enter para continuar...")

    
# Disciplinas
def consultDiscipline():
    clearScreen()
    print("=== Consulta de Disciplina ===")
    term = input("Digite o nome ou ID da disciplina: ").strip()
    discipline = next((d for d in disciplinas if d['nome'] == term or d['disciplinaId'] == term), None)

    if discipline:
        clearScreen()
        print("\n=== Informações da Disciplina ===")
        print(f"Nome: {discipline['nome']}")
        print(f"ID: {discipline['disciplinaId']}")
        print(f"Carga Horária: {discipline.get('cargaHoraria', 'Não especificada')}")

        # Exibir todos os professores associados
        if 'professores' in discipline and discipline['professores']:
            print("\nProfessores responsáveis:")
            for professor in discipline['professores']:
                print(f"- {professor['nome']} (ID: {professor['professorId']})")
        else:
            print("Nenhum professor alocado para esta disciplina.")
    else:
        print("Disciplina não encontrada.")

    input("\nPressione Enter para continuar...")
    
# Turma
def consultClass():
    clearScreen()
    print("=== Consulta de Turma ===")
    term = input("Digite o nome ou ID da turma: ").strip()
    turma = next((t for t in turmas if t['nome'] == term or t['codigo'] == term), None)

    if turma:
        clearScreen()
        print("\n=== Informações da Turma ===")
        print(f"Nome: {turma['nome']}")
        print(f"Código: {turma['codigo']}")

        print("\nDisciplinas alocadas:")
        for disciplina in turma['disciplinas']:
            print(f"- {disciplina['nome']}")

        print("\nAlunos matriculados:")
        for aluno in turma['alunos']:
            print(f"- {aluno['nome']}")
    else:
        print("Turma não encontrada.")

    input("\nPressione Enter para continuar...")
