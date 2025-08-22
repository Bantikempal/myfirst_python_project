from models.repos.invoice_repo import InvoiceRepo
from models.invoice import Invoice


def view_invoices():
    """Fetches and displays all invoices."""
    try:
        repo = InvoiceRepo()
        all_invoices = repo.get_all_invoices()
        if not all_invoices:
            print("No Invoices found.")
        else:
            print("Invoices Table Data \n----------------")
            for invoice in all_invoices:
                print(f"Invoice ID: {invoice.invoice_id}, Customer ID: {invoice.customer_id}, Invoice Date: {invoice.invoice_date}, Billing Address: {invoice.billing_address}, City: {invoice.billing_city}, State: {invoice.billing_state},  Country: {invoice.billing_country}, Postal Code : {invoice.billing_postal_code}, Total: {invoice.total}")
    except Exception as e:
        print(f"An error occurred: {e}")


def view_invoice_by_id(invoice_id: int):
    """Fetches and displays an invoice by ID."""
    try:
        repo = InvoiceRepo()
        invoice = repo.get_invoice(invoice_id)
        if invoice:
            print(f"Invoice ID: {invoice.invoice_id}, Customer ID: {invoice.customer_id}, Invoice Date: {invoice.invoice_date}, Billing Address: {invoice.billing_address}, City: {invoice.billing_city}, State: {invoice.billing_state},  Country: {invoice.billing_country}, Postal Code : {invoice.billing_postal_code}, Total: {invoice.total}")
        else:
            print(f"No Invoice found with ID {invoice_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_invoice():
    """Create an Invoice."""
    try:
        invoice_id = int(input("Enter Invoice ID: "))
        customer_id = int(input("Enter Customer ID: "))
        invoice_date = input("Enter Invoice Date (YYYY-MM-DD): ")
        billing_address = input("Enter Billing Address: ")
        billing_city = input("Enter Billing City: ")
        billing_state = input("Enter Billing State: ")
        billing_country = input("Enter Billing Country: ")
        billing_postal_code = input("Enter Billing Postal Code: ")
        total = float(input("Enter Total: "))
        new_invoice = Invoice(invoice_id, customer_id, invoice_date, billing_address, billing_city, billing_state, billing_country, billing_postal_code, total)
        repo = InvoiceRepo()
        repo.create_invoice(new_invoice)
        view_invoices()
    except Exception as e:
        print(f"An error occurred: {e}")


def update_invoice():
    """Update an Invoice."""
    try:
        invoice_id = int(input("Enter Invoice ID: "))
        customer_id = int(input("Enter Customer ID: "))
        invoice_date = input("Enter Invoice Date (YYYY-MM-DD): ")
        billing_address = input("Enter Billing Address: ")
        billing_city = input("Enter Billing City: ")
        billing_state = input("Enter Billing State: ")
        billing_country = input("Enter Billing Country: ")
        billing_postal_code = input("Enter Billing Postal Code: ")
        total = float(input("Enter Total: "))
        updated_invoice = Invoice(invoice_id, customer_id, invoice_date, billing_address, billing_city, billing_state, billing_country, billing_postal_code, total)
        repo = InvoiceRepo()
        repo.update_invoice(invoice_id, updated_invoice)
        view_invoices()
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_invoice():
    """Delete an Invoice."""
    try:
        invoice_id = int(input("Enter Invoice ID to delete: "))
        repo = InvoiceRepo()
        repo.delete_invoice(invoice_id)
        view_invoices()
    except Exception as e:
        print(f"An error occurred: {e}")

def invoice_main():
    """Main menu for managing invoices."""
    while True:
        print("\nInvoice Management Menu")
        print("1. View All Invoices")
        print("2. View Invoice by ID")
        print("3. Create Invoice")
        print("4. Update Invoice")
        print("5. Delete Invoice")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_invoices()
        elif choice == '2':
            try:
                invoice_id = int(input("Enter Invoice ID: "))
                view_invoice_by_id(invoice_id)
            except ValueError:
                print("Invalid input. Please enter a valid integer for Invoice ID.")
        elif choice == '3':
            create_invoice()
        elif choice == '4':
            update_invoice()
        elif choice == '5':
            delete_invoice()
        elif choice == '0':
            print("Exiting Invoice Management Menu.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
   invoice_main()