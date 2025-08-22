class Artist:
    def __init__(self, artist_id: int, artist_name: str):
        self.artist_id = artist_id
        self.artist_name = artist_name

    def __repr__(self):
        return f"Artist Id={self.artist_id} , Name={self.artist_name})"
