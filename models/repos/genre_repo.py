from models.genre import Genre
from models.repos.a_genre import AGenre
import sqlite3

class GenreRepo(AGenre):
    def create_genre(self, model: Genre) -> None:
        conn=sqlite3.connect("chinook.db")
        conn.execute(f"insert into genres values ({model.genre_id},'{model.genre_name}')")
        conn.commit()
        
    def update_genre(self, gt_id: int, model: Genre) -> None:
        conn=sqlite3.connect("chinook.db")
        conn.execute(f"update genres set Name = '{model.genre_name}' where GenreId = {gt_id}")
        conn.commit()
        
    def delete_genre(self, gt_id: int) -> None:
        conn=sqlite3.connect("chinook.db")
        conn.execute(f"delete from genres where GenreId={gt_id}")
        conn.commit()


    def get_genre(self, gt_id: int) -> Genre:
        conn=sqlite3.connect("chinook.db")
        cursor=conn.execute("select * from genres where GenreId=?",(gt_id,))
        row=cursor.fetchone()
        if cursor:
            return Genre(genre_id=row[0], genre_name=row[1])
        else:
            print(f"No genre found with Id {gt_id}")
        
       
        

    def get_all_genres(self) -> list[Genre]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM genres")
                for row in cursor:
                    g = Genre(genre_id=row[0], genre_name=row[1])
                    data_list.append(g)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
