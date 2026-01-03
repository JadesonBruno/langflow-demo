# LangFlow Demo 🚀

Demonstração prática de integração com LangFlow via API REST. Este projeto ilustra como fazer requisições a flows do LangFlow executando localmente via Docker.

## 📋 Sobre o Projeto

Este projeto é uma demo de integração com [LangFlow](https://github.com/logspace-ai/langflow), uma ferramenta open-source para criação visual de fluxos de LLM (Large Language Models). O código Python demonstra como:

- Configurar autenticação via variáveis de ambiente
- Fazer requisições POST para executar flows do LangFlow
- Processar e exibir respostas da API
- Tratar erros de conexão e autenticação

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **Requests** - Cliente HTTP para chamadas à API
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **LangFlow** - Framework visual para fluxos de LLM
- **Docker** - Containerização do servidor LangFlow
- **Poetry** - Gerenciamento de dependências

## 📦 Pré-requisitos

- Python 3.12 ou superior
- Poetry instalado
- Docker (para executar o servidor LangFlow)

## 🚀 Instalação e Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/JadesonBruno/langflow-demo.git
cd langflow-demo
```

### 2. Configurar Ambiente Virtual com Poetry

```bash
# Configurar Poetry para criar venv no projeto
poetry config virtualenvs.in-project true

# Instalar dependências
poetry install
```

### 3. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
LANGFLOW_API_KEY=your_api_key_here
```

### 4. Executar o Servidor LangFlow via Docker

#### Opção 1: Docker Run

```bash
docker run --rm -p 7860:7860 -e LANGFLOW_API_KEY=your_key ghcr.io/langflow/langflow:latest
```

#### Opção 2: Docker Compose

Crie um arquivo `docker-compose.yml`:

```yaml
version: "3.8"
services:
  langflow:
    image: ghcr.io/langflow/langflow:latest
    ports:
      - "7860:7860"
    environment:
      - LANGFLOW_API_KEY=${LANGFLOW_API_KEY}
    volumes:
      - ./data:/app/data
```

Execute:

```bash
docker-compose up -d
```

### 5. Acessar a Interface do LangFlow

Abra o navegador em: `http://localhost:7860`

Crie ou importe uma flow e copie o ID da flow para usar no script.

## 💻 Uso

### Executar o Script de Teste

```bash
poetry run python src/test.py
```

### Estrutura do Código

O arquivo [`src/test.py`](src/test.py) contém:

- **Carregamento de variáveis**: Leitura da `LANGFLOW_API_KEY` do arquivo `.env`
- **Configuração da requisição**: Definição do endpoint, payload e headers
- **Execução da chamada**: POST para o endpoint da flow com autenticação Bearer
- **Tratamento de resposta**: Exibição de status, headers e corpo da resposta
- **Tratamento de erros**: Captura de exceções de requisição e parsing

### Exemplo de Payload

```python
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "Quanto é 2 + 2?",
}
```

### Exemplo de Resposta

```json
{
  "status": "success",
  "result": "2 + 2 é igual a 4."
}
```

## 🔧 Gerenciamento do Ambiente Virtual

### Recriar o .venv com Poetry

Se precisar recriar o ambiente virtual:

```powershell
# Remover ambiente existente
Remove-Item -Recurse -Force .venv

# Configurar Poetry (se ainda não configurado)
poetry config virtualenvs.in-project true

# Recriar e instalar dependências
poetry install
```

## 📁 Estrutura do Projeto

```
langflow-demo/
├── src/
│   └── test.py          # Script de teste da API
├── .env                 # Variáveis de ambiente (não versionado)
├── pyproject.toml       # Configuração do Poetry e dependências
├── README.md            # Documentação do projeto
└── LICENSE              # Licença MIT
```

## 🐛 Troubleshooting

### Erro: LANGFLOW_API_KEY não definida

Certifique-se de que o arquivo `.env` existe e contém a chave:

```env
LANGFLOW_API_KEY=sua_chave_aqui
```

### Erro: Connection Refused

Verifique se o servidor LangFlow está rodando:

```bash
docker ps
```

Deve aparecer um container na porta 7860.

### Erro: Flow ID Inválido

- Acesse http://localhost:7860
- Abra a flow desejada
- Copie o ID correto da URL ou da interface
- Atualize a variável `url` em [`src/test.py`](src/test.py)

## 🔐 Segurança

⚠️ **Nunca commite o arquivo `.env` com suas chaves de API!**

Adicione ao `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

## 📚 Recursos Adicionais

- [Documentação LangFlow](https://docs.langflow.org/)
- [API Reference LangFlow](https://docs.langflow.org/api-reference)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Requests Documentation](https://requests.readthedocs.io/)

## 📞 Suporte e Contato

**Jadeson Bruno**
- 📧 Email: jadesonbruno.a@outlook.com
- 🐙 GitHub: [@JadesonBruno](https://github.com/JadesonBruno)
- 💼 LinkedIn: [Jadeson Bruno](https://www.linkedin.com/in/jadeson-silva/)

---

⭐ **Se este projeto foi útil, deixe uma estrela no repositório!**

📝 **Licença**: MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
