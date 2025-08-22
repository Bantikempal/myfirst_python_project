from models.playlist_track import PlaylistTrack
from models.repos.a_playlist_track import APlaylistTrack
import sqlite3

class PlaylistTrackRepo(APlaylistTrack):
    def create_playlist_track(self, model: PlaylistTrack) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(
                    "INSERT INTO playlist_track (PlaylistId, TrackId) VALUES (?, ?)",
                    (model.playlist_id, model.track_id)
                )
                conn.commit()
                print("Playlist-Track association created successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def update_playlist_track(self, pl_id: int, model: PlaylistTrack) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(
                    "UPDATE playlist_track SET TrackId = ? WHERE PlaylistId = ? AND TrackId = ?",
                    (model.track_id, pl_id, model.track_id)  
                )
                conn.commit()
                print("Playlist-Track association updated successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def delete_playlist_track(self, pl_id: int, tr_id: int) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(
                    "DELETE FROM playlist_track WHERE PlaylistId = ? AND TrackId = ?",
                    (pl_id, tr_id)
                )
                conn.commit()
                print("Playlist-Track association deleted successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def get_playlist_track(self, pl_id: int) -> list:
        try:
            with sqlite3.connect("chinook.db") as conn:
                data = conn.execute("SELECT * FROM playlist_track WHERE PlaylistId = ?", (pl_id,))
                rows = data.fetchall()
                if rows:
                    return [PlaylistTrack(playlist_id=row[0], track_id=row[1]) for row in rows]
                else:
                    print(f"No tracks found for PlaylistId {pl_id}")
                    return []
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def get_all_playlist_tracks(self) -> list[PlaylistTrack]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM playlist_track")
                for row in cursor:
                    plt = PlaylistTrack(playlist_id=row[0], track_id=row[1])
                    data_list.append(plt)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
