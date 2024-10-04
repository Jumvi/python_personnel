from flask import jsonify, request
from . import app
from .models import Employee
import logging
import sys

# Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s : %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)




@app.route('/employe', methods=['GET'])
def get_employees():
    logger.info("Route '/' appelée")
    try:
        employees = Employee.get_all()
        logger.debug(f"Employés récupérés : {employees}")
        return jsonify(employees)
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des employés : {str(e)}")
        return jsonify({"error": "Une erreur s'est produite"}), 500


@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.get_by_id(id)
    if employee:
        return jsonify(employee)
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