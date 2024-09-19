# To-Do List com Interface Gráfica em Python

Este é um simples aplicativo de To-Do List desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica e SQLite para o armazenamento de dados. Ele permite que você adicione, remova, edite e marque tarefas como concluídas.

## Funcionalidades

Adicionar Tarefas: Insira uma nova tarefa no campo de texto e clique no botão "Add Task".
Excluir Tarefas: Selecione uma tarefa da lista e clique em "Delete Task" para removê-la.
Marcar Tarefas como Concluídas: Selecione uma tarefa e clique em "Complete Task" para marcar como concluída.
Persistência de Dados: As tarefas são armazenadas em um banco de dados SQLite, garantindo que elas não sejam perdidas ao fechar o aplicativo.

## Tecnologias Utilizadas

- Python 3
- Tkinter – Biblioteca padrão para a criação de interfaces gráficas.
- SQLite – Banco de dados embutido para persistir as tarefas.

## Instalação

- Clone o repositório:

git clone https://github.com/seu-usuario/todo-list-python.git

- Acesse o diretório do projeto:

cd todo-list-python

- Execute o arquivo principal:

python todo_list.py

### Nota: Certifique-se de que você tem o Python 3 instalado em sua máquina. Tkinter e SQLite vêm pré-instalados com a maioria das distribuições Python, então você não deve precisar instalar bibliotecas adicionais.

## Estrutura do Projeto

todo_list.py – Arquivo principal que contém a lógica do aplicativo e a interface gráfica.
todo_list.db – Arquivo de banco de dados SQLite (gerado automaticamente ao rodar o aplicativo pela primeira vez).

## Como Usar

- Adicionar Tarefas:

Digite uma nova tarefa no campo de entrada e clique em "Add Task".

- Excluir Tarefas:

Selecione a tarefa na lista e clique em "Delete Task" para removê-la.

- Marcar como Concluída:

Selecione a tarefa na lista e clique em "Complete Task". Ela será marcada como concluída na lista.

## Melhorias Futuras

Algumas ideias para expandir o projeto incluem:

Adicionar funcionalidade de edição de tarefas.
Implementar categorias de tarefas.
Criar um histórico de tarefas concluídas.
Adicionar filtro para tarefas concluídas/não concluídas.
Contribuições
Contribuições são bem-vindas! Se você tiver alguma ideia ou melhoria, fique à vontade para abrir um pull request ou relatar um problema.

### Licença
### Este projeto está licenciado sob a MIT License.
