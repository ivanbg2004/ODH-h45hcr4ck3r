import hashlib
import os
import itertools
import time

class HashCracker:
    """
    A powerful and professional hash cracking tool with advanced features.
    """

    def __init__(self, hash_value, hash_type, wordlist=None, charset=None, min_length=None, max_length=None, rainbow_table=None, use_gpu=False):
        """
        Initializes the HashCracker object.

        Args:
            hash_value (str): The hash value to crack.
            hash_type (str): The hash algorithm (e.g., "md5", "sha256").
            wordlist (str, optional): Path to a wordlist file. Defaults to None.
            charset (str, optional): Character set for brute-force attacks. Defaults to None.
            min_length (int, optional): Minimum password length for brute-force. Defaults to None.
            max_length (int, optional): Maximum password length for brute-force. Defaults to None.
            rainbow_table (str, optional): Path to a precomputed rainbow table. Defaults to None.
            use_gpu (bool, optional):  Enable GPU acceleration (if available). Defaults to False.
        """

        self.hash_value = hash_value
        self.hash_type = hash_type
        self.wordlist = wordlist
        self.charset = charset
        self.min_length = min_length
        self.max_length = max_length
        self.rainbow_table = rainbow_table
        self.use_gpu = use_gpu
        self.start_time = None


    def _hash_password(self, password):
        """
        Hashes a password using the specified algorithm.
        """
        try:
            return hashlib.new(self.hash_type, password.encode()).hexdigest()
        except ValueError:
            print(f"[!] Invalid hash type: {self.hash_type}.  Please use a valid algorithm (md5, sha1, sha256, etc.).")
            return None


    def wordlist_attack(self):
        """
        Performs a dictionary attack using a wordlist.
        """
        if not self.wordlist:
            print("[!] Wordlist path not provided.")
            return None

        print("[*] Starting wordlist attack...")
        try:
            with open(self.wordlist, "r", encoding="utf-8", errors="ignore") as file:
                for i, password in enumerate(file):
                    password = password.strip()
                    hashed_attempt = self._hash_password(password)
                    if hashed_attempt is None:
                        return None

                    if hashed_attempt == self.hash_value:
                        print(f"[+] Password found (wordlist): {password} (Attempt {i+1})")
                        self.stop_timer()
                        return password

                    if (i + 1) % 10000 == 0:
                        print(f"[*] {i+1} passwords tried from wordlist...")

            print("[-] Password not found in wordlist.")
            self.stop_timer()
            return None

        except FileNotFoundError:
            print(f"[!] Wordlist file not found: {self.wordlist}")
            return None
        except Exception as e:
            print(f"[!] Error during wordlist attack: {e}")
            return None

    def brute_force_attack(self):
        """
        Performs a brute-force attack using a character set and length range.
        """
        if not (self.charset and self.min_length is not None and self.max_length is not None):
            print("[!] Charset, min_length, and max_length must be provided for brute-force attack.")
            return None

        print("[*] Starting brute-force attack...")

        for length in range(self.min_length, self.max_length + 1):
            for combination in itertools.product(self.charset, repeat=length):
                password = ''.join(combination)
                hashed_attempt = self._hash_password(password)
                if hashed_attempt is None:
                    return None

                if hashed_attempt == self.hash_value:
                    print(f"[+] Password found (brute-force): {password}")
                    self.stop_timer()
                    return password

        print("[-] Password not found during brute-force attack.")
        self.stop_timer()
        return None

    def rainbow_table_attack(self):
      """
      Performs a rainbow table attack (not implemented in this version).
      """
      print("[!] Rainbow table attacks are not yet implemented.")
      return None # Placeholder

    def start_timer(self):
        """Starts the timer to track the cracking time."""
        self.start_time = time.time()

    def stop_timer(self):
        """Stops the timer and prints the elapsed time."""
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            print(f"[*] Time elapsed: {elapsed_time:.2f} seconds")

    def run(self):
        """
        Runs the hash cracking process, prioritizing attacks.
        """
        self.start_timer()
        password = None
        if self.wordlist:
            password = self.wordlist_attack()
            if password:
                return password

        if self.charset and self.min_length and self.max_length:
            password = self.brute_force_attack()
            if password:
                return password

        if self.rainbow_table:
            password = self.rainbow_table_attack()
            if password:
                return password

        return None


if __name__ == "__main__":
    print(" ____  ____  ____  ____  ______   ____  ")
    print("(_  _)(_  _)(_  _)(_  _)(  __  ) (_  _) ")
    print("  )(    )(    )(    )(   ) (__) |   )(   ")
    print(" (__)  (__)  (__)  (__) (______/  (__)  ")
    print("-----------------------------------------")
    print("  A Powerful Hash Cracking Tool by OD&H  ")
    print("-----------------------------------------\n")

    hash_value = input("Enter the hash: ").strip()
    hash_type = input("Enter the hash type (md5, sha1, sha256, etc.): ").strip()

    cracker = HashCracker(hash_value=hash_value, hash_type=hash_type)

    attack_type = input("Choose attack type (wordlist, brute-force, rainbow-table, or auto): ").strip().lower()

    if attack_type == "wordlist" or attack_type == "auto":
        wordlist = input("Enter path to wordlist: ").strip()
        cracker.wordlist = wordlist

    if attack_type == "brute-force" or attack_type == "auto":
        charset = input("Enter charset for brute-force (e.g., abcdefghijklmnopqrstuvwxyz0123456789): ").strip()
        min_length = int(input("Enter minimum password length: ").strip())
        max_length = int(input("Enter maximum password length: ").strip())
        cracker.charset = charset
        cracker.min_length = min_length
        cracker.max_length = max_length

    if attack_type == "rainbow-table":
        rainbow_table = input("Enter path to rainbow table: ").strip()
        cracker.rainbow_table = rainbow_table


    if attack_type == "wordlist":
        cracker.wordlist_attack()
    elif attack_type == "brute-force":
        cracker.brute_force_attack()
    elif attack_type == "rainbow-table":
        cracker.rainbow_table_attack()
    elif attack_type == "auto":
       result = cracker.run()
       if result:
          print(f"Cracking successful! Password found: {result}")
       else:
          print("Password not found using the available attack methods.")
    else:
        print("Invalid attack type.")
