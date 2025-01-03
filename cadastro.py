import os
import random
import string

# Listas para armazenar os registros
alunos = []
professores = []
disciplinas = []
turmas = []

# Funções auxiliares para manipulação do sistema
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def getAlunoId():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

def getProfessorId():
    letra = random.choice(string.ascii_uppercase)
    numeros = ''.join(random.choices(string.digits, k=4))
    return letra + numeros

def getDisciplinaId():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=3))

def getTurmaId():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=4))

#Validação do CPF
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

# Submenu de cadastro
def cadastroSubMenu():
    while True:
        limpar_tela()
        print("\n=== MENU DE CADASTRO ===")
        print("1 - Cadastrar Aluno")
        print("2 - Cadastrar Professor")
        print("3 - Cadastrar Disciplina")
        print("4 - Cadastrar Turma")
        print("5 - Voltar ao Menu Principal")

        try:
            opcao = int(input("Selecione uma opção: ").strip())
            limpar_tela()
            match opcao:
                case 1:
                    cadastrar_aluno()
                case 2:
                    cadastrar_professor()
                case 3:
                    cadastrar_disciplina()
                case 4:
                    cadastrar_turma()
                case 5:
                    break
                case _:
                    print("Opção inválida! Por favor, tente novamente.")
                    input("Pressione Enter para continuar...")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            input("Pressione Enter para continuar...")

# Funções de cadastro
#Aluno
def cadastrar_aluno():
    limpar_tela()
    print("=== Cadastro de Aluno ===")
    nome = input("Nome: ").strip()
    alunoId = getAlunoId()
    dataNascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()

    while True:
        cpf = input("CPF (apenas números): ").strip()
        if validar_cpf(cpf):
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
    limpar_tela()
    print(f"Aluno cadastrado com sucesso!\nNome: {nome}\nID: {alunoId}")
    input("Pressione Enter para continuar...")

#Professor
def cadastrar_professor():
    limpar_tela()
    print("=== Cadastro de Professor ===")
    nome = input("Nome: ").strip()
    professorId = getProfessorId()
    dataNascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()

    while True:
        cpf = input("CPF (apenas números): ").strip()
        if validar_cpf(cpf):
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
    limpar_tela()
    print(f"Professor cadastrado com sucesso!\nNome: {nome}\nID: {professorId}")
    input("Pressione Enter para continuar...")

#Disciplina
def cadastrar_disciplina():
    limpar_tela()
    print("=== Cadastro de Disciplina ===")
    nome = input("Nome da disciplina: ").strip()
    disciplinaId = getDisciplinaId()
    cargaHoraria = input("Carga horária: ").strip()

    disciplinas.append({
        "nome": nome,
        "disciplinaId": disciplinaId,
        "cargaHoraria": cargaHoraria,
        "professor": None
    })
    limpar_tela()
    print(f"Disciplina cadastrada com sucesso!\nNome: {nome}\nID: {disciplinaId}")
    input("Pressione Enter para continuar...")

#Turmas
def cadastrar_turma():
    limpar_tela()
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
    codigo = getTurmaId()

    #Verificação de disciplinas disponiveis para alocação.
    disciplinas_disponiveis = [d for d in disciplinas]
    print("\nDisciplinas disponíveis para associação:")
    for i, disciplina in enumerate(disciplinas_disponiveis, start=1):
        print(f"{i} - {disciplina['nome']} (ID: {disciplina['disciplinaId']})")

    disciplinas_associadas = []
    while True:
        opcao = input("Digite o número da disciplina para associar ou 0 para encerrar: ").strip()
        if opcao == "0":
            break
        try:
            index = int(opcao) - 1
            if 0 <= index < len(disciplinas_disponiveis):
                disciplinas_associadas.append(disciplinas_disponiveis[index])
                print(f"Disciplina {disciplinas_disponiveis[index]['nome']} associada com sucesso!")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    turmas.append({
        "nome": nome,
        "codigo": codigo,
        "disciplinas": disciplinas_associadas,
        "alunos": []
    })
    limpar_tela()
    print(f"Turma cadastrada com sucesso!\nNome: {nome}\nID: {codigo}")
    input("Pressione Enter para continuar...")
