from abc import ABC, abstractmethod
from models.playlist_track import PlaylistTrack

class APlaylistTrack(ABC):
    @abstractmethod
    def create_playlist_track(self, model: PlaylistTrack) -> None:
        pass

    @abstractmethod
    def update_playlist_track(self, pl_t_id: int, model: PlaylistTrack) -> None:
        pass

    @abstractmethod
    def delete_playlist_track(self, pl_t_id: int) -> None:
        pass

    @abstractmethod
    def get_playlist_track(self, pl_t_id: int) -> PlaylistTrack:
        pass

    @abstractmethod
    def get_all_playlist_tracks(self) -> list[PlaylistTrack]:
        pass
