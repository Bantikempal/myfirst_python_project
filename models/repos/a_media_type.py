from abc import ABC, abstractmethod
from models.media_type import MediaType

class AMediaType(ABC):
    @abstractmethod
    def create_media_type(self, model: MediaType) -> None:
        pass

    @abstractmethod
    def update_media_type(self, mt_id: int, model: MediaType) -> None:
        pass

    @abstractmethod
    def delete_media_type(self, mt_id: int) -> None:
        pass

    @abstractmethod
    def get_media_type(self, mt_id: int) -> MediaType:
        pass

    @abstractmethod
    def get_all_media_types(self) -> list[MediaType]:
        pass
