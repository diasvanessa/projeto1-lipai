from models.aluno import Aluno
from models.projeto import Projeto
import uuid


class Participacao:
    """Classe que representa a participação de um aluno em um projeto,
    com codigo, data_inicio, data_fim, aluno, projeto"""

    def __init__(self, data_inicio, data_fim, aluno, projeto, codigo=None):
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto
        if codigo is None:
            self.codigo = uuid.uuid4().hex[:8]
        else:
            self.codigo = codigo

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        if not codigo:
            raise ValueError("O código da participação não pode ser vazio.")
        self._codigo = codigo

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio):
        if not isinstance(data_inicio, str) or not data_inicio.strip():
            raise ValueError("A data de início deve ser uma string não vazia.")
        self._data_inicio = data_inicio

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, data_fim):
        if not isinstance(data_fim, str) or not data_fim.strip():
            raise ValueError("A data de fim deve ser uma string não vazia.")
        if data_fim < self.data_inicio:
            raise ValueError("A data de fim não pode ser anterior à data de início.")
        self._data_fim = data_fim

    @property
    def aluno(self):
        return self._aluno

    @aluno.setter
    def aluno(self, aluno):
        if not isinstance(aluno, Aluno):
            raise ValueError("Aluno deve ser um objeto da classe Aluno.")
        self._aluno = aluno

    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, projeto):
        if not isinstance(projeto, Projeto):
            raise ValueError("Projeto deve ser um objeto da classe Projeto.")
        self._projeto = projeto

    @classmethod
    def from_string(cls, rep_participacao, aluno, projeto):
        codigo, data_inicio, data_fim = rep_participacao.split(sep=",")
        return cls(data_inicio, data_fim, aluno, projeto, codigo)

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return value.codigo == self.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def __str__(self):
        return (
            f"Participacao[codigo={self.codigo}, "
            f"data_inicio={self.data_inicio}, "
            f"data_fim={self.data_fim}, "
            f"aluno={self.aluno.matricula}, "
            f"projeto={self.projeto.codigo}]"
        )

    def __repr__(self):
        return (
            f"Participacao(codigo={self.codigo}, "
            f"data_inicio={self.data_inicio}, "
            f"data_fim={self.data_fim}, "
            f"aluno={repr(self.aluno)}, "
            f"projeto={repr(self.projeto)})"
        )
