from models.repos.playlist_repo import PlaylistRepo
from models.playlist import Playlist


def create_playlist():
    try:
        name = input("Enter Playlist Name: ")
        playlist = Playlist(playlist_id=None, playlist_name=name)
        repo = PlaylistRepo()
        repo.create_playlist(playlist)
        print("Playlist created successfully")
    except Exception as e:
        print(f"Error creating playlist: {e}")


def update_playlist():
    try:
        pl_id = int(input("Enter Playlist ID to update: "))
        name = input("Enter New Playlist Name: ")
        playlist = Playlist(playlist_id=pl_id, playlist_name=name)
        repo = PlaylistRepo()
        repo.update_playlist(pl_id, playlist)
        print("Playlist updated successfully")
    except Exception as e:
        print(f"Error updating playlist: {e}")


def delete_playlist():
    try:
        pl_id = int(input("Enter Playlist ID to delete: "))
        repo = PlaylistRepo()
        repo.delete_playlist(pl_id)
        print("Playlist deleted successfully")
    except Exception as e:
        print(f"Error deleting playlist: {e}")


def get_playlist():
    try:
        pl_id = int(input("Enter Playlist ID to fetch: "))
        repo = PlaylistRepo()
        playlist = repo.get_playlist(pl_id)
        if playlist:
            print(f"Id: {playlist.playlist_id}, Name: {playlist.playlist_name}")
        else:
            print("Playlist not found")
    except Exception as e:
        print(f"Error fetching playlist: {e}")


def view_all_playlists():
    try:
        repo = PlaylistRepo()
        playlists = repo.get_all_playlists()
        if not playlists:
            print("No playlists found")
        else:
            print("\nPlaylist Table Data \n-------------------")
            for pl in playlists:
                print(f"Id: {pl.playlist_id}, Name: {pl.playlist_name}")
    except Exception as e:
        print(f"Error fetching playlists: {e}")


def playlist_main():
    while True:
        print("\nPlaylist Menu ")
        print("1. Create Playlist")
        print("2. Update Playlist")
        print("3. Delete Playlist")
        print("4. Get Playlist by ID")
        print("5. View All Playlists")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_playlist()
        elif choice == "2":
            update_playlist()
        elif choice == "3":
            delete_playlist()
        elif choice == "4":
            get_playlist()
        elif choice == "5":
            view_all_playlists()
        elif choice == "6":
            print("Exiting Playlist Menu")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    playlist_main()
