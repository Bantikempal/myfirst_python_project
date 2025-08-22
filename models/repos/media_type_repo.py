import sqlite3
from models.media_type import MediaType
from models.repos.a_media_type import AMediaType

class MediaTypeRepo(AMediaType):

    def create_media_type(self, model: MediaType) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO media_types (Name) VALUES (?)",
                    (model.media_type_name,)
                )
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def update_media_type(self, mt_id: int, model: MediaType) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE media_types SET Name = ? WHERE MediaTypeId = ?",
                    (model.media_type_name, mt_id)
                )
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def delete_media_type(self, mt_id: int) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM media_types WHERE MediaTypeId = ?",
                    (mt_id,)
                )
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def get_media_type(self, mt_id: int) -> MediaType | None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM media_types WHERE MediaTypeId = ?",
                    (mt_id,)
                )
                row = cursor.fetchone()
                if row:
                    return MediaType(media_type_id=row[0], media_type_name=row[1])
                return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def get_all_media_types(self) -> list[MediaType]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM media_types")
                for row in cursor:
                    mt = MediaType(media_type_id=row[0], media_type_name=row[1])
                    data_list.append(mt)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
