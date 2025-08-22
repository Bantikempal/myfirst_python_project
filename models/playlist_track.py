class PlaylistTrack:
    def __init__(self, playlist_id: int, track_id: str):
        self.playlist_id = playlist_id
        self.track_id = track_id

    def __repr__(self):
        return f"(Playlist Track Id={self.playlist_id} , Track ID = {self.track_id})"
