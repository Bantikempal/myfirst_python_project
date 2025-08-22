from models.track import Track
from models.repos.a_track import ATrack
import sqlite3

class TrackRepo(ATrack):
    def create_track(self, model: Track) -> None:
        conn=sqlite3.connect("chinook.db")
        conn.execute(f"insert into tracks values ({model.track_id},'{model.track_name}', {model.album_id}, {model.media_type_id}, {model.genre_id}, '{model.composer}', {model.milliseconds}, {model.bytes}, {model.unitprice})")
        conn.commit()
        
    def update_track(self, t_id: int, model: Track) -> None:
        conn=sqlite3.connect("chinook.db")
        conn.execute(f"update tracks set Name = '{model.track_name}', AlbumID = {model.album_id}, MediaTypeId = {model.media_type_id}, GenreId = {model.genre_id}, Composer = '{model.composer}', Milliseconds = {model.milliseconds}, Bytes = {model.bytes}, UnitPrice = {model.unitprice} where TrackId = {t_id}")
        conn.commit()
        
    def delete_track(self, t_id: int) -> None:
        conn=sqlite3.connect("chinook.db")
        conn.execute(f"delete from tracks where TrackId={t_id}")
        conn.commit()


    def get_track(self, t_id: int) -> Track:
        conn=sqlite3.connect("chinook.db")
        cursor=conn.execute("select * from tracks where TrackId=?",(t_id,))
        row=cursor.fetchone()
        if cursor:
            return Track(track_id=row[0], track_name=row[1], album_id=row[2], media_type_id=row[3], genre_id=row[4], composer=row[5], milliseconds=row[6], bytes=row[7], unitprice=row[8])
        else:
            print(f"No track found with Id {t_id}")
        
       
        

    def get_all_tracks(self) -> list[Track]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM tracks")
                for row in cursor:
                    g = Track(track_id=row[0], track_name=row[1], album_id=row[2], media_type_id=row[3], genre_id=row[4], composer=row[5], milliseconds=row[6], bytes=row[7], unitprice=row[8])
                    data_list.append(g)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
