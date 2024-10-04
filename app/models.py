from enum import Enum
from .db import get_db_connection


class User_Function(Enum):
    MANAGER = "Manager"
    ENGINEER = "Engineer"
    TECHNICIAN = "Technician"
    ADMINISTRATOR = "Administrator"
    SECRETAIRE = "Secretaire"
    INFORMATICIEN = "Informaticien"
    COMPTABLE = "Comptable",
    DIRECTEUR = "Directeur"
   
 
class Departement(Enum):
    INFORMATIQUE = "Informatique"
    ADMINISTRATION = "Administraction"
    FINANCE = "Finance"
    TECHNIQUE = "Technique"
    COMMERCIAL = "Commercial"
    COMMUNICATION = "Communication"
    RESSOURCESHUMAIN = "Ressources-Humain"
    

class Employee:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees")
        employees = cur.fetchall()
        cur.close()
        conn.close()
        return employees

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees WHERE id = %s", (id,))
        employee = cur.fetchone()
        cur.close()
        conn.close()
        return employee

    @staticmethod
    def get_by_name(name):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees WHERE name = %s", (name,))
        employees = cur.fetchall()
        cur.close()
        conn.close()
        return employees

    @staticmethod
    def get_by_province(province):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees WHERE province = %s", (province,))
        employees = cur.fetchall()
        cur.close()
        conn.close()
        return employees

    @staticmethod
    def get_by_function(fonction):
        if fonction not in [f.value for f in User_Function]:
            raise ValueError("Fonction invalide")
        conn = get_db_connection()
        cur = conn.cursor()
        query = "SELECT * FROM employees WHERE function = %s"
        cur.execute(query, (fonction,))
        employees = cur.fetchall()
        cur.close()
        conn.close()
        return employees

    @staticmethod
    def get_by_department(department):
        if department not in [d.value for d in Departement]:
            raise ValueError('Département invalide')
        conn = get_db_connection()
        cur = conn.cursor()
        query = "SELECT * FROM employees WHERE department = %s"
        cur.execute(query, (department,))
        employees = cur.fetchall()
        cur.close()
        conn.close()
        return employees

    @staticmethod
    def create(name, middle_name, first_name, fonction,
               department, province, 
               age, matricule, address):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO employees (name, middle_name, first_name, 
            fonction, 
            department, province, age, matricule, address) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id""",
            (name, middle_name, first_name, 
             fonction.value, department, 
             province, age, matricule, address)
        )
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return id

    @staticmethod
    def update(id, name, middle_name, first_name, function, department, 
               province, age, matricule, address):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            """UPDATE employees SET name = %s, middle_name = %s, 
            first_name = %s, function = %s, department = %s, province = %s, 
            age = %s, matricule = %s, address = %s WHERE id = %s""",
            (name, middle_name, first_name, function.value, 
             department, province, age, matricule, address, id)
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM employees WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
