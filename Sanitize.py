import os
import subprocess
import random

def list_drives():
    try:
        # Using lsblk to list block devices, excluding read-only devices
        result = subprocess.check_output(["lsblk", "-do", "name,ro,type", "--json"])
        drives = [f"/dev/{disk['name']}" for disk in result['blockdevices']
                  if disk['ro'] == "0" and disk['type'] == "disk"]
        return drives
    except Exception as e:
        print(f"Error listing drives: {e}")
        return []

def get_drive_size(drive):
    with open(drive, 'rb') as f:
        f.seek(0, os.SEEK_END)
        return f.tell()

def overwrite_data(drive, method):
    try:
        drive_size = get_drive_size(drive)
        block_size = 4096 * 1024  # Increased block size for efficiency (4MB)

        for pass_num in range(1, 4):  # Three-pass overwrite
            random.seed(12345)  # Fixed seed for reproducibility

            with open(drive, 'wb') as f:
                for i in range(0, drive_size, block_size):
                    if method == 'zeros':
                        data = b'\x00' * block_size
                    elif method == 'random':
                        data = random.randbytes(block_size)
                    else:
                        print("Unknown method. Exiting.")
                        return False

                    try:
                        f.write(data)
                        f.flush()
                    except IOError as e:
                        print(f"Write error on {drive}: {e}")
                        continue  # Skip to next block in case of a write error

                    # Progress feedback
                    progress = ((i / drive_size) + pass_num - 1) * 33.33
                    print(f"Pass {pass_num}: {progress:.2f}% complete", end='\r')

        return True
    except Exception as e:
        print(f"\nError during overwriting: {e}")
        return False

def main():
    print("Secure Data Sanitization Tool")

    # List drives and allow the user to select one
    drives = list_drives()
    if not drives:
        print("No writable drives found.")
        return

    print("Available Drives:")
    for drive in drives:
        print(drive)

    selected_drive = input("Enter the drive to sanitize (e.g., /dev/sda): ")
    if selected_drive not in drives:
        print("Invalid drive selected.")
        return

    # Select erasure method
    print("Available Methods: zeros, random")
    method = input("Enter the erasure method: ")

    # Perform data sanitization
    if overwrite_data(selected_drive, method):
        print("\nData overwriting completed.")
    else:
        print("\nData sanitization failed.")

if __name__ == "__main__":
    main()
