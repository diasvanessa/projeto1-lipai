# projeto1-lipai

Projeto A – Sistema de Gestão de Alunos e Projetos de IC  
Este sistema foi desenvolvido para organizar o cadastro de alunos, projetos e suas participações,
facilitando o gerenciamento das informações de forma simples e centralizada.

# Funcionalidades
- Cadastro de alunos
- Cadastro de projetos
- Registro de participações de alunos em projetos
- Listagem de alunos e projetos cadastrados
- Busca de alunos, projetos e alunos participantes de um projeto ou projetos que o aluno participa
- Menu interativo via terminal

# Como executar o projeto

1. Certifique-se de que o Python 3 esteja instalado em sua máquina.
2. Clone o repositório:
   ```bash
   git clone https://github.com/diasvanessa/projeto1-lipai
3. Acesse a pasta raiz do projeto:
   ```bash
    cd projeto1-lipai
5. Execute o arquivo principal com o comando:
   ```bash
    python src/main.py

# Estrutura de diretorios
```bash
projeto1-lipai/
├── .vscode/                # Configurações do VS Code
├── data/                   # Arquivos de dados do projeto
├── src/                    # Código-fonte principal
│   ├── __pycache__/        # Cache do Python
│   ├── models/             # Modelos de dados
│   │   ├── __pycache__/
│   │   ├── aluno.py        # Classe Aluno
│   │   ├── participacao.py # Classe Participacao
│   │   └── projeto.py     # Classe Projeto
│   ├── services/           # Regras de serviços
│   ├── main.py             # Arquivo principal de execução
│   └── menus.py            # Menus e interação com o usuário
├── .env                    # Variáveis de ambiente
└── README.md               # Documentação do projeto
