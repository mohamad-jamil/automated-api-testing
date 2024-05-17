from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

tasks = []

def generate_documentation():
    documentation = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            endpoint = app.view_functions[rule.endpoint]
            docstring = endpoint.__doc__ if endpoint.__doc__ else "No documentation available"
            documentation.append({
                'url': rule.rule,
                'methods': ', '.join(rule.methods),
                'docstring': docstring.strip()
            })

    return documentation

# GET: root page
@app.route('/')
def api_documentation():
    """
    Renders the API documentation page, listing all available endpoints
    along with their descriptions.
    """
    documentation = generate_documentation()
    return render_template('api_documentation.html', documentation=documentation)

# POST: new task
@app.route('/tasks', methods=['POST'])
def create_task():
    """
    Creates a new task.
    """
    data = request.json
    if 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data.get('description', ''),
        'completed': False
    }
    tasks.append(task)
    return jsonify({'message': 'Task created successfully', 'task': task}), 201

# GET: all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Retrieves all tasks.
    """
    completedParam = request.args.get('completed')
    if completedParam is not None:
        if completedParam.lower() in ['true', 'false']:
            completed = completedParam.lower() == 'true'
            return jsonify({'tasks': [task for task in tasks if task['completed'] == completed]})
        else:
            return jsonify({'error': f'Unexpected parameter value for \'completed\': {completedParam}'})
    return jsonify({'tasks': tasks})
        
# GET: task count
@app.route('/tasks/count', methods=['GET'])
def get_num_tasks():
    """
    Retrieves the number of tasks.
    """
    return jsonify({'message': f'There are currently {len(tasks)} tasks.'})

# GET: task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """
    Retrieves a specific task by its ID.
    """
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'task': task})

# PUT: update task by ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Updates an existing task.
    """
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    data = request.json
    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])
    task['completed'] = data.get('completed', task['completed'])
    return jsonify({'message': 'Task updated successfully', 'task': task})

# PUT: mark task as complete
@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def mark_task_complete(task_id):
    """
    Marks a task as complete by its ID.
    """
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task['completed'] = True
    return jsonify({'message': 'Task updated successfully', 'task': task})

# PUT: mark task as incomplete
@app.route('/tasks/<int:task_id>/incomplete', methods=['PUT'])
def mark_task_incomplete(task_id):
    """
    Marks a task as incomplete by its ID.
    """
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task['completed'] = False
    return jsonify({'message': 'Task updated successfully', 'task': task})

# DELETE: all tasks
@app.route('/tasks', methods=['DELETE'])
def delete_tasks():
    """
    Deletes all tasks.
    """
    global tasks
    tasks = []
    return jsonify({'message': 'Tasks deleted successfully'})

# DELETE: task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Deletes a specific task by its ID.
    """
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)