# Welcome to DirEnumerator 3000 - Unleash the Power of Enumeration!
# Developed by Parth Padhiyar - The Code Explorer 🚀
# (c) 2023 Parth Padhiyar. All rights reserved.

# Remember, in the world of directories, we're not lost, just exploring!
# So, fasten your seatbelt and let's dive into the URLiverse. 🌐

import os
import csv
import signal
from datetime import datetime
import requests
from colorama import Fore, Style, init as colorama_init

colorama_init(autoreset=True)

# Function to handle keyboard interrupts gracefully
def signal_handler(sig, frame):
    print("\nScript interrupted by user.")
    exit(0)

# Function to prompt the user for the target URL
def get_target_url():
    target_url = input("Enter the target URL (include http/https): ").strip()
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "http://" + target_url
    return target_url

# Function to read directories from the file
def read_directories_from_file(file_path='SPdir.txt'):
    try:
        with open(file_path, 'r') as file:
            directories = [line.strip() for line in file.readlines()]
        return directories
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)

# Function to handle NTLM authentication
def handle_ntlm_authentication():
    auth_option = input("Choose authentication option (basic/ntlmv1/ntlmv2): ").lower()
    if auth_option.startswith('ntlm'):
        ntlm_username = input("Enter NTLM username: ")
        ntlm_password = input("Enter NTLM password: ")
        return (auth_option, ntlm_username, ntlm_password)
    else:
        return None

# Function to make HTTP requests and log results
def make_http_request(target_url, directory, auth=None, log_file=None):
    url = f"{target_url}/{directory}"
    try:
        response = requests.get(url, auth=auth, timeout=5)
        status_code = response.status_code
        log_result(url, status_code, log_file)
        print(colored_status(status_code), url)
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

# Function to log results to a CSV file
def log_result(url, status_code, log_file):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = [timestamp, url, status_code]

    with open(log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(log_entry)

# Function to colorize console output based on HTTP status code
def colored_status(status_code):
    if status_code == 200:
        return f"{Fore.GREEN}{status_code}{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}{status_code}{Style.RESET_ALL}"

# Main function
def main():
    # Set up a signal handler for graceful interruption
    signal.signal(signal.SIGINT, signal_handler)

    # Get the target URL from the user
    target_url = get_target_url()

    # Read directories from a file
    directories = read_directories_from_file()

    # Handle NTLM authentication
    auth = handle_ntlm_authentication()

    # Create a log file with a unique name based on the target URL and timestamp
    log_file = f"{target_url.replace('://', '_').replace('/', '_').strip('_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    # Iterate through directories and make HTTP requests
    for directory in directories:
        make_http_request(target_url, directory, auth, log_file)

if __name__ == "__main__":
    # Execute the main function when the script is run
    main()
