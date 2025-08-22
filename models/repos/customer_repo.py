from models.customer import Customer
from models.repos.a_customer import ACustomer
import sqlite3

class CustomerRepo(ACustomer):
    def create_customer(self, model: Customer) -> None:
        with sqlite3.connect("chinook.db") as conn:
            conn.execute(f"""
                INSERT INTO customers (CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId)
                VALUES (
                    {model.customer_id},
                    '{model.first_name}',
                    '{model.last_name}',
                    '{model.company}',
                    '{model.address}',
                    '{model.city}',
                    '{model.state}',
                    '{model.country}',
                    '{model.postal_code}',
                    '{model.phone}',
                    '{model.fax}',
                    '{model.email}',
                    {model.support_rep_id}
                )
            """)
            conn.commit()

    def update_customer(self, customer_id: int, model: Customer) -> None:
        with sqlite3.connect("chinook.db") as conn:
            conn.execute(f"""
                UPDATE customers
                SET FirstName = '{model.first_name}',
                    LastName = '{model.last_name}',
                    Company = '{model.company}',
                    Address = '{model.address}',
                    City = '{model.city}',
                    State = '{model.state}',
                    Country = '{model.country}',
                    PostalCode = '{model.postal_code}',
                    Phone = '{model.phone}',
                    Fax = '{model.fax}',
                    Email = '{model.email}',
                    SupportRepId = {model.support_rep_id}
                WHERE CustomerId = {customer_id}
            """)
            conn.commit()

    def delete_customer(self, customer_id: int) -> None:
        with sqlite3.connect("chinook.db") as conn:
            conn.execute(f"DELETE FROM customers WHERE CustomerId = {customer_id}")
            conn.commit()

    def get_customer(self, customer_id: int) -> Customer:
        with sqlite3.connect("chinook.db") as conn:
            cursor = conn.execute("SELECT * FROM customers WHERE CustomerId = ?", (customer_id,))
            row = cursor.fetchone()
            if row:
                return Customer(*row)
            else:
                print(f"No customer found with ID {customer_id}")

    def get_all_customers(self) -> list[Customer]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM customers")
                for row in cursor:
                    customer = Customer(*row)
                    data_list.append(customer)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
