# OD&H Hash Cracker

A powerful and professional hash cracking tool brought to you by Oblivion Development & Hosting (OD&H).  This tool provides efficient methods for cracking password hashes, including dictionary attacks and brute-force techniques.

## Overview

The OD&H Hash Cracker is a Python-based tool designed for security professionals and enthusiasts to test the strength of password hashes.  It offers:

*   **Support for common hash algorithms:** MD5, SHA1, SHA256, SHA512, and more.
*   **Wordlist-based cracking:** Attempts to crack the hash by comparing it against a list of potential passwords.
*   **Brute-force cracking:** Attempts to crack the hash by generating and testing all possible password combinations within a specified character set and length range.
*   **Timing for performance analysis:** Tracks the time taken to crack the hash.
*   **Object-oriented design:** Makes the code modular, extensible, and easy to maintain.
*   **Clear and informative output:** Provides progress updates and error messages.

**Developed and Maintained by Oblivion Development & Hosting (OD&H)**

## Features

*   **Hash Algorithm Support:** Supports a wide range of hash algorithms via Python's `hashlib` library.
*   **Wordlist Attack:**  Efficiently cracks passwords using a provided wordlist file. Handles different character encodings.
*   **Brute-Force Attack:** Customizable brute-force attack with user-defined character sets, minimum length, and maximum length.
*   **Attack Prioritization:** The `auto` attack mode prioritizes wordlist attacks before attempting brute-force.
*   **Clear Reporting:** Provides clear output of password cracking attempts, including the attack type and number of passwords tried.
*   **Timing:** Tracks the total runtime of the tool.
*   **Error Handling:** Handles common errors, such as invalid hash types, missing wordlist files, and invalid user inputs.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ivanbg2004/ODH-h45hcr4ck3r.git
    cd odh-hash-cracker
    ```

2.  **(Optional) Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```

3.  **Install dependencies (if any - likely not needed for this script, but good practice):**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the script:**

    ```bash
    python hash_cracker.py
    ```

2.  **Follow the prompts:**

    *   Enter the hash to crack.
    *   Enter the hash algorithm (e.g., `md5`, `sha1`, `sha256`).
    *   Choose an attack type:
        *   `wordlist`: Uses a wordlist file.
        *   `brute-force`: Uses a brute-force attack.
        *   `rainbow-table`: (Not fully implemented)  A placeholder for future rainbow table support.
        *   `auto`: Attempts wordlist attack first, then brute-force if a wordlist is provided and brute-force settings are configured.
    *   Provide the necessary information based on the attack type you selected (wordlist path, character set, minimum length, maximum length).

## Example

```
  _   _   _   _   _   _   _   _   _
 / \ / \ / \ / \ / \ / \ / \ / \ / \
( O | D | & | H |   | H | A | S | H )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
  _   _   _   _   _   _   _   _   _
 / \ / \ / \ / \ / \ / \ / \ / \ / \
(   | C | R | A | C | K | E | R |   )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/

-----------------------------------------
       OD&H - Oblivion Development
-----------------------------------------

Enter the hash: e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4
Enter the hash type (md5, sha1, sha256, etc.): sha1
Choose attack type (wordlist, brute-force, rainbow-table, or auto): auto
Enter path to wordlist: You can use: https://raw.githubusercontent.com/ivanbg2004/ODH-h45hcr4ck3r/refs/heads/main/odh-wordlist.txt
Enter charset for brute-force (e.g., abcdefghijklmnopqrstuvwxyz0123456789): abcdefg
Enter minimum password length: 1
Enter maximum password length: 4
```

## OD&H Wordlist

To enhance the effectiveness of the wordlist attack, we provide a curated wordlist specifically designed for this tool. This wordlist is designed for fast, ethical cracking and is available at:

[Check it out here!](https://raw.githubusercontent.com/ivanbg2004/ODH-h45hcr4ck3r/refs/heads/main/odh-wordlist.txt)

**Important Considerations:**

*   **Use with Caution:** As with any wordlist, ensure you only use this for authorized penetration testing and security assessments.
*   **License:** This wordlist is provided under the same license as this tool (MIT License). See the [LICENSE](LICENSE) file for more details.
*   **Content:** This wordlist may contain sensitive information. Handle it responsibly and securely.
*   **Ethical Use:** OD&H is not responsible for any misuse of this wordlist. Ensure you comply with all applicable laws and ethical guidelines.

**How to Use:**

1.  Download the `odh-wordlist.txt` file.
2.  When prompted for the wordlist path, specify the location of the downloaded file.

**Disclaimer:**

OD&H does not guarantee the success of cracking any particular hash using this wordlist. The effectiveness of any wordlist depends on various factors, including the password complexity and the target system.

## Contributing

We welcome contributions to the OD&H Hash Cracker!  Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear and concise code with comments.
4.  Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

*   Developed and Maintained by Oblivion Development & Hosting (OD&H)
*   [Link to OD&H Website](https://odh.ivan-vcard.xyz)

Copyright © 2025 Oblivion Development & Hosting (OD&H).  All rights reserved.

This software is a weapon.  Use it wisely, and only on targets you are authorized to engage. OD&H accepts no responsibility for collateral damage or unauthorized incursions. By using this tool, you agree to uphold the highest ethical standards in your digital endeavors. May your hashes crack swiftly and your intentions remain true.
