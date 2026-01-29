class Aluno:
    """Representa um aluno com nome, email e matrícula."""
    def __init__(self, matricula, nome, email):
        self.nome = nome
        self.email = email
        self.matricula = matricula
        
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("O nome não pode ser vazio.")
        self._nome = valor
        
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, valor):
        if "@" not in valor:
            raise ValueError("Email inválido.")
        self._email = valor
        
    @property
    def matricula(self):
        return self._matricula
    @matricula.setter
    def matricula(self, valor):
        if not valor:
            raise ValueError("A matrícula não pode ser vazia.")
        self._matricula = valor    
        
    @classmethod
    def from_string(cls, rep_aluno):
        matricula, nome, email = rep_aluno.split(sep=",")
        return cls(matricula, nome, email)
    def __hash__(self):
        return hash(self.matricula)
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.matricula == value.matricula
        return False
    def __str__(self):
        return f"Aluno: {self.nome}, Email: {self.email}, Matrícula: {self.matricula}"
    def __repr__(self):
        return f"Aluno(matricula={self.matricula}, nome={self.nome}, email={self.email})"
    
