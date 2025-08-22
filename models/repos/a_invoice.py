from abc import ABC, abstractmethod
from models.invoice import Invoice

class AInvoice(ABC):
    @abstractmethod
    def create_invoice(self, model: Invoice) -> None:
        pass

    @abstractmethod
    def update_invoice(self, invoice_id: int, model: Invoice) -> None:
        pass

    @abstractmethod
    def delete_invoice(self, invoice_id: int) -> None:
        pass

    @abstractmethod
    def get_invoice(self, invoice_id: int) -> Invoice:
        pass

    @abstractmethod
    def get_all_invoices(self) -> list[Invoice]:
        pass
