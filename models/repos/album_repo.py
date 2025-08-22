from models.album import Album
from models.repos.a_album import A_Album
import sqlite3

class AlbumRepo(A_Album):
    def create_album(self, model: Album) -> None:
        conn=sqlite3.connect("chinook.db")
        conn.execute(f"insert into albums values ({model.album_id},'{model.album_title}', {model.artist_id})")
        conn.commit()
        
    def update_album(self, alb_id: int, model: Album) -> None:
        conn=sqlite3.connect("chinook.db")
        conn.execute(f"update albums set Title = '{model.album_title}', ArtistID = {model.artist_id} where AlbumId = {alb_id}")
        conn.commit()
        
    def delete_album(self, alb_id: int) -> None:
        conn=sqlite3.connect("chinook.db")
        conn.execute(f"delete from albums where AlbumId={alb_id}")
        conn.commit()


    def get_album(self, alb_id: int) -> Album:
        conn=sqlite3.connect("chinook.db")
        cursor=conn.execute("select * from albums where AlbumId=?",(alb_id,))
        row=cursor.fetchone()
        if cursor:
            return Album(album_id=row[0], album_title=row[1], artist_id=row[2])
        else:
            print(f"No album found with Id {alb_id}")
        

    def get_all_albums(self) -> list[Album]:
        data_list = []

        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM albums")
                for row in cursor:
                    g = Album(album_id=row[0], album_title=row[1], artist_id=row[2])
                    data_list.append(g)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
