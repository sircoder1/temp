import requests
import time
import os
import hashlib

# Raw GitHub link to the Python script
GITHUB_RAW_URL = "https://raw.githubusercontent.com/sircoder1/temp/main/index.py"

# Local filename to save the downloaded script
LOCAL_SCRIPT_NAME = "index.py"

# Variable to store the last known checksum
last_checksum = None

def get_checksum(file_path):
    """Computes the SHA-256 checksum of a file."""
    try:
        hasher = hashlib.sha256()
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

def download_script():
    """Downloads the Python script from GitHub."""
    try:
        response = requests.get(GITHUB_RAW_URL, timeout=10)
        response.raise_for_status()  # Raise an error for HTTP failures
        with open(LOCAL_SCRIPT_NAME, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Downloaded {LOCAL_SCRIPT_NAME} successfully.")
        return True
    except requests.RequestException as e:
        print(f"Error downloading script: {e}")
        return False

def run_script():
    """Executes the downloaded Python script."""
    try:
        print(f"Executing {LOCAL_SCRIPT_NAME}...")
        os.system(f"python {LOCAL_SCRIPT_NAME}")
    except Exception as e:
        print(f"Error executing script: {e}")

def main():
    """Main loop to download and run the script if it has changed."""
    global last_checksum

    while True:
        downloaded = download_script()
        if downloaded:
            new_checksum = get_checksum(LOCAL_SCRIPT_NAME)

            # If the file has changed, execute it
            if new_checksum != last_checksum:
                print("File changed! Running the new script...\n")
                run_script()
                last_checksum = new_checksum
            else:
                print("No changes detected. Skipping execution.")

        print("Waiting 1 minute before next check...\n")
        time.sleep(60)  # Wait for 1 minute (60 seconds)

if __name__ == "__main__":
    main()
