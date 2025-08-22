from views.album_view import album_main
from views.artist_view import artist_main   
from views.customer_view import customer_main
from views.employee_view import employee_main
from views.genre_view import genre_main
from views.invoice_item_view import invoice_item_main
from views.invoice_view import invoice_main
from views.media_type_view import media_type_main   
from views.playlist_track_view import playlist_track_main   
from views.playlist_view import playlist_main
from views.track_view import track_main

while True:
    print("\nAlbum Management Menu")
    print("1. manage Albums ")
    print("2. manage Artists ")
    print("3. manage Customers ")
    print("4. manage Employees ")
    print("5. manage Genres ")
    print("6. manage Invoice Items ")
    print("7. manage Invoices ")
    print("8. manage Media Types ")
    print("9. manage Playlist Tracks ")
    print("10. manage Playlist")
    print("11. Manage track")
    print("0. Exit")


    choice = input("Enter your choice: ")


    if choice == '1':
        album_main()
    elif choice == '2': 
        artist_main()   
    elif choice == '3':
        customer_main()    
    elif choice == '4':
        employee_main()
    elif choice == '5':
        genre_main()        
    elif choice == '6':
        invoice_item_main()    
    elif choice == '7':
        invoice_main()    
    elif choice == '8':
        media_type_main()    
    elif choice == '9':
        playlist_track_main()    
    elif choice == '10':
        playlist_main()    
    elif choice == '11':
        track_main()        
    elif choice == '0':
        print()
        break
    else:
        print(".")    