from abc import ABC, abstractmethod
from models.playlist import Playlist

class APlaylist(ABC):
    @abstractmethod
    def create_playlist(self, model: Playlist) -> None:
        pass

    @abstractmethod
    def update_playlist(self, pl_id: int, model: Playlist) -> None:
        pass

    @abstractmethod
    def delete_playlist(self, pl_id: int) -> None:
        pass

    @abstractmethod
    def get_playlist(self, pl_id: int) -> Playlist:
        pass

    @abstractmethod
    def get_all_playlists(self) -> list[Playlist]:
        pass
