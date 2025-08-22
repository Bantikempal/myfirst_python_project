from models.repos.media_type_repo import MediaTypeRepo
from models.media_type import MediaType

def view_media_types():
    """Fetches and displays all media types."""
    try:
        repo = MediaTypeRepo()
        all_media_types = repo.get_all_media_types()
        if not all_media_types:
            print("No media types found.")
        else:
            print("Media Types Table Data \n----------------")
            for mt in all_media_types:
                print(f"ID: {mt.media_type_id}, Name: {mt.media_type_name}")
    except Exception as e:
        print(f"An error occurred: {e}")


def view_media_type_by_id(mt_id: int):
    """Fetches and displays a media type by ID."""
    try:
        repo = MediaTypeRepo()
        mt = repo.get_media_type(mt_id)
        if mt:
            print(f"ID: {mt.media_type_id}, Name: {mt.media_type_name}")
        else:
            print(f"No media type found with ID {mt_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_media_type():
    """Create a new media type."""
    try:
        name = input("Enter Media Type Name: ")
        new_mt = MediaType(media_type_id=None, media_type_name=name)
        repo = MediaTypeRepo()
        repo.create_media_type(new_mt)
        print("Media Type created successfully.\n")
        view_media_types()
    except Exception as e:
        print(f"An error occurred: {e}")


def update_media_type():
    """Update an existing media type."""
    try:
        mt_id = int(input("Enter Media Type ID to update: "))
        name = input("Enter new Media Type Name: ")
        updated_mt = MediaType(media_type_id=mt_id, media_type_name=name)
        repo = MediaTypeRepo()
        repo.update_media_type(mt_id, updated_mt)
        print("Media Type updated successfully.\n")
        view_media_types()
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_media_type():
    """Delete a media type."""
    try:
        mt_id = int(input("Enter Media Type ID to delete: "))
        repo = MediaTypeRepo()
        repo.delete_media_type(mt_id)
        print("Media Type deleted successfully.\n")
        view_media_types()
    except Exception as e:
        print(f"An error occurred: {e}")


def media_type_main():
    """Main function to manage media type operations."""
    while True:
        print("\nMedia Type Management Menu")
        print("1. View All Media Types")
        print("2. View Media Type by ID")
        print("3. Create Media Type")
        print("4. Update Media Type")
        print("5. Delete Media Type")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_media_types()
        elif choice == '2':
            mt_id = int(input("Enter Media Type ID: "))
            view_media_type_by_id(mt_id)
        elif choice == '3':
            create_media_type()
        elif choice == '4':
            update_media_type()
        elif choice == '5':
            delete_media_type()
        elif choice == '0':
            print("Exiting Media Type Management.")
            break
        else:
            print("Invalid choice, please try again.")        


if __name__ == "__main__":
    media_type_main()
