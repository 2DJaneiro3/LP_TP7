Topics - Aplicação Web Django

==============================

Descrição da Aplicação
-----------------------
Este projeto é uma aplicação web de gestão de tópicos de discussão, semelhante a um fórum ou plataforma colaborativa. O objetivo é permitir que os utilizadores possam criar tópicos, interagir com comentários e visualizar discussões organizadas por tópicos. A aplicação foi construída utilizando o **Django** (versão mínima 4.0), um dos frameworks Python mais robustos para o desenvolvimento de aplicações web.

Funcionalidades
---------------
- **Autenticação de Utilizadores:** Permite que os utilizadores criem uma conta e façam login para interagir na plataforma.
- **Gestão de Tópicos:** Os utilizadores podem criar, editar e eliminar tópicos de discussão. Apenas o autor do tópico pode editá-lo ou eliminá-lo.
- **Comentários nos Tópicos:** Os utilizadores podem adicionar, editar e eliminar comentários dentro de um tópico. Novamente, a eliminação e edição de comentários só são permitidas para o autor do comentário.
- **Listagem de Tópicos:** A página inicial exibe uma lista de tópicos disponíveis, com título, descrição e data de criação.
- **Detalhes do Tópico:** Ao clicar num tópico, o utilizador é redirecionado para uma página que exibe os detalhes do tópico, incluindo todos os comentários relacionados.

Tecnologias Utilizadas
----------------------
- **Django:** Framework web Python utilizado para criar a aplicação.
- **Python:** Linguagem de programação utilizada no backend.
- **SQLite:** Base de dados relacional utilizada (padrão do Django, ideal para desenvolvimento local).
- **django-crispy-forms:** Biblioteca para melhorar o design e a usabilidade dos formulários.
- **HTML/CSS:** Para renderizar as páginas web e estruturar o layout.
- **Bootstrap:** Framework CSS para estilizar as páginas e tornar a interface mais atraente.

Fluxo da Aplicação
------------------
1. **Página de Login/Registo:** Utilizadores podem registar-se ou fazer login na plataforma.
2. **Página Inicial:** A página inicial exibe a lista de tópicos. Cada tópico tem um título e uma descrição.
3. **Detalhes do Tópico:** Clicando num tópico, o utilizador é redirecionado para uma página que exibe os detalhes do tópico e os comentários associados.
4. **Formulários de Criação e Edição:** Utilizadores podem criar novos tópicos ou adicionar comentários. Apenas o autor do tópico ou comentário pode editá-los ou eliminá-los.

Como a Aplicação Funciona
-------------------------
A aplicação foi dividida em várias views, cada uma responsável por uma ação específica. As views são associadas às URLs, e os dados são manipulados utilizando o ORM do Django, garantindo fácil interação com a base de dados.

- **Tópicos:** Cada tópico tem um título, descrição, autor e data de criação.
- **Comentários:** Cada comentário está associado a um tópico específico e tem um autor e conteúdo.

A aplicação também conta com validação e verificação de permissões, como garantir que o utilizador que criou um tópico ou comentário seja o único capaz de editá-lo ou eliminá-lo.

Funcionalidades em Detalhe
---------------------------
Autenticação de Utilizadores
- **Login e Registo:** A aplicação permite que os utilizadores criem contas, façam login e logout. O acesso a funcionalidades como criação e edição de tópicos requer que o utilizador esteja autenticado.

CRUD de Tópicos e Comentários
- **Criar, Editar, Eliminar:** Utilizadores autenticados podem criar novos tópicos, editar os existentes e eliminá-los, mas apenas o autor pode editar ou eliminar os seus próprios tópicos.
- **Comentários:** Da mesma forma, comentários podem ser adicionados a tópicos e editados/eliminados apenas pelos seus autores.

Design Responsivo
- **Utilização do Bootstrap:** A interface foi criada utilizando o Bootstrap para garantir que a aplicação seja responsiva e se adapte a dispositivos móveis.

==============================================

# Como Instalar e Configurar a Aplicação Topics

Este guia explica como configurar e executar a aplicação **Topics** localmente no pc. Segue as instruções abaixo para garantir que a aplicação funciona corretamente no teu ambiente de desenvolvimento.

### Pré-requisitos

Antes de começar, precisamos de ter as seguintes ferramentas instaladas:

- **Python 3.8 ou +** - Para executar a aplicação e gerir dependências.
- **pip** - Gestor de pacotes do Python.
- **git** - Para clonar o repositório e gerir o código-fonte.

Caso ainda não tenhas essas ferramentas instaladas, podes baixá-las nos seguintes links:

- [Download Python] - (https://www.python.org/downloads/)
- [Download Git] - (https://git-scm.com/downloads)

---

### Passo 1: Clonar o Repositório
Primeiro, clonamos o repositório para o computador, utilizando o Git. No terminal (ou prompt de comando), executa os seguintes comandos:

git clone https://github.com/2DJaneiro3/LP_TP7.git
cd LP_TP7

### Passo 2: Criar e Ativar o Ambiente Virtual
Recomenda-se utilizar um ambiente virtual Python para isolar as dependências do projeto. 
Segue os passos abaixo para criar e ativar o ambiente virtual:

python -m venv venv
venv\Scripts\activate

Depois de ativado, verás o nome do ambiente virtual no prompt de comando, geralmente algo como (venv).

### Passo 3: Instalar as Dependências
Com o ambiente virtual ativado, instala as dependências necessárias que estão listadas no arquivo requirements.txt do projeto. Executa o seguinte comando:

pip install -r requirements.txt

Este comando irá instalar todas as bibliotecas necessárias para a aplicação funcionar corretamente, incluindo o Django e outras dependências.

### Passo 4: Configurar a base de Dados
A aplicação utiliza o banco de dados SQLite por padrão (configuração padrão do Django).
Para configurar a base de dados e aplicar as migrações necessárias, executa:

python manage.py migrate

Este comando cria as tabelas da base de dados de acordo com os modelos definidos no código.

### Passo 5: Criar um Superutilizador (Opcional, mas recomendado)
Para entrar o painel administrativo do Django e poder gerir os dados (como criar e editar tópicos), é necessário criar um superutilizador.
Para criar um superutilizador, executa o seguinte comando:

python manage.py createsuperuser

Segue as instruções para definir o nome de utilizador, e-mail e senha. Esse superutilizador pode ser utilizado para entrar no painel administrativo da aplicação.

### Passo 6: Rodar a Aplicação
Agora que tudo está configurado, podes iniciar o servidor de desenvolvimento do Django. 
Para isso, executa o comando:

python manage.py runserver

Este comando inicia o servidor local. A aplicação então estará acessível no navegador através do endereço:
http://127.0.0.1:8000/

### Passo 7: Testar a Aplicação
Podes testar a aplicação executando os testes unitários que já estão configurados por nós. 
Para executar os testes, usa o comando:

python manage.py test

Isto irá executar os testes definidos no código e irá garantir que as funcionalidades principais estejam funcionando corretamente.

---

## Conclusão
Agora a aplicação Topics deve estar a funcionar localmente! Podes começar a interagir com a plataforma, criando tópicos, comentando e gerenciando os dados.

Boa sorte e aproveita a aplicação! :)