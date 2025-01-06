Sites que ajudaram a realizar o projeto:

https://pillow.readthedocs.io/en/stable/installation/basic-installation.html

https://docs.python.org/pt-br/3/tutorial/controlflow.html#match-statements

https://docs.python.org/pt-br/3/tutorial/datastructures.html#tuples-and-sequences

https://cursos.alura.com.br/course/python-crie-sua-primeira-aplicacao/task/151390

https://docs.python.org/3/

https://realpython.com/

https://www.w3schools.com/python/

https://www.programiz.com/python-programming

# Claro, não poderia deixar de fazer uma menção honrosa ao ChatGPT por tirar todas as minhas dúvidas
 e ajudar a resolver os INCONTAVEIS ERROS que esse código teve ao longo de sua criação.


                                                #sistema escolar - cadastrar alunos, professores, turmas, disciplinas.
                                                        #alunos: nome matriculas, id(vc cria), data de nascimento sexo endereço telefone email
                                                        #professores: nome, id(vc cria), matricula, data de nascimento, sexo, endereço, telefone, email
                                                        #disciplina: nome código(vc cria), carga horaria, professor 
                                                        #turmas: nome, código(vc cria), disciplina, professor, alunos(lista-pequena)}
                                                        
                                                #deve permitir a matricula de alunos em turmas

                                                #o sistema deve permitir a alocação de professores em disciplinas

                                                #o sistema deve permitir a alocação de disciplinas em turmas

                                                #a consulta de alunos matriculados em turmas

                                                #a consulta de professores alocados em disciplinas

                                                #a consulta de disciplinas alocadas em turmas

                                                #permitir a filtragem de professores por disciplina

                                                #minhas ideias: criar uma interface onde eu posso selecionar o que a pessoa quer fazer (cadastrar, verificar tudo(matérias alunos professores categoria id))

                                                #cada cadastro gera uma sequencia de codigo/id aleatorio de 5 numeros que definiram quem é professor/aluno ou turma/disciplina


Estrutura do Projeto

Arquivos e Funções Principais

1. Index:
        Responsável pelo menu principal do sistema e pela navegação entre os módulos.

Funções principais:
        startSchool_message: Exibe uma mensagem de boas-vindas.
        selectOption: Permite selecionar as opções do menu principal (cadastro, consulta, matrículas, administração).

2. Cadastro:
        Contém as funções para cadastrar alunos, professores, disciplinas e turmas.
        Verifica se CPF tem 11 dígitos.
        Gera IDs únicos para alunos, professores, disciplinas e turmas.

Funções principais:        
        registerStudent: Cadastra um novo aluno.
        registerTeacher: Cadastra um novo professor.
        registerDiscipline: Adiciona uma nova disciplina.
        registerClass: Cria uma nova turma verificando pré-requisitos (alunos, professores e disciplinas).

3. Consulta:
        Permite realizar consultas sobre alunos, professores, disciplinas e turmas.
        Exige os 6 primeiros dígitos do CPF para exibir informações de alunos e professores pela Lei Geral de Proteção de Dados LGPD. 
        Exibe mensagens claras caso não encontre registros.

Funções principais:
        consultStudent: Exibe informações de um aluno e suas turmas.
        consultTeacher: Exibe informações de um professor, suas disciplinas e turmas.
        consultDiscipline: Mostra detalhes de uma disciplina e seu professor.
        consultClass: Lista as disciplinas e alunos de uma turma.

4. Matricula:
        Realiza a matrícula de alunos em turmas.
        Verifica se o aluno já está matriculado em uma turma antes de matricular.

Funções principais:
        enrollStudent: Permite selecionar um aluno e matriculá-lo em uma turma.

5. Administracao:
        Menu para administrar alocações de professores, filtrar professores por disciplina e adicionar disciplinas em turmas.
        Garante que disciplinas e professores existam antes de realizar alocações.

Funções principais:
        allocateProfessors: Seleciona um professor e o aloca a uma disciplina.
        addSubjectsToClass: Adiciona disciplinas adicionais a turmas.
        administrationMenu: Menu principal de administração.
        filterProfessors: Busca disciplinas e exibe o professor vinculado.
