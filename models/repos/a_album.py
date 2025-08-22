from abc import ABC, abstractmethod
from models.album import Album

class A_Album(ABC):
    @abstractmethod
    def create_album(self, model: Album) -> None:
        pass

    @abstractmethod
    def update_album(self, alb_id: int, model: Album) -> None:
        pass

    @abstractmethod
    def delete_album(self, alb_id: int) -> None:
        pass

    @abstractmethod
    def get_album(self, alb_id: int) -> Album:
        pass

    @abstractmethod
    def get_all_albums(self) -> list[Album]:
        pass
