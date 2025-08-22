class Customer:
    def __init__(self, customer_id, first_name, last_name, company, address, city, state, country, postal_code, phone, fax, email, support_rep_id):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.postal_code = postal_code
        self.phone = phone
        self.fax = fax
        self.email = email
        self.support_rep_id = support_rep_id

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.first_name}, {self.last_name}, {self.company}, {self.address}, {self.city}, {self.state}, {self.country}, {self.postal_code}, {self.phone}, {self.fax}, {self.email}, {self.support_rep_id})"
