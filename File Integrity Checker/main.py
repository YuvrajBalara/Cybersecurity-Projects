import os
import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)  # 64KB chunks
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

def check_integrity(directory_path):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    hash_map = {}

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_sha256(file_path)
            print(f"{file_path}: {file_hash}")
            hash_map[file_path] = file_hash

    return hash_map

# e.g usage:
if __name__ == "__main__":
    directory = input("Enter the directory path to check integrity: ")
    hashes = check_integrity(directory)
