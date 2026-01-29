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
        if aluno.matricula in self.alunos:
            raise ValueError("Aluno com essa matrícula já existe.")
        self.alunos[aluno.matricula] = aluno

    def buscar_aluno(self, matricula):
        return self.alunos.get(matricula, None)

    def listar_alunos(self):
        return list(self.alunos.values())

    def salvar_alunos(self):
        with open(CAMINHO_ALUNOS, "w", encoding='utf-8') as arquivo:
            for aluno in self.alunos.values():
                arquivo.write(
                    f"{aluno.matricula},{aluno.nome},{aluno.email}\n")

    def carregar_alunos(self):
        with open(CAMINHO_ALUNOS, "r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                aluno = Aluno.from_string(linha.strip())
                self.adicionar_aluno(aluno)


class RepositorioProjetos:
    """Classe que representa um repositorio de projetos"""

    def __init__(self):
        self.projetos = {}

    def adicionar_projeto(self, projeto):
        if projeto.codigo in self.projetos:
            raise ValueError("Projeto com esse código já existe.")
        self.projetos[projeto.codigo] = projeto

    def buscar_projeto(self, codigo):
        return self.projetos.get(codigo, None)

    def listar_projetos(self):
        return list(self.projetos.values())

    def salvar_projetos(self):
        with open(CAMINHO_PROJETOS, "w", encoding='utf-8') as arquivo:
            for projeto in self.projetos.values():
                arquivo.write(
                    f"{projeto.codigo},{projeto.titulo},{projeto.responsavel}\n")

    def carregar_projetos(self):
        with open(CAMINHO_PROJETOS, "r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                projeto = Projeto.from_string(linha.strip())
                
                self.adicionar_projeto(projeto)


class RepositorioParticipacoes:
    """ Classe que representa um repositório de participações."""

    def __init__(self):
        self.participacoes = []

    def adicionar_participacao(self, participacao):
        if participacao.aluno.matricula in [p.aluno.matricula for p in self.participacoes if p.projeto.codigo == participacao.projeto.codigo]:
            raise ValueError("Esse aluno já está cadastrado nesse projeto.")
        self.participacoes.append(participacao)

    def listar_participacoes(self):
        return self.participacoes
    
    def salvar_participacoes(self):
        with open(CAMINHO_PARTICIPACOES, "w", encoding='utf-8') as arquivo:
            for participacao in self.participacoes:
                arquivo.write(
                    f"{participacao.codigo},{participacao.data_inicio},{participacao.data_fim},{participacao.aluno.matricula},{participacao.projeto.codigo}\n")

    def carregar_participacoes(self, repositorio_alunos, repositorio_projetos):
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
    