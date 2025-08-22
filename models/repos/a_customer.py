from abc import ABC, abstractmethod
from models.customer import Customer

class ACustomer(ABC):
    @abstractmethod
    def create_customer(self, model: Customer) -> None:
        pass

    @abstractmethod
    def update_customer(self, customer_id: int, model: Customer) -> None:
        pass

    @abstractmethod
    def delete_customer(self, customer_id: int) -> None:
        pass

    @abstractmethod
    def get_customer(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def get_all_customers(self) -> list[Customer]:
        pass
