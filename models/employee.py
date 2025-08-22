class Employee:
    def __init__(self, employee_id, last_name, first_name, title, reports_to, birth_date, hire_date, address, city, state, country, postal_code, phone, fax, email):
        self.employee_id = employee_id
        self.last_name = last_name
        self.first_name = first_name
        self.title = title
        self.reports_to = reports_to
        self.birth_date = birth_date
        self.hire_date = hire_date
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.postal_code = postal_code
        self.phone = phone
        self.fax = fax
        self.email = email

    def __repr__(self):
        return f"Employee({self.employee_id}, {self.last_name}, {self.first_name}, {self.title}, {self.reports_to}, {self.birth_date}, {self.hire_date}, {self.address}, {self.city}, {self.state}, {self.country}, {self.postal_code}, {self.phone}, {self.fax}, {self.email})"
