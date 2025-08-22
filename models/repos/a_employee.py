from abc import ABC, abstractmethod
from models.employee import Employee

class AEmployee(ABC):
    @abstractmethod
    def create_employee(self, model: Employee) -> None:
        pass

    @abstractmethod
    def update_employee(self, emp_id: int, model: Employee) -> None:
        pass

    @abstractmethod
    def delete_employee(self, emp_id: int) -> None:
        pass

    @abstractmethod
    def get_employee(self, emp_id: int) -> Employee:
        pass

    @abstractmethod
    def get_all_employees(self) -> list[Employee]:
        pass
