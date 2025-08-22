from abc import ABC, abstractmethod
from models.genre import Genre

class AGenre(ABC):
    @abstractmethod
    def create_genre(self, model: Genre) -> None:
        pass

    @abstractmethod
    def update_genre(self, g_id: int, model: Genre) -> None:
        pass

    @abstractmethod
    def delete_genre(self, g_id: int) -> None:
        pass

    @abstractmethod
    def get_genre(self, g_id: int) -> Genre:
        pass

    @abstractmethod
    def get_all_genres(self) -> list[Genre]:
        pass
