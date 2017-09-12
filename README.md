
API - Avaliação de Conhecimentos REST
====

Uma API desenvolvida em Python, utilizando Djando e DjangoRestFramework. 
Que expõe os dados disponíveis em https://goo.gl/WCMv3j utilizando uma
abordagem orientada a recursos e que atendea alguns requisitos...


    * GET /feiras/

    * POST /feiras/

    * POST /feiras/busca/

    * GET /feiras/{id}/

    * PUT /feiras/{id}/

    * DELETE /feiras/{id}/


---
Como executar?
---
1. Criar e ativar um [ambiente virtual](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
    * `mkvirtualenv feiras` para criar um virtualenv chamado feiras
    * `workon feiras` para ativar o virtualenv sempre que for trabalhar no projeto

2. Instalar as dependências
    * `pip install -r requirements.txt`

3. Depois de instaladas as dependências, basta executar o comando:
    * `python manage.py migrate` para gerar o banco de dados padrão (sqlite3)
    * `python manage.py runserver` para iniciar o servidor local.


---
Documentação
---

A documentação da API fica na raiz da aplição, ou seja, assim que você iniciar o servidor e abrir o link principal, irá visualizar toda a documentação.


---
Logs
---

Os logs da api estão sendo gravados no aruivo 'api_logs.log' na pasta 'logs' que fica na raiz do projeto.


---
Testes
---

    * 'python manage.py test' para executar todos os testes do projeto.
    * 'coverage run --source='.' manage.py test' para executar os testes com o coverage.
    * 'coverage report -m' para visualizar os dados do coverage no terminal.
    * 'coverage html' para vizualizar os resultados em páginas html, será criada uma pasta 'htmlcov', abra o arquivo 'index.html' que estará dentro dela.


---
Importando dados de arquivos CSV
---

Faremos a importação a partir de um command do django.

    * 'python manage.py csv_to_bd /endereco/do/arquivo.csv'
