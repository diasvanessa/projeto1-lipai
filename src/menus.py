from models.aluno import Aluno
from services.services import RepositorioAlunos, RepositorioProjetos, RepositorioParticipacoes
from models.participacao import Participacao
from models.projeto import Projeto
import os

repositorio_alunos = RepositorioAlunos()
repositorio_alunos.carregar_alunos()

repositorio_projetos = RepositorioProjetos()
repositorio_projetos.carregar_projetos()

repositorio_participacoes = RepositorioParticipacoes()
repositorio_participacoes.carregar_participacoes(repositorio_alunos, repositorio_projetos)

def cadastrar():
    """ Função para chamar as funcoes de cadastrar alunos, projetos ou participações. """
    print("Deseja cadastrar:")
    print("1. Aluno")
    print("2. Projeto")
    print("3. Participação")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        cadastrar_aluno()
    elif escolha == "2":
        cadastrar_projeto()
    elif escolha == "3":
        cadastrar_participacao()
    else:
        print("Opção inválida.")


def listar():
    """ Função para chamar as funcoes de listar alunos, projetos ou participações. """
    print("Deseja listar:")
    print("1. Aluno")
    print("2. Projeto")
    print("3. Participação")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        listar_alunos()
    elif escolha == "2":
        listar_projetos()
    elif escolha == "3":
        listar_participacoes()
    else:
        print("Opção inválida.")

def buscar():
    print("Deseja buscar:")
    print("1. Aluno")
    print("2. Projeto")
    print("3. Participação")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        buscar_aluno()
    elif escolha == "2":
        buscar_projeto()
    elif escolha == "3":
        buscar_participacao()
    else:
        print("Opção inválida.")


def cadastrar_aluno():
    """ Função para cadastrar um aluno. """
    while True:
        try:
            matricula = input("Digite a matrícula do aluno: ")
            nome = input("Digite o nome do aluno: ")
            email = input("Digite o email do aluno: ")
            aluno = Aluno(matricula, nome, email)
            repositorio_alunos.adicionar_aluno(aluno)
            print(f"Aluno cadastrado com sucesso: {aluno}")
            print("Deseja cadastrar outro aluno? (s/n)")
            resposta = input().lower()
            if resposta == 's':
                continue
            repositorio_alunos.salvar_alunos()
            break
        except ValueError as e:
            print(f"Erro ao cadastrar aluno: {e}. Tente novamente.")


def listar_alunos():
    """ Função para listar todos os alunos cadastrados. """
    alunos = repositorio_alunos.listar_alunos()
    print(alunos)


def buscar_aluno():
    """ Função para buscar um aluno pela matrícula. """
    matricula = input("Digite a matrícula do aluno que deseja buscar: ")
    aluno = repositorio_alunos.buscar_aluno(matricula)
    if aluno:
        print(f"Aluno encontrado: {aluno}")
    else:
        print("Aluno não encontrado.")

def cadastrar_projeto():
    """ Função para cadastrar um projeto. """
    while True:
        try: 
            codigo = int(input("Digite o código do projeto: "))
            titulo = input("Digite o título do projeto: ")
            responsavel = input("Digite o responsável pelo projeto: ")
            projeto = Projeto(codigo, titulo, responsavel)
            repositorio_projetos.adicionar_projeto(projeto)
            print(f"Projeto cadastrado com sucesso: {projeto}")
            print("Deseja cadastrar outro projeto? (s/n)")
            resposta = input().lower()
            if resposta == 's':
                continue
            repositorio_projetos.salvar_projetos()
            break
        except ValueError as e:
            print(f"Erro ao cadastrar projeto: {e}. Tente novamente.")
            
def listar_projetos():
    """ Função para listar todos os projetos cadastrados. """
    projetos = repositorio_projetos.listar_projetos()
    print(projetos)
    
def buscar_projeto():
    """ Função para buscar um projeto pelo código. """
    codigo = int(input("Digite o código do projeto que deseja buscar: "))
    projeto = repositorio_projetos.buscar_projeto(codigo)
    if projeto:
        print(f"Projeto encontrado: {projeto}")
    else:
        print("Projeto não encontrado.")
        
def cadastrar_participacao():
    """ Função para cadastrar uma participação. """
    while True:
        try:
            matricula = input("Digite a matrícula do aluno: ")
            aluno = repositorio_alunos.buscar_aluno(matricula)
            if not aluno:
                print("Aluno não encontrado.")
                return
            codigo = input("Digite o código do projeto: ")
            codigo = int(codigo)
            projeto = repositorio_projetos.buscar_projeto(codigo)
            if not projeto:
                print("Projeto não encontrado.")
                return
            data_inicio = input("Digite a data de início da participação (DD/MM/AAAA): ")
            data_fim = input("Digite a data de fim da participação (DD/MM/AAAA): ")
            participacao = Participacao(data_inicio, data_fim, aluno, projeto)
            repositorio_participacoes.adicionar_participacao(participacao)
            escolha = input("Deseja cadastrar outra participação? (s/n): ").lower()
            if escolha == 's':
                continue
            repositorio_participacoes.salvar_participacoes()
            break            
        except ValueError as e:
            print(f"Erro ao cadastrar participacao: {e}. Tente novamente.")
    
    
def listar_participacoes():
    """ Função para listar todas as participações cadastradas. """
    participacoes = repositorio_participacoes.listar_participacoes()
    print(participacoes)
    
def buscar_participacao():
    """ Funcao para buscar todos os alunos participantes de um projeto ou
    todos projetos de um aluno."""
    print("Deseja buscar participações por:")
    print("1. Participações de aluno")
    print("2. Alunos de um projeto")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        matricula = input("Digite a matrícula do aluno: ")
        participacoes = repositorio_participacoes.buscar_participacoes_por_aluno(matricula)
        if participacoes:
            print(f"Participações encontradas: {participacoes}")
        else:
            print("Nenhuma participação encontrada para esse aluno.")
    elif escolha == "2":
        codigo = int(input("Digite o código do projeto: "))
        participacoes = repositorio_participacoes.buscar_participacoes_por_projeto(codigo)
        if participacoes:
            print(f"Alunos participantes encontrados: {participacoes}")
        else:
            print("Nenhum aluno encontrado para esse projeto.")
            
