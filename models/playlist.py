class Playlist:
    def __init__(self, playlist_id: int, playlist_name: str):
        self.playlist_id = playlist_id
        self.playlist_name = playlist_name

    def __repr__(self):
        return f"Playlist Id = {self.playlist_id} , Name = {self.playlist_name})"
