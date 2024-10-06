import zipfile
import argparse
import os
import itertools

def crack_zip(zip_file_path, dictionary_path):
    try:
        zip_file = zipfile.ZipFile(zip_file_path)
        with open(dictionary_path, 'r', encoding='utf-8', errors='ignore') as file:
            passwords = file.readlines()
        for password in passwords:
            try:
                password = password.strip()
                zip_file.extractall(pwd=bytes(password, 'utf-8'))
                print(f"[+] Password found: {password}")
                return password
            except:
                continue
        print("[-] Password not found in the dictionary")
    except FileNotFoundError:
        print(f"Error: File '{zip_file_path}' not found")
    except Exception as e:
        print(f"Error: {str(e)}")

def create_wordlist_directory():
    wordlist_dir = os.path.join(os.getcwd(), "wordlists")
    if not os.path.exists(wordlist_dir):
        os.makedirs(wordlist_dir)
    wordlist_path = os.path.join(wordlist_dir, "generated_passwords.txt")
    generate_wordlist(wordlist_path)
    return wordlist_path

def generate_wordlist(file_path):
    common_passwords = [
        "123456", "password", "123456789", "12345678", "12345",
        "qwerty", "abc123", "11111", "1234", "admin", "letmein"
    ]
    combinations = itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=4)
    with open(file_path, 'w') as file:
        for password in common_passwords:
            file.write(password + "\n")
        for combo in itertools.islice(combinations, 100):
            file.write("".join(combo) + "\n")

def main():
    parser = argparse.ArgumentParser(description="A command-line ZIP password cracker.")
    parser.add_argument("zipfile", help="Path to the ZIP file")
    parser.add_argument("--wordlist", help="Path to a custom wordlist", default=None)
    args = parser.parse_args()

    zip_file_path = args.zipfile
    wordlist_path = args.wordlist

    if not wordlist_path:
        wordlist_path = create_wordlist_directory()

    print(f"[*] Cracking ZIP file: {zip_file_path}")
    print(f"[*] Using wordlist: {wordlist_path}")

    crack_zip(zip_file_path, wordlist_path)

if __name__ == "__main__":
    main()
