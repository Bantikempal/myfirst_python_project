class Album:
    def __init__(self, album_id: int, album_title: str, artist_id: int):
        self.album_id = album_id
        self.album_title = album_title
        self.artist_id = artist_id
    def __repr__(self):
        return f"Album Id = {self.album_id} , Name = {self.album_title} , Artist Id = {self.artist_id} )"
