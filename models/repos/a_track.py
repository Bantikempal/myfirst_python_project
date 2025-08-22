from abc import ABC, abstractmethod
from models.track import Track

class ATrack(ABC):
    @abstractmethod
    def create_track(self, model: Track) -> None:
        pass

    @abstractmethod
    def update_track(self, t_id: int, model: Track) -> None:
        pass

    @abstractmethod
    def delete_track(self, t_id: int) -> None:
        pass

    @abstractmethod
    def get_track(self, t_id: int) -> Track:
        pass

    @abstractmethod
    def get_all_tracks(self) -> list[Track]:
        pass
