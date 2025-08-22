from models.repos.artist_repo import ArtistRepo
from models.artist import Artist 

def view_artist():
    """Fetches and displays all Artist types."""
    try:
        ar = ArtistRepo()
        ga_artist = ar.get_all_artists()
        if not ga_artist:
            print("No artist types found.")
        else:
            print("Artist Table Data \n----------------")
            for li in ga_artist:
                print(f"Id : {li.artist_id} , Name : {li.artist_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_artist_by_id(art_id: int):
    """Fetches and displays a artist type by ID."""
    try:
        atr = ArtistRepo()
        at = atr.get_artist(art_id)
        if at:
            print(f"Id: {at.artist_id}, Name: {at.artist_name}")
        else:
            print(f"No artist type found with ID {art_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")
  
def view_created_artist():
    """Create a Artist"""
    try:
        artistid = input("Enter Artist Id : ")
        artistname = input("Enter Artist Name : ")
        insertartist = Artist(artistid,artistname)
        cgr = ArtistRepo()
        cgr.create_artist(insertartist)
        view_artist()
    except Exception as e:
        print(f"An error occured : {e}")

def view_update_artist():
    """Update a Artist"""
    try:
        artistid = input("Enter Artist Id : ")
        artistname = input("Enter Artist Name : ")
        ug = Artist(artistid,artistname)
        cgr = ArtistRepo()
        cgr.update_artist(artistid,ug)
        view_artist()
    except Exception as e:
        print(f"An error occured : {e}")

def view_delete_artist():
    """Delete a Artist"""
    try:
        artistid=input("Enter artist id which you want to delete : ")
        dgtr=ArtistRepo()
        dgtr.delete_artist(artistid)
        view_artist()
    except Exception as e:
        print(f"An error occured : {e}")      

def artist_main():
    while True:
        print("\nArtist Management Menu")
        print("1. View all artist types ")
        print("2. View artist type by ID ")
        print("3. Create artist type ")
        print("4. Update artist type ")
        print("5. Delete artist type ")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            view_artist()
        elif choice == '2':
            try:
                art_id = int(input("Enter Artist ID: "))
                view_artist_by_id(art_id)
            except ValueError:
                print("Invalid input. Please enter a numeric ID.")
        elif choice == '3':
            view_created_artist()
        elif choice == '4':
            view_update_artist()
        elif choice == '5':
            view_delete_artist()
        elif choice == '6':
            print("Exiting Artist Management Menu.")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
   artist_main()