class Genre:
    def __init__(self, genre_id: int, genre_name: str):
        self.genre_id = genre_id
        self.genre_name = genre_name

    def __repr__(self):
        return f"Genre(Id={self.genre_id} , Name={self.genre_name})"
