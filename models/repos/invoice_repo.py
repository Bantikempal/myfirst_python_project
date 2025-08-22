from models.invoice import Invoice
from models.repos.a_invoice import AInvoice
import sqlite3


class InvoiceRepo(AInvoice):
    def create_invoice(self, model: Invoice) -> None:
        with sqlite3.connect("chinook.db") as conn:
            conn.execute(f"""
                INSERT INTO invoices VALUES (
                    {model.invoice_id},
                    {model.customer_id},
                    '{model.invoice_date}',
                    '{model.billing_address}',
                    '{model.billing_city}',
                    '{model.billing_state}',
                    '{model.billing_country}',
                    '{model.billing_postal_code}',
                    {model.total}
                )
            """)
            conn.commit()

    def update_invoice(self, invoice_id: int, model: Invoice) -> None:
        with sqlite3.connect("chinook.db") as conn:
            conn.execute(f"""
                UPDATE invoices
                SET CustomerId = {model.customer_id},
                    InvoiceDate = '{model.invoice_date}',
                    BillingAddress = '{model.billing_address}',
                    BillingCity = '{model.billing_city}',
                    BillingState = '{model.billing_state}',
                    BillingCountry = '{model.billing_country}',
                    BillingPostalCode = '{model.billing_postal_code}',
                    Total = {model.total}
                WHERE InvoiceId = {invoice_id}
            """)
            conn.commit()

    def delete_invoice(self, invoice_id: int) -> None:
        with sqlite3.connect("chinook.db") as conn:
            conn.execute(f"DELETE FROM invoices WHERE InvoiceId = {invoice_id}")
            conn.commit()

    def get_invoice(self, invoice_id: int) -> Invoice:
        with sqlite3.connect("chinook.db") as conn:
            cursor = conn.execute("SELECT * FROM invoices WHERE InvoiceId = ?", (invoice_id,))
            row = cursor.fetchone()
            if row:
                return Invoice(
                    invoice_id=row[0],
                    customer_id=row[1],
                    invoice_date=row[2],
                    billing_address=row[3],
                    billing_city=row[4],
                    billing_state=row[5],
                    billing_country=row[6],
                    billing_postal_code=row[7],
                    total=row[8]
                )
            else:
                print(f"No invoice found with ID {invoice_id}")

    def get_all_invoices(self) -> list[Invoice]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM invoices")
                for row in cursor:
                    invoice = Invoice(
                        invoice_id=row[0],
                        customer_id=row[1],
                        invoice_date=row[2],
                        billing_address=row[3],
                        billing_city=row[4],
                        billing_state=row[5],
                        billing_country=row[6],
                        billing_postal_code=row[7],
                        total=row[8]
                    )
                    data_list.append(invoice)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
