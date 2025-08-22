class MediaType:
    def __init__(self, media_type_id: int, media_type_name: str):
        self.media_type_id = media_type_id
        self.media_type_name = media_type_name

    def __repr__(self):
        return f"MediaType id={self.media_type_id}, name={self.media_type_name})"
