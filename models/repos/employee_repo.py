from models.employee import Employee
from models.repos.a_employee import AEmployee
import sqlite3

class EmployeeRepo(AEmployee):
    def create_employee(self, model: Employee) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute("""
                    INSERT INTO employees (EmployeeId, FirstName, LastName, Title, ReportsTo, BirthDate, HireDate, Address, City, State, Country, PostalCode, Phone, Fax, Email)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (model.employee_id, model.first_name, model.last_name, model.title, model.reports_to, model.birth_date, model.hire_date, model.address, model.city, model.state, model.country, model.postal_code, model.phone, model.fax, model.email))

        except sqlite3.Error as e:
            print(f"Error occurred: {e}")
        
    
    def update_employee(self, emp_id: int, model: Employee) -> None:
        with sqlite3.connect("chinook.db") as conn:
            conn.execute("""
                UPDATE employees
                SET  FirstName = ?, LastName = ?, Title = ?, ReportsTo = ?, BirthDate = ?, HireDate = ?, Address = ?, City = ?, State = ?, Country = ?, PostalCode = ?, Phone = ?, Fax = ?, Email = ?
                WHERE EmployeeId = ?
            """, ( model.first_name, model.last_name, model.title, model.reports_to, model.birth_date, model.hire_date, model.address, model.city, model.state, model.country, model.postal_code, model.phone, model.fax, model.email, emp_id))
            conn.commit()

    def delete_employee(self, emp_id: int) -> None:
        with sqlite3.connect("chinook.db") as conn:
            conn.execute("DELETE FROM employees WHERE EmployeeId = ?", (emp_id,))
            conn.commit()

    def get_employee(self, emp_id: int) -> Employee:
        with sqlite3.connect("chinook.db") as conn:
            cursor = conn.execute(f"SELECT * FROM employees WHERE EmployeeId = {emp_id}")
            row = cursor.fetchone()
            if row:
                return Employee(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]
                )
            else:
                print(f"No employee found with ID {emp_id}")

    def get_all_employees(self) -> list[Employee]:
        employees = []
        with sqlite3.connect("chinook.db") as conn:
            cursor = conn.execute("SELECT * FROM employees")
            for row in cursor:
                employees.append(Employee(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]
                ))
        return employees
