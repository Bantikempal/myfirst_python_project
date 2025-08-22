from models.invoice_item import Invoice_Item
from models.repos.a_invoice_item import A_Invoice_Item
import sqlite3


class Invoice_Item_Repo(A_Invoice_Item):
    def create_invoice_item(self, model: Invoice_Item) -> None:
        with sqlite3.connect("chinook.db") as conn:
            conn.execute(f"""
                INSERT INTO invoice_items VALUES (
                    {model.invoice_item_id},
                    '{model.invoice_id}',
                    {model.track_id},
                    {model.unitprice},
                    {model.quantity}
                )
            """)
            conn.commit()

    def update_invoice_item(self, inv_item_id: int, model: Invoice_Item) -> None:
        with sqlite3.connect("chinook.db") as conn:
            conn.execute(f"""
                UPDATE invoice_items
                SET InvoiceID = '{model.invoice_id}',
                    TrackId = {model.track_id},
                    UnitPrice = {model.unitprice},
                    Quantity = {model.quantity}
                WHERE InvoiceLineId = {inv_item_id}
            """)
            conn.commit()

    def delete_invoice_item(self, inv_item_id: int) -> None:
        with sqlite3.connect("chinook.db") as conn:
            conn.execute(f"DELETE FROM invoice_items WHERE InvoiceLineId = {inv_item_id}")
            conn.commit()

    def get_invoice_item(self, inv_item_id: int) -> Invoice_Item:
        with sqlite3.connect("chinook.db") as conn:
            cursor = conn.execute("SELECT * FROM invoice_items WHERE InvoiceLineId = ?", (inv_item_id,))
            row = cursor.fetchone()
            if row:
                return Invoice_Item(
                    invoice_item_id=row[0],
                    invoice_id=row[1],
                    track_id=row[2],
                    unitprice=row[3],
                    quantity=row[4]
                )
            else:
                print(f"No invoice item found with ID {inv_item_id}")

    def get_all_invoice_items(self) -> list[Invoice_Item]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM invoice_items")
                for row in cursor:
                    item = Invoice_Item(
                        invoice_item_id=row[0],
                        invoice_id=row[1],
                        track_id=row[2],
                        unitprice=row[3],
                        quantity=row[4]
                    )
                    data_list.append(item)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list


# View Layer

def view_invoice_items():
    """Fetches and displays all invoice items."""
    try:
        repo = Invoice_Item_Repo()
        all_items = repo.get_all_invoice_items()
        if not all_items:
            print("No Invoice Items found.")
        else:
            print("Invoice Items Table Data \n----------------")
            for item in all_items:
                print(f"Item ID: {item.invoice_item_id}, Invoice ID: {item.invoice_id}, Track ID: {item.track_id}, Unit Price: {item.unitprice}, Quantity: {item.quantity}")
    except Exception as e:
        print(f"An error occurred: {e}")


def view_invoice_item_by_id(item_id: int):
    """Fetches and displays an invoice item by ID."""
    try:
        repo = Invoice_Item_Repo()
        item = repo.get_invoice_item(item_id)
        if item:
            print(f"Item ID: {item.invoice_item_id}, Invoice ID: {item.invoice_id}, Track ID: {item.track_id}, Unit Price: {item.unitprice}, Quantity: {item.quantity}")
        else:
            print(f"No Invoice Item found with ID {item_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_invoice_item():
    """Create an Invoice Item."""
    try:
        item_id = int(input("Enter Invoice Item ID: "))
        invoice_id = int(input("Enter Invoice ID: "))
        track_id = int(input("Enter Track ID: "))
        unit_price = float(input("Enter Unit Price: "))
        quantity = int(input("Enter Quantity: "))
        new_item = Invoice_Item(item_id, invoice_id, track_id, unit_price, quantity)
        repo = Invoice_Item_Repo()
        repo.create_invoice_item(new_item)
        view_invoice_items()
    except Exception as e:
        print(f"An error occurred: {e}")


def update_invoice_item():
    """Update an Invoice Item."""
    try:
        item_id = int(input("Enter Invoice Item ID to update: "))
        invoice_id = int(input("Enter new Invoice ID: "))
        track_id = int(input("Enter new Track ID: "))
        unit_price = float(input("Enter new Unit Price: "))
        quantity = int(input("Enter new Quantity: "))
        updated_item = Invoice_Item(item_id, invoice_id, track_id, unit_price, quantity)
        repo = Invoice_Item_Repo()
        repo.update_invoice_item(item_id, updated_item)
        view_invoice_items()
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_invoice_item():
    """Delete an Invoice Item."""
    try:
        item_id = int(input("Enter Invoice Item ID to delete: "))
        repo = Invoice_Item_Repo()
        repo.delete_invoice_item(item_id)
        view_invoice_items()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    print("Choose an option:")
    print("1. View all invoice items")
    print("2. View invoice item by ID")
    print("3. Create an invoice item")
    print("4. Update an invoice item")
    print("5. Delete an invoice item")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_invoice_items()
    elif choice == "2":
        try:
            item_id = int(input("Enter Invoice Item ID: "))
            view_invoice_item_by_id(item_id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
    elif choice == "3":
        create_invoice_item()
    elif choice == "4":
        update_invoice_item()
    elif choice == "5":
        delete_invoice_item()
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")
