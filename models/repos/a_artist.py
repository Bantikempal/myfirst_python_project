from abc import ABC, abstractmethod
from models.artist import Artist

class A_Artist(ABC):
    @abstractmethod
    def create_artist(self, model: Artist) -> None:
        pass

    @abstractmethod
    def update_artist(self, g_id: int, model: Artist) -> None:
        pass

    @abstractmethod
    def delete_artist(self, g_id: int) -> None:
        pass

    @abstractmethod
    def get_artist(self, g_id: int) -> Artist:
        pass

    @abstractmethod
    def get_all_artists(self) -> list[Artist]:
        pass
