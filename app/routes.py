from flask import jsonify, request
from app import app
from app.models import Employee

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.get_all()
    return jsonify([dict(zip(['id', 'name', 'position', 'department'], emp)) for emp in employees])

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.get_by_id(id)
    if employee:
        return jsonify(dict(zip(['id', 'name', 'position', 'department'], employee)))
    return jsonify({"error": "Employee not found"}), 404

@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    if not all(k in data for k in ('name', 'position', 'department')):
        return jsonify({"error": "Missing data"}), 400
    id = Employee.create(data['name'], data['position'], data['department'])
    return jsonify({"id": id, "message": "Employee created successfully"}), 201

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    if not all(k in data for k in ('name', 'position', 'department')):
        return jsonify({"error": "Missing data"}), 400
    Employee.update(id, data['name'], data['position'], data['department'])
    return jsonify({"message": "Employee updated successfully"})

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    Employee.delete(id)
    return jsonify({"message": "Employee deleted successfully"})