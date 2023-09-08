import os
import shutil
import hashlib

# Function to batch rename files in a directory
def batch_rename_files(directory, new_prefix):
    for count, filename in enumerate(os.listdir(directory)):
        new_filename = f"{new_prefix}_{count + 1}{os.path.splitext(filename)[1]}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# Function to organize files into folders by file type
def organize_files_by_type(source_dir, target_dir):
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            file_type = filename.split('.')[-1].lower()
            target_subdir = os.path.join(target_dir, file_type)
            os.makedirs(target_subdir, exist_ok=True)
            shutil.move(os.path.join(source_dir, filename), os.path.join(target_subdir, filename))

# Function to find and remove duplicate files
def find_and_remove_duplicates(directory):
    hashes = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
            if file_hash in hashes:
                print(f"Duplicate found: {file_path}")
                os.remove(file_path)
            else:
                hashes[file_hash] = file_path

if __name__ == "__main__":
    source_directory = "your_source_directory"
    target_directory = "your_target_directory"
    new_file_prefix = "new_file"

    # Uncomment the section you want to use
    # batch_rename_files(source_directory, new_file_prefix)
    # organize_files_by_type(source_directory, target_directory)
    # find_and_remove_duplicates(source_directory)
