"""Módulo que define os repositórios para alunos, projetos e participações."""

import os
from models.aluno import Aluno
from models.projeto import Projeto
from models.participacao import Participacao

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

CAMINHO_ALUNOS = os.path.join(DATA_DIR, "alunos.csv")
CAMINHO_PROJETOS = os.path.join(DATA_DIR, "projetos.csv")
CAMINHO_PARTICIPACOES = os.path.join(DATA_DIR, "participacoes.csv")


class RepositorioAlunos:
    """Classe que representa um repositório de alunos."""

    def __init__(self):
        self.alunos = {}

    def adicionar_aluno(self, aluno):
        """ Adiciona um aluno ao repositório. """
        if aluno.matricula in self.alunos:
            raise ValueError("Aluno com essa matrícula já existe.")
        self.alunos[aluno.matricula] = aluno

    def buscar_aluno(self, matricula):
        """ Busca no repositorio um aluno com a matricula fornecida. """
        return self.alunos.get(matricula, None)

    def listar_alunos(self):
        """ Retorna uma lista com todos os alunos cadastrados. """
        return list(self.alunos.values())

    def salvar_alunos(self):
        """ Salva os alunos no arquivo CSV. """
        with open(CAMINHO_ALUNOS, "w", encoding='utf-8') as arquivo:
            for aluno in self.alunos.values():
                arquivo.write(
                    f"{aluno.matricula},{aluno.nome},{aluno.email}\n")

    def carregar_alunos(self):
        """ Carrega os alunos do arquivo CSV. """
        with open(CAMINHO_ALUNOS, "r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                aluno = Aluno.from_string(linha.strip())
                self.adicionar_aluno(aluno)


class RepositorioProjetos:
    """Classe que representa um repositorio de projetos"""

    def __init__(self):
        self.projetos = {}

    def adicionar_projeto(self, projeto):
        """ Adiciona um projeto ao repositório. """
        if projeto.codigo in self.projetos:
            raise ValueError("Projeto com esse código já existe.")
        self.projetos[projeto.codigo] = projeto

    def buscar_projeto(self, codigo):
        """ Busca no repositório um projeto com o código fornecido. """
        return self.projetos.get(codigo, None)

    def listar_projetos(self):
        """ Retorna uma lista com todos os projetos cadastrados. """
        return list(self.projetos.values())

    def salvar_projetos(self):
        """ Salva os projetos no arquivo CSV. """
        with open(CAMINHO_PROJETOS, "w", encoding='utf-8') as arquivo:
            for projeto in self.projetos.values():
                arquivo.write(
                    f"{projeto.codigo},{projeto.titulo},{projeto.responsavel}\n")

    def carregar_projetos(self):
        """ Carrega os projetos do arquivo CSV. """
        with open(CAMINHO_PROJETOS, "r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                projeto = Projeto.from_string(linha.strip())
                
                self.adicionar_projeto(projeto)
                
    def adicionar_participacao_ao_projeto(self, codigo_projeto, participacao):
        """ Adiciona uma participação a um projeto específico. """
        projeto = self.buscar_projeto(codigo_projeto)
        if projeto:
            projeto.adicionar_participacao(participacao)
        else:
            raise ValueError("Projeto não encontrado.")


class RepositorioParticipacoes:
    """ Classe que representa um repositório de participações."""

    def __init__(self):
        self.participacoes = []

    def adicionar_participacao(self, participacao):
        """ Adiciona uma participação ao repositório. """
        if participacao.aluno.matricula in [p.aluno.matricula for p in self.participacoes if p.projeto.codigo == participacao.projeto.codigo]:
            raise ValueError("Esse aluno já está cadastrado nesse projeto.")
        self.participacoes.append(participacao)

    def listar_participacoes(self):
        """ Retorna uma lista com todas as participações cadastradas. """
        return self.participacoes
    
    def salvar_participacoes(self):
        """ Salva as participações no arquivo CSV. """
        with open(CAMINHO_PARTICIPACOES, "w", encoding='utf-8') as arquivo:
            for participacao in self.participacoes:
                arquivo.write(
                    f"{participacao.codigo},{participacao.data_inicio},{participacao.data_fim},{participacao.aluno.matricula},{participacao.projeto.codigo}\n")

    def carregar_participacoes(self, repositorio_alunos, repositorio_projetos):
        """ Carrega as participações do arquivo CSV. """
        with open(CAMINHO_PARTICIPACOES, "r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                codigo, data_inicio, data_fim, matricula, codigo_projeto,  = linha.strip().split(
                    sep=",")
                aluno = repositorio_alunos.buscar_aluno(matricula)
                projeto = repositorio_projetos.buscar_projeto(int(codigo_projeto))
                if aluno and projeto:
                    participacao = Participacao(
                        data_inicio, data_fim, aluno, projeto, codigo)
                    self.adicionar_participacao(participacao)
                    projeto.adicionar_participacao(participacao)

    def buscar_participacoes_por_aluno(self, matricula):
        """ Busca todas as participações de um aluno pelo número de matrícula. """
        participacoes = []
        for participacao in self.participacoes:
            if participacao.aluno.matricula == matricula:
                dados = {
                    "titulo": participacao.projeto.titulo,
                    "data_inicio": participacao.data_inicio,
                    "data_fim": participacao.data_fim
                }
                participacoes.append(dados)
        return participacoes
    
    def buscar_participacoes_por_projeto(self, codigo):
        """ Busca todos os alunos participantes de um projeto pelo código do projeto. """
        participacoes = []
        for participacao in self.participacoes:
            if participacao.projeto.codigo == codigo:
                dados = {
                    "Aluno": participacao.aluno.nome,
                    "data_inicio": participacao.data_inicio,
                    "data_fim": participacao.data_fim
                }
                participacoes.append(dados)
        return participacoes
    