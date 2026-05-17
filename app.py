from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
tasks = [
    {"id": 1, "title": "Learn Python", "done": True},
    {"id": 2, "title": "Learn Docker", "done": False},
    {"id": 3, "title": "Build REST API", "done": True},
]

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# GET single task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# POST create new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title", "Untitled"),
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# PUT update task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        data = request.get_json()
        task["title"] = data.get("title", task["title"])
        task["done"] = data.get("done", task["done"])
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# DELETE task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
