import os
import shutil

def main():
    """
    This function provides a simple command-line interface for file management.
    """

    while True:
        print("\nChoose an action:")
        print("1. Create a new directory")
        print("2. Delete a directory")
        print("3. Rename a file or directory")
        print("4. Copy a file or directory")
        print("5. Move a file or directory")
        print("6. List files in a directory")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            directory_name = input("Enter the name of the new directory: ")
            create_directory(directory_name)
        elif choice == '2':
            directory_name = input("Enter the name of the directory to delete: ")
            delete_directory(directory_name)
        elif choice == '3':
            old_name = input("Enter the old name: ")
            new_name = input("Enter the new name: ")
            rename_item(old_name, new_name)
        elif choice == '4':
            source = input("Enter the source path: ")
            destination = input("Enter the destination path: ")
            copy_item(source, destination)
        elif choice == '5':
            source = input("Enter the source path: ")
            destination = input("Enter the destination path: ")
            move_item(source, destination)
        elif choice == '6':
            directory_name = input("Enter the directory to list files: ")
            list_files(directory_name)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def create_directory(directory_name):
    """
    Creates a new directory.

    Args:
        directory_name: The name of the directory to create.
    """
    try:
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except OSError as e:
        print(f"Error creating directory: {e}")

def delete_directory(directory_name):
    """
    Deletes a directory.

    Args:
        directory_name: The name of the directory to delete.
    """
    try:
        shutil.rmtree(directory_name)
        print(f"Directory '{directory_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory_name}' not found.")
    except OSError as e:
        print(f"Error deleting directory: {e}")

def rename_item(old_name, new_name):
    """
    Renames a file or directory.

    Args:
        old_name: The old name of the file or directory.
        new_name: The new name of the file or directory.
    """
    try:
        os.rename(old_name, new_name)
        print(f"'{old_name}' renamed to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"File or directory '{old_name}' not found.")
    except OSError as e:
        print(f"Error renaming: {e}")

def copy_item(source, destination):
    """
    Copies a file or directory.

    Args:
        source: The path to the source file or directory.
        destination: The path to the destination.
    """
    try:
        if os.path.isdir(source):
            shutil.copytree(source, destination)
            print(f"Directory '{source}' copied to '{destination}' successfully.")
        else:
            shutil.copy2(source, destination)
            print(f"File '{source}' copied to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"File or directory '{source}' not found.")
    except OSError as e:
        print(f"Error copying: {e}")

def move_item(source, destination):
    """
    Moves a file or directory.

    Args:
        source: The path to the source file or directory.
        destination: The path to the destination.
    """
    try:
        shutil.move(source, destination)
        print(f"'{source}' moved to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"File or directory '{source}' not found.")
    except OSError as e:
        print(f"Error moving: {e}")

def list_files(directory_name):
    """
    Lists all files in a directory.

    Args:
        directory_name: The name of the directory to list files from.
    """
    try:
        files = os.listdir(directory_name)
        print(f"Files in '{directory_name}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory '{directory_name}' not found.")
    except OSError as e:
        print(f"Error listing files: {e}")

if __name__ == "__main__":
    main()