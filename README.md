# projeto1-lipai

Projeto A – Sistema de Gestão de Alunos e Projetos de IC  
Sistema para gerenciar alunos, projetos e participações em projetos de iniciação científica ou desenvolvimento.

## Como executar o projeto

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

### Estrutura de diretorios
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
