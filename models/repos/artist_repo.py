from models.artist import Artist
from models.repos.a_artist import A_Artist
import sqlite3

class ArtistRepo(A_Artist):
    def create_artist(self, model: Artist) -> None:
        conn=sqlite3.connect("chinook.db")
        conn.execute(f"insert into artists values ({model.artist_id},'{model.artist_name}')")
        conn.commit()
        
    def update_artist(self, gt_id: int, model: Artist) -> None:
        conn=sqlite3.connect("chinook.db")
        conn.execute(f"update artists set Name = '{model.artist_name}' where ArtistId = {gt_id}")
        conn.commit()
        
    def delete_artist(self, gt_id: int) -> None:
        conn=sqlite3.connect("chinook.db")
        conn.execute(f"delete from artists where ArtistId={gt_id}")
        conn.commit()

    def get_artist(self, art_id: int) -> Artist:
        conn=sqlite3.connect("chinook.db")
        data=conn.execute("select * from artists where ArtistId=?",(art_id,))
        row=data.fetchone()
        
        if data:
            return Artist(artist_id=row[0], artist_name=row[1])
        else:
            print(f"No artist found with Id {art_id}")
        
      

    def get_all_artists(self) -> list[Artist]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM artists")
                for row in cursor:
                    g = Artist(artist_id=row[0], artist_name=row[1])
                    data_list.append(g)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
