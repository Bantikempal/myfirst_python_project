from abc import ABC, abstractmethod
from models.invoice_item import Invoice_Item

class A_Invoice_Item(ABC):
    @abstractmethod
    def create_invoice_item(self, model: Invoice_Item) -> None:
        pass

    @abstractmethod
    def update_invoice_item(self, inv_item_id: int, model: Invoice_Item) -> None:
        pass

    @abstractmethod
    def delete_invoice_item(self, inv_item_id: int) -> None:
        pass

    @abstractmethod
    def get_invoice_item(self, inv_item_id: int) -> Invoice_Item:
        pass

    @abstractmethod
    def get_all_invoice_items(self) -> list[Invoice_Item]:
        pass
