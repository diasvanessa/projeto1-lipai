class Projeto:
    """Classe que representa um projeto, codigo (int), titulo, 
    responsavel, lista de participacoes"""

    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError(
                "O código do projeto deve ser um inteiro positivo.")
        self._codigo = valor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor:
            raise ValueError("O título do projeto não pode ser vazio.")
        self._titulo = valor

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        if not valor:
            raise ValueError("O responsável pelo projeto não pode ser vazio.")
        self._responsavel = valor

    def adicionar_participacao(self, participacao):
        self.participacoes.append(participacao)

    @classmethod
    def from_string(cls, rep_projeto):
        codigo, titulo, responsavel = rep_projeto.split(sep=",")
        codigo = int(codigo)
        return cls(codigo, titulo, responsavel)

    def __hash__(self):
        return hash(self.codigo)

    def __repr__(self):
        return f"Projeto(codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel})"

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return value.codigo == self.codigo
        return False

    def __str__(self):
            texto = f"Projeto {self.codigo}: {self.titulo} (Resp: {self.responsavel})"
            if self.participacoes:
                texto += "\n   Participações:"
                for p in self.participacoes:
                    texto += f"\n    -> {p}" 
            else:
                texto += "\n   (Nenhuma participação cadastrada)"
            return texto