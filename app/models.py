from app import get_db_connection

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
    def create(name, position, department):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO employees (name, position, department) VALUES (%s, %s, %s) RETURNING id",
                    (name, position, department))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return id

    @staticmethod
    def update(id, name, position, department):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE employees SET name = %s, position = %s, department = %s WHERE id = %s",
                    (name, position, department, id))
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