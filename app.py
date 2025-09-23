from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__) #defino app como a variavel que vai armazenar o Flask criado nesse file

tasks = []
taskIdControl = 1

@app.route("/tasks", methods=["POST"])
def createTask():
    global taskIdControl #Torno a variavel disponivel para essa função
    data = request.get_json() #esse metodo recupera o que o cliente enviou
    newTask = Task(id=taskIdControl, title=data["title"], description=data["description"])
    taskIdControl += 1
    tasks.append(newTask)

    return jsonify({
        "message": "Task created",
    })

@app.route("/tasks", methods=["GET"])
def getTasks():
    taskList = [task.toDict() for task in tasks] #crio uma nova lista e coloco um for dentro dela
    return jsonify({
        "tasks": taskList,
        "totalTasks": len(taskList),
    })

if __name__ == "__main__": #estamos garantindo que só vamos subir o debug true quando estamos rodando apenas na maquina
    app.run(debug=True) #permite que informe varias coisas que estão ocorrendo nos logs