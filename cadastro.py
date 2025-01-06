import os
import random
import string

# Listas para armazenar os registros
alunos = []
professores = []
disciplinas = []
turmas = []


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funções para gerar IDs 
def generateStudentId():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

def generateTeacherId():
    letra = random.choice(string.ascii_uppercase)
    numeros = ''.join(random.choices(string.digits, k=4))
    return letra + numeros

def generateDisciplineId():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=3))

def generateClassId():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=4))

# Validação do CPF
def validateCpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

# Submenu de cadastro
def registrationSubMenu():
    while True:
        clearScreen()
        print("\n=== MENU DE CADASTRO ===")
        print("1 - Cadastrar Aluno")
        print("2 - Cadastrar Professor")
        print("3 - Cadastrar Disciplina")
        print("4 - Cadastrar Turma")
        print("5 - Voltar ao Menu Principal")

        try:
            option = int(input("Selecione uma opção: ").strip())
            clearScreen()
            match option:
                case 1:
                    registerStudent()
                case 2:
                    registerTeacher()
                case 3:
                    registerDiscipline()
                case 4:
                    registerClass()
                case 5:
                    break
                case _:
                    print("Opção inválida! Por favor, tente novamente.")
                    input("Pressione Enter para continuar...")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            input("Pressione Enter para continuar...")

# Funções de cadastro
# Aluno
def registerStudent():
    clearScreen()
    print("=== Cadastro de Aluno ===")
    nome = input("Nome: ").strip()
    alunoId = generateStudentId()
    dataNascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()

    while True:
        cpf = input("CPF (apenas números): ").strip()
        if validateCpf(cpf):
            break
        else:
            print("CPF inválido! Certifique-se de digitar 11 números.")

    sexo = input("Sexo (M/F): ").strip().upper()
    endereco = input("Endereço: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

    alunos.append({
        "nome": nome,
        "alunoId": alunoId,
        "dataNascimento": dataNascimento,
        "cpf": cpf,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
    })
    clearScreen()
    print(f"Aluno cadastrado com sucesso!\nNome: {nome}\nID: {alunoId}")
    input("Pressione Enter para continuar...")

# Professor
def registerTeacher():
    clearScreen()
    print("=== Cadastro de Professor ===")
    nome = input("Nome: ").strip()
    professorId = generateTeacherId()
    dataNascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()

    while True:
        cpf = input("CPF (apenas números): ").strip()
        if validateCpf(cpf):
            break
        else:
            print("CPF inválido! Certifique-se de digitar 11 números.")

    sexo = input("Sexo (M/F): ").strip().upper()
    endereco = input("Endereço: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

    professores.append({
        "nome": nome,
        "professorId": professorId,
        "dataNascimento": dataNascimento,
        "cpf": cpf,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
    })
    clearScreen()
    print(f"Professor cadastrado com sucesso!\nNome: {nome}\nID: {professorId}")
    input("Pressione Enter para continuar...")

# Disciplina
def registerDiscipline():
    clearScreen()
    print("=== Cadastro de Disciplina ===")
    nome = input("Nome da disciplina: ").strip()
    disciplinaId = generateDisciplineId()
    cargaHoraria = input("Carga horária: ").strip()

    disciplinas.append({
        "nome": nome,
        "disciplinaId": disciplinaId,
        "cargaHoraria": cargaHoraria,
        "professor": None
    })
    clearScreen()
    print(f"Disciplina cadastrada com sucesso!\nNome: {nome}\nID: {disciplinaId}")
    input("Pressione Enter para continuar...")

# Turmas
def registerClass():
    clearScreen()
    print("=== Cadastro de Turma ===")

    if not alunos:
        print("Erro: Não há alunos cadastrados. Cadastre pelo menos um aluno antes de criar uma turma.")
        input("Pressione Enter para voltar...")
        return

    if not professores:
        print("Erro: Não há professores cadastrados. Cadastre pelo menos um professor antes de criar uma turma.")
        input("Pressione Enter para voltar...")
        return

    if not disciplinas:
        print("Erro: Não há disciplinas cadastradas. Cadastre pelo menos uma disciplina antes de criar uma turma.")
        input("Pressione Enter para voltar...")
        return

    nome = input("Nome da turma: ").strip()
    codigo = generateClassId()

    # Verificação de disciplinas disponíveis para alocação.
    disciplinasDisponiveis = [d for d in disciplinas]
    print("\nDisciplinas disponíveis para associação:")
    for i, disciplina in enumerate(disciplinasDisponiveis, start=1):
        print(f"{i} - {disciplina['nome']} (ID: {disciplina['disciplinaId']})")

    disciplinasAssociadas = []
    while True:
        opcao = input("Digite o número da disciplina para associar ou 0 para encerrar: ").strip()
        if opcao == "0":
            break
        try:
            index = int(opcao) - 1
            if 0 <= index < len(disciplinasDisponiveis):
                disciplinasAssociadas.append(disciplinasDisponiveis[index])
                print(f"Disciplina {disciplinasDisponiveis[index]['nome']} associada com sucesso!")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    turmas.append({
        "nome": nome,
        "codigo": codigo,
        "disciplinas": disciplinasAssociadas,
        "alunos": []
    })
    clearScreen()
    print(f"Turma cadastrada com sucesso!\nNome: {nome}\nID: {codigo}")
    input("Pressione Enter para continuar...")
