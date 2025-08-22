class Track:
    def __init__(self,track_id,track_name,album_id,media_type_id,genre_id,composer,milliseconds,bytes,unitprice):
        self.track_id = track_id
        self.track_name = track_name
        self.album_id = album_id
        self.media_type_id = media_type_id
        self.genre_id = genre_id
        self.composer = composer
        self.milliseconds = milliseconds
        self.bytes = bytes
        self.unitprice = unitprice
    
    
    def __repr__(self):
        return f"Track id = {self.track_id}, name = {self.track_name}, album id = {self.album_id}, media_type id = {self.media_type_id}, genre id = {self.genre_id}, composer = {self.composer}, milliseconds = {self.milliseconds}, bytes = {self.bytes}, unitprice = {self.unitprice})"