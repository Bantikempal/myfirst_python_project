from models.playlist import Playlist
from models.repos.a_playlist import APlaylist
import sqlite3

class PlaylistRepo(APlaylist):
    def create_playlist(self, model: Playlist) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(
                    "INSERT INTO playlists (Name) VALUES (?)",
                    (model.playlist_name,)
                )
                conn.commit()
                print("Playlist created successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def update_playlist(self, pl_id: int, model: Playlist) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(
                    "UPDATE playlists SET Name = ? WHERE PlaylistId = ?",
                    (model.playlist_name, pl_id)
                )
                conn.commit()
                print("Playlist updated successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def delete_playlist(self, pl_id: int) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(
                    "DELETE FROM playlists WHERE PlaylistId = ?",
                    (pl_id,)
                )
                conn.commit()
                print("Playlist deleted successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def get_playlist(self, pl_id: int) -> Playlist | None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute(
                    "SELECT * FROM playlists WHERE PlaylistId = ?",
                    (pl_id,)
                )
                row = cursor.fetchone()
                if row:
                    return Playlist(playlist_id=row[0], playlist_name=row[1])
                else:
                    print(f"No playlist found with PlaylistId {pl_id}")
                    return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def get_all_playlists(self) -> list[Playlist]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM playlists")
                for row in cursor:
                    pl = Playlist(playlist_id=row[0], playlist_name=row[1])
                    data_list.append(pl)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
