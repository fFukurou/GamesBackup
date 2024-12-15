import shutil
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from GamePaths import *

def copy_directory(src, dest):
    """ Function to copy a single directory. """
    try:
        if not os.path.exists(src):
            print(f"Source directory '{src}' does not exist.")
            return

        # Create destination if it doesn't exist
        os.makedirs(dest, exist_ok=True)

        shutil.copytree(src, dest, dirs_exist_ok=True)
        print(f"Successfully copied from '{src}' to '{dest}'")
    except Exception as e:
        print(f"Error copying '{src}' to '{dest}': {e}")

def copy_multiple_directories(dir_pairs):
    """ Function to copy multiple directories using ThreadPoolExecutor. """
    with ThreadPoolExecutor() as executor:
        futures = []
        
        # Submit tasks for each source-destination pair
        for src, dest in dir_pairs:
            futures.append(executor.submit(copy_directory, src, dest))
        
        # Wait for all tasks to complete and print status
        for future in as_completed(futures):
            future.result()  # Will re-raise any exception

if __name__ == "__main__":
    # List of (source, destination) folder pairs
    directories_to_copy = [
        STANLEY_PARABLE,
        
    ]

    # Replces \ with / on windows
    directories_to_copy = [
        (src.replace("\\", "/"), dest.replace("\\", "/")) 
        for src, dest in directories_to_copy
    ]
            
    # Copy all directories concurrently
    copy_multiple_directories(directories_to_copy)
