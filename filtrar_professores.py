from cadastro import disciplinas

def filterProfessors():
    print("\n=== FILTRAR PROFESSORES POR MATÉRIA ===")

    # Verificar se há disciplinas cadastradas
    if not disciplinas:
        print("Nenhuma disciplina cadastrada. Cadastre disciplinas primeiro.")
        input("Pressione Enter para voltar ao menu anterior.")
        return

    # Buscar disciplina
    termo = input("Digite o nome ou ID da disciplina: ").strip()
    disciplina = next((d for d in disciplinas if d["nome"] == termo or d["disciplinaId"] == termo), None)

    if not disciplina:
        print("Disciplina não encontrada. Verifique o nome ou ID e tente novamente.")
        input("Pressione Enter para voltar ao menu anterior.")
        return

    # Verificar professores associados
    professores = disciplina.get("professores", [])
    if not professores:
        print(f"A disciplina {disciplina['nome']} ainda não possui professores alocados.")
    else:
        print(f"\nProfessores alocados à disciplina {disciplina['nome']}:")
        for professor in professores:
            print(f"- Nome: {professor['nome']} | ID: {professor['professorId']}")

    input("\nPressione Enter para voltar ao menu anterior.")
