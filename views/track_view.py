from models.repos.track_repo import TrackRepo
from models.track import Track

def view_track():
    """Fetches and displays all track types."""
    try:
        tr = TrackRepo()
        gatrack = tr.get_all_tracks()
        if not gatrack:
            print("No track types found.")
        else:
            print("Track Table Data \n----------------")
            for li in gatrack:
                print(f"Track id = {li.track_id}, Name = {li.track_name}, Album id = {li.album_id}, Media_type id = {li.media_type_id}, Genre id = {li.genre_id}, Composer = {li.composer}, Milliseconds = {li.milliseconds}, Bytes = {li.bytes}, Unitprice = {li.unitprice}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_track_type_by_id(t_id: int):
    """Fetches and displays a track type by ID."""
    try:
        tr = TrackRepo()
        gt = tr.get_track(t_id)
        if gt:
            print(f"Track id = {gt.track_id}, Name = {gt.track_name}, Album id = {gt.album_id}, Media_type id = {gt.media_type_id}, genre id = {gt.genre_id}, Composer = {gt.composer}, Milliseconds = {gt.milliseconds}, Bytes = {gt.bytes}, Unitprice = {gt.unitprice}")
        else:
            print(f"No track type found with ID {t_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def view_created_track():
    """Create a Track"""
    try:
        trackid = input("Enter Track Id : ")
        trackname = input("Enter Track Name : ")
        a_id = input("Enter Album Id : ")
        mtid = input("Enter Media Type Id : ")
        gid = input("Enter Genre Id : ")
        comp = input("Enter composer : ")
        ms = input("Enter Millisecond : ")
        b = input("Enter Bytes : ")
        up=input("Enter Unit Price : ")
        ct = Track(trackid,trackname,a_id,mtid,gid,comp,ms,b,up)
        ctr=TrackRepo()
        ctr.create_track(ct)
        view_track()
    except Exception as e:
        print(f"An error occured : {e}")

def view_update_track():
    """Update a Track"""
    try:
        trackid = input("Enter Track Id : ")
        trackname = input("Enter Track Name : ")
        a_id = input("Enter Album Id : ")
        mtid = input("Enter Media Type Id : ")
        gid = input("Enter Genre Id : ")
        comp = input("Enter Composer : ")
        ms = input("Enter Millisecond : ")
        b = input("Enter Bytes : ")
        up=input("Enter Unit Price : ")
        ut = Track(trackid,trackname,a_id,mtid,gid,comp,ms,b,up)
        utr = TrackRepo()
        utr.update_track(trackid,ut)
        view_track()
    except Exception as e:
        print(f"An error occured : {e}")

def view_delete_track():
    """Delete a track"""
    try:
        trackid=input("Enter track id which you want to delete : ")
        dgtr=TrackRepo()
        dgtr.delete_track(trackid)
        view_track()
    except Exception as e:
        print(f"An error occured : {e}")

def track_main():
    while True:
        print("\nTrack Management Menu")
        print("1. View All Tracks")
        print("2. View Track by ID")
        print("3. Create Track")
        print("4. Update Track")
        print("5. Delete Track")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_track()
        elif choice == "2":
            try:
                t_id = int(input("Enter Track ID: "))
                view_track_type_by_id(t_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == "3":
            view_created_track()
        elif choice == "4":
            view_update_track()
        elif choice == "5":
            view_delete_track()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

    
      
if __name__ == "__main__":
    track_main()