from models.repos.playlist_repo import PlaylistRepo
from models.playlist import Playlist

def view_playlists():
    try:
        repo = PlaylistRepo()
        playlists = repo.get_all_playlists()
        if not playlists:
            print("No playlists found.")
        else:
            print("Playlist Table Data \n----------------")
            for pl in playlists:
                print(f"Id: {pl.playlist_id}, Name: {pl.playlist_name}")
    except Exception as e:
        print(f"An error occurred: {e}")


def view_playlist_by_id(pl_id: int):
    try:
        repo = PlaylistRepo()
        playlist = repo.get_playlist(pl_id)
        if playlist:
            print(f"\nPlaylist Details\n----------------")
            print(f"Id: {playlist.playlist_id}, Name: {playlist.playlist_name}")
        else:
            print(f"No playlist found with ID {pl_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_playlist():
    try:
        name = input("Enter Playlist Name: ")
        new_pl = Playlist(playlist_id=None, playlist_name=name)
        repo = PlaylistRepo()
        repo.create_playlist(new_pl)
        print("Playlist created successfully.\n")
        view_playlists()
    except Exception as e:
        print(f"An error occurred: {e}")


def update_playlist():
    try:
        pl_id = int(input("Enter Playlist ID to update: "))
        name = input("Enter New Playlist Name: ")
        updated_pl = Playlist(playlist_id=pl_id, playlist_name=name)
        repo = PlaylistRepo()
        repo.update_playlist(pl_id, updated_pl)
        print("Playlist updated successfully.\n")
        view_playlists()
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_playlist():
    try:
        pl_id = int(input("Enter Playlist ID to delete: "))
        repo = PlaylistRepo()
        repo.delete_playlist(pl_id)
        print("Playlist deleted successfully.\n")
        view_playlists()
    except Exception as e:
        print(f"An error occurred: {e}")


def playlist_track_main():
    while True:
        print("\nPlaylist Management Menu")
        print("1. View All Playlists")
        print("2. View Playlist by ID")
        print("3. Create Playlist")
        print("4. Update Playlist")
        print("5. Delete Playlist")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_playlists()
        elif choice == '2':
            try:
                pl_id = int(input("Enter Playlist ID: "))
                view_playlist_by_id(pl_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == '3':
            create_playlist()
        elif choice == '4':
            update_playlist()
        elif choice == '5':
            delete_playlist()
        elif choice == '0':
            print()
            break
        else:
            print("Invalid choice, please try again.")        


if __name__ == "__main__":
    playlist_track_main()
