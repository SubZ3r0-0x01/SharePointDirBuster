# SharePoint DirEnumerator 3000 - Unleash the Power of Enumeration!

Welcome to SharePoint DirEnumerator 3000, a specialized directory enumeration tool for Microsoft SharePoint, developed by **Parth Padhiyar - The Code Explorer** 🚀. 

![SharePoint DirEnumerator 3000](https://your_image_url_here)

## Overview

In the SharePoint realm, DirEnumerator 3000 is your go-to tool for efficiently navigating directories. Whether you're conducting a SharePoint security assessment or simply exploring, this script simplifies the process of traversing SharePoint's directory structure.

## Features

- **Graceful Interruption**: DirEnumerator 3000 handles keyboard interrupts gracefully, allowing you to stop the script without any hiccups.

- **User-Friendly**: Easy-to-use prompts for entering the SharePoint site URL, proxy settings, and authentication options.

- **HTTP Requests and Logging**: Make HTTP requests to specified directories, log results to a CSV file, and visualize HTTP status codes with colorized console output.

- **Proxy Support**: Optionally use a proxy for SharePoint requests.

- **NTLM Authentication**: Supports basic and NTLMv1/v2 authentication methods.

## Requirements

- Python 3.x
- [colorama](https://pypi.org/project/colorama/)
- [requests](https://pypi.org/project/requests/)
- [urllib3](https://pypi.org/project/urllib3/)

## Getting Started

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python dir_enumerator.py`

## Usage

1. Enter the SharePoint site URL when prompted, ensuring it starts with "http://" or "https://."
2. Choose whether to use a proxy for your SharePoint requests.
3. If needed, provide proxy details.
4. If the SharePoint site requires authentication, select the appropriate method (basic/ntlmv1/ntlmv2) and enter credentials.
5. Sit back, fasten your seatbelt, and let SharePoint DirEnumerator 3000 do the exploring!

## Configuration

- The tool reads directories from the "SPdir.txt" file by default. Ensure your SharePoint directory list is present in this file.

- SSL verification is set to False by default for upstreaming to Burp Suite. Adjust the `verify_ssl` variable as needed.

## Results

SharePoint DirEnumerator 3000 logs results to a CSV file with a unique name based on the SharePoint site URL and timestamp. Find your log file in the project directory.

## Contributing

If you find a bug or have an enhancement in mind, feel free to open an issue or submit a pull request. Your contributions make SharePoint DirEnumerator 3000 even better!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Remember, in the world of SharePoint directories, we're not lost, just exploring! So, fasten your seatbelt and let's dive into the SharePointiverse. 🌐
