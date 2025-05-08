# Encurtador de URL
Um serviço de encurtamento de URLs desenvolvido com Flask e MongoDB, permitindo que usuários convertam URLs longas em versões curtas e fáceis de compartilhar.

## Funcionalidades
- Encurtamento de URLs através de uma API simples
- Redirecionamento automático para a URL original
- Armazenamento persistente no MongoDB
- Prevenção de duplicatas (a mesma URL original gera o mesmo código curto)

## Tecnologias utilizadas
- Python 3
- Flask
- MongoDB
- Flask-PyMongo

## Pré-requisitos
- Python 3.x instalado
- MongoDB rodando localmente ou acesso a um cluster remoto
- Gerenciador de pacotes pip

## Configuração do ambiente
### 1) Clone o repositório:
```bash
git clone https://github.com/LuisMig-code/url-shortener.git
cd url-shortener
```

### 2) Crie e ative um ambiente virtual (opcional mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```

### 3) Instale as dependências:
```bash
pip install -r requirements.txt
```

### 4) Configure a conexão com o MongoDB:
- Crie um arquivo .env na raiz do projeto
- Defina a variável MONGO_URI com sua string de conexão:
```
MONGO_URI=mongodb://usuario:senha@localhost:27017/banco_de_dados
```
- Ou use a configuração padrão (requer MongoDB local com autenticação)

## Executando a aplicação:
``` bash
python app.py
```

A aplicação estará disponível em http://localhost:5000

## Uso:
### 1) Acesse a página inicial (/) para ver a interface web
### 2) Para usar a API diretamente:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"url":"SUA_URL_AQUI"}' http://localhost:5000/shorten
```

### 3) Acesse a URL curta gerada para ser redirecionado à URL original

## Estrutura do projeto:
app.py: Aplicação principal Flask
requirements.txt: Dependências do projeto
templates/: Páginas HTML (inclui index.html para a interface web)
.env: Arquivo para variáveis de ambiente (não versionado)

## Contribuição:
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença:
MIT





