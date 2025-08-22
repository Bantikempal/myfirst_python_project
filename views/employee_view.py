from models.employee import Employee
from models.repos.employee_repo import EmployeeRepo

def view_employees():
    """Fetch and display all employees."""
    repo = EmployeeRepo()
    employees = repo.get_all_employees()
    if employees:
        print("Employees:\n")
        for emp in employees:
            print(f"ID: {emp.employee_id}, Name: {emp.first_name} {emp.last_name}, Title: {emp.title}, Reports To: {emp.reports_to}, Birth Date: {emp.birth_date}, Hire Date: {emp.hire_date}, Address: {emp.address}, City: {emp.city}, State: {emp.state}, Country: {emp.country}, Postal Code: {emp.postal_code}, Phone: {emp.phone}, Fax: {emp.fax}, Email: {emp.email}")
    else:
        print("No employees found")
def view_employee_by_id(emp_id: int):
    """Fetch and display a single employee by ID."""
    repo = EmployeeRepo()
    employee = repo.get_employee(emp_id)
    if employee:
        print(f"ID: {employee.employee_id}, Name: {employee.first_name} {employee.last_name}, Title: {employee.title}, Reports To: {employee.reports_to}, Birth Date: {employee.birth_date}, Hire Date: {employee.hire_date}, Address: {employee.address}, City: {employee.city}, State: {employee.state}, Country: {employee.country}, Postal Code: {employee.postal_code}, Phone: {employee.phone}, Fax: {employee.fax}, Email: {employee.email}")
    else:
        print(f"No employee found with ID {emp_id}")

def view_create_employee():
    """Create a new employee."""
    emp_id = int(input("Enter Employee ID: "))
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    title = input("Enter Title: ")
    reports_to = int(input("Enter Reports To ID: "))
    birth_date = input("Enter Birth Date (YYYY-MM-DD): ")
    hire_date = input("Enter Hire Date (YYYY-MM-DD): ")
    address = input("Enter Address: ")
    city = input("Enter City: ")
    state = input("Enter State: ")
    country = input("Enter Country: ")
    postal_code = input("Enter Postal Code: ")
    phone = input("Enter Phone: ")
    fax = input("Enter Fax: ")
    email = input("Enter Email: ")

    new_employee = Employee(emp_id, first_name, last_name, title, reports_to, birth_date, hire_date, address, city, state, country, postal_code, phone, fax, email)
    repo = EmployeeRepo()
    repo.create_employee(new_employee)
    view_employees()


def view_update_employee():
    """Update an employee."""
    emp_id = int(input("Enter Employee ID to update: "))
    first_name = input("Enter New First Name: ")
    last_name = input("Enter New Last Name: ")
    title = input("Enter New Title: ")
    reports_to = int(input("Enter New Reports To ID: "))
    birth_date = input("Enter New Birth Date (YYYY-MM-DD): ")
    hire_date = input("Enter New Hire Date (YYYY-MM-DD): ")
    address = input("Enter New Address: ")
    city = input("Enter New City: ")
    state = input("Enter New State: ")
    country = input("Enter New Country: ")
    postal_code = input("Enter New Postal Code: ")
    phone = input("Enter New Phone: ")
    fax = input("Enter New Fax: ")
    email = input("Enter New Email: ")

    updated_employee = Employee(emp_id, first_name, last_name, title, reports_to, birth_date, hire_date, address, city, state, country, postal_code, phone, fax, email)
    repo = EmployeeRepo()
    repo.update_employee(emp_id, updated_employee)
    print("Employee updated successfully.")
    view_employees()

def view_delete_employee():
    """Delete an employee."""
    emp_id = int(input("Enter Employee ID to delete: "))
    repo = EmployeeRepo()
    repo.delete_employee(emp_id)
    print("Employee deleted successfully.")
    view_employees()


def employee_main():
    """Main function to manage employee operations."""
    while True:
        print("\nEmployee Management Menu")
        print("1. View All Employees")
        print("2. View Employee by ID")
        print("3. Create New Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_employees()
        elif choice == '2':
            emp_id = int(input("Enter Employee ID: "))
            view_employee_by_id(emp_id)
        elif choice == '3':
            view_create_employee()
        elif choice == '4':
            view_update_employee()
        elif choice == '5':
            view_delete_employee()
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
   employee_main()