# 📝 API de Gerenciamento de Tasks

## Descrição do Projeto

Este repositório contém uma API acadêmica desenvolvida em **Flask** para gerenciamento de tarefas (**Tasks**).  
O objetivo principal é demonstrar a implementação de um **CRUD completo** (Create, Read, Update e Delete) utilizando rotas REST.  
As tasks são armazenadas em memória (lista Python), sendo uma solução simples para estudos e prototipagem.

---

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação utilizada.
- **Flask**: Framework web minimalista para criação da API.

---

## Fluxo da API

1. **Criar Task**  
   - Endpoint: `POST /tasks`  
   - Cria uma nova tarefa com título e descrição.

2. **Listar todas as Tasks**  
   - Endpoint: `GET /tasks`  
   - Retorna todas as tarefas criadas, junto com o total.

3. **Buscar Task por ID**  
   - Endpoint: `GET /tasks/<id>`  
   - Retorna apenas uma tarefa pelo seu identificador único.

4. **Atualizar Task**  
   - Endpoint: `PUT /tasks/<id>`  
   - Atualiza título, descrição e status de conclusão da tarefa.

5. **Deletar Task**  
   - Endpoint: `DELETE /tasks/<id>`  
   - Remove uma tarefa pelo seu identificador.

---

