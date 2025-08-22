from models.repos.customer_repo import CustomerRepo
from models.customer import Customer

def view_customers():
    """Fetches and displays all customers."""
    try:
        repo = CustomerRepo()
        all_customers = repo.get_all_customers()
        if not all_customers:
            print("No customers found.")
        else:
            print("Customers Table Data \n----------------")
            for customer in all_customers:
                print(f"ID: {customer.customer_id}, Name: {customer.first_name} {customer.last_name}, Company: {customer.company}, Address: {customer.address}, City: {customer.city}, State: {customer.state}, Country: {customer.country}, PostalCode: {customer.postal_code}, Phone: {customer.phone}, Fax: {customer.fax} , Email: {customer.email}, SupportRepid: {customer.support_rep_id}")
    except Exception as e:
        print(f"An error occurred: {e}")


def view_customer_by_id(customer_id: int):
    """Fetches and displays a customer by ID."""
    try:
        repo = CustomerRepo()
        customer = repo.get_customer(customer_id)
        if customer:
            print(f"ID: {customer.customer_id}, Name: {customer.first_name} {customer.last_name}, Company: {customer.company}, Address: {customer.address}, City: {customer.city}, State: {customer.state}, Country: {customer.country}, PostalCode: {customer.postal_code}, Phone: {customer.phone}, Fax: {customer.fax} , Email: {customer.email}, SupportRepid: {customer.support_rep_id}")
        else:
            print(f"No customer found with ID {customer_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_customer():
    """Create a new customer."""
    try:
        customer_id = int(input("Enter Customer ID: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        company = input("Enter Company: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        country = input("Enter Country: ")
        postal_code = input("Enter Postal Code: ")
        phone = input("Enter Phone: ")
        fax = input("Enter Fax: ")
        email = input("Enter Email: ")
        support_rep_id = int(input("Enter Support Rep ID: "))
        new_customer = Customer(customer_id, first_name, last_name, company, address, city, state, country, postal_code, phone, fax, email, support_rep_id)
        repo = CustomerRepo()
        repo.create_customer(new_customer)
        view_customers()
    except Exception as e:
        print(f"An error occurred: {e}")


def update_customer():
    """Update an existing customer."""
    try:
        customer_id = int(input("Enter Customer ID to update: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        company = input("Enter Company: ")
        
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        country = input("Enter Country: ")
    
        postal_code = input("Enter Postal Code: ")
        phone = input("Enter Phone: ")
        fax = input("Enter Fax: ")
        email = input("Enter Email: ")
        support_rep_id = int(input("Enter Support Rep ID: "))
        updated_customer = Customer(customer_id, first_name, last_name, company, address, city, state, country, postal_code, phone, fax, email, support_rep_id)
        repo = CustomerRepo()
        repo.update_customer(customer_id, updated_customer)
        view_customers()
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_customer():
    """Delete a customer."""
    try:
        customer_id = int(input("Enter Customer ID to delete: "))
        repo = CustomerRepo()
        repo.delete_customer(customer_id)
        view_customers()
    except Exception as e:
        print(f"An error occurred: {e}")

def customer_main():
    """Main function to manage customer operations."""
    while True:
        print("\nCustomer Management Menu")
        print("1. View All Customers")
        print("2. View Customer by ID")
        print("3. Create Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_customers()
        elif choice == '2':
            customer_id = int(input("Enter Customer ID: "))
            view_customer_by_id(customer_id)
        elif choice == '3':
            create_customer()
        elif choice == '4':
            update_customer()
        elif choice == '5':
            delete_customer()
        elif choice == '0':
            print("Exiting Customer Management.")
            break
        else:
            print("Invalid choice, please try again.")        
    
if __name__ == "__main__":
    customer_main()
   