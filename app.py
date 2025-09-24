from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__) #defino app como a variavel que vai armazenar o Flask criado nesse file

tasks = []
taskIdControl = 1

@app.route("/tasks", methods=["POST"]) #rota para criar uma task
def createTask():
    global taskIdControl #Torno a variavel disponivel para essa função
    data = request.get_json() #esse metodo recupera o que o cliente enviou
    newTask = Task(id=taskIdControl, title=data["title"], description=data["description"])
    taskIdControl += 1
    tasks.append(newTask)

    return jsonify({
        "id": newTask.id,
        "message": "Task created",
    })

@app.route("/tasks", methods=["GET"]) #rota para retornar todas as tasks
def getTasks():
    taskList = [task.toDict() for task in tasks] #crio uma nova lista e coloco um for dentro dela
    return jsonify({
        "tasks": taskList,
        "totalTasks": len(taskList),
    })

@app.route("/tasks/<int:id>", methods=["GET"]) #rota para retornar apenas uma única task
def getTask(id):
    taskList = [task.toDict() for task in tasks]
    for task in taskList:
        if task['id'] == id:
            return jsonify({
                "task": task,
            })

    return jsonify({
        "message": "Task not found",
    }), 404

@app.route("/tasks/<int:id>", methods=["PUT"])
def updateTask(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t

    if task == None:
        return jsonify({
            "message": "Task not found",
        }), 404

    data = request.get_json() #recuperamos o que o cliente enviou para nós
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]
    return jsonify({
        "id": task.id,
        "message": "Task updated",
    })

@app.route("/tasks/<int:id>", methods=["DELETE"])
def deleteTask(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t

    if not task: #se não houver a task
        return jsonify({
            "message": "Task not found",
        }), 404

    tasks.remove(task)
    return jsonify({
        "message": "Task deleted",
    })


if __name__ == "__main__": #estamos garantindo que só vamos subir o debug true quando estamos rodando apenas na maquina
    app.run(debug=True) #permite que informe varias coisas que estão ocorrendo nos logs