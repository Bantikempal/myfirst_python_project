class Invoice_Item:
    def __init__(self, invoice_item_id: int, invoice_id: int, track_id: int, unitprice: int,quantity:int ) :
        self.invoice_item_id = invoice_item_id
        self.invoice_id = invoice_id
        self.track_id = track_id
        self.unitprice = unitprice
        self.quantity = quantity
    def __repr__(self):
        return f"Invoice line Id = {self.invoice_item_id} , Invoice id = {self.invoice_id} , Track Id = {self.track_id} , Unitprcie = {self.unitprice} , quantity = {self.quantity})"
