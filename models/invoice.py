class Invoice:
    def __init__(self, invoice_id, customer_id, invoice_date, billing_address, billing_city, billing_state, billing_country, billing_postal_code, total):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.invoice_date = invoice_date
        self.billing_address = billing_address
        self.billing_city = billing_city
        self.billing_state = billing_state
        self.billing_country = billing_country
        self.billing_postal_code = billing_postal_code
        self.total = total

    def __repr__(self):
        return (f"Invoice ID = {self.invoice_id}, Customer ID = {self.customer_id}, Invoice Date = {self.invoice_date}, "
                f"Billing Address = {self.billing_address}, Billing City = {self.billing_city}, Billing State = {self.billing_state}, "
                f"Billing Country = {self.billing_country}, Billing Postal Code = {self.billing_postal_code}, Total = {self.total}")
