import os

# Define a list of potentially dangerous file extensions
dangerous_extensions = ['.exe', '.dll', '.bat', '.vbs']

# Specify the directory to scan
directory_to_scan = '/path/to/directory'

# Scan the directory for potentially malicious files
def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            _, extension = os.path.splitext(file_path)
            if extension in dangerous_extensions:
                print("Potentially dangerous file found:", file_path)

# Start the scan
scan_directory(directory_to_scan)
