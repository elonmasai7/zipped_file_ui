import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import threading
import itertools
from tkinter import ttk

custom_wordlist_path = None

def crack_zip(zip_file_path, dictionary_path):
    try:
        zip_file = zipfile.ZipFile(zip_file_path)
        with open(dictionary_path, 'r', encoding='utf-8', errors='ignore') as file:
            passwords = file.readlines()
        for password in passwords:
            try:
                password = password.strip()
                zip_file.extractall(pwd=bytes(password, 'utf-8'))
                result_message = f"Password found: {password}"
                messagebox.showinfo("Success", result_message)
                return
            except:
                continue
        else:
            messagebox.showinfo("Failed", "Password not found in the dictionary")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{zip_file_path}' not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_cracking(zip_file_path, dictionary_path):
    crack_thread = threading.Thread(target=crack_zip, args=(zip_file_path, dictionary_path))
    crack_thread.start()

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
        "qwerty", "abc123", "111111", "1234", "admin", "letmein"
    ]
    combinations = itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=4)
    with open(file_path, 'w') as file:
        for password in common_passwords:
            file.write(password + "\n")
        for combo in itertools.islice(combinations, 100):
            file.write("".join(combo) + "\n")

def select_zip_file():
    file_path = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
    if file_path:
        zip_file_label.config(text=os.path.basename(file_path))
        zip_file_label.filepath = file_path

def select_custom_wordlist():
    global custom_wordlist_path
    custom_wordlist_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if custom_wordlist_path:
        wordlist_label.config(text=f"Custom wordlist: {os.path.basename(custom_wordlist_path)}")

def on_start_cracking():
    zip_file_path = getattr(zip_file_label, 'filepath', None)
    if not zip_file_path:
        messagebox.showerror("Error", "Please select a ZIP file")
        return
    if custom_wordlist_path:
        dictionary_path = custom_wordlist_path
    else:
        dictionary_path = create_wordlist_directory()
    start_cracking(zip_file_path, dictionary_path)

root = tk.Tk()
root.title("Modern ZIP Password Cracker")
root.geometry("500x300")
root.configure(bg="#2E3440")

style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background="#2E3440", foreground="#ECEFF4", font=("Helvetica", 12))
style.configure("TButton", background="#4C566A", foreground="#ECEFF4", font=("Helvetica", 12), padding=6)
style.map("TButton", background=[('active', '#5E81AC')])

header_label = ttk.Label(root, text="ZIP Password Cracker", font=("Helvetica", 16, "bold"), anchor="center")
header_label.pack(pady=20)

zip_frame = ttk.Frame(root, padding="10")
zip_frame.pack(fill="x", padx=20, pady=10)

zip_file_label = ttk.Label(zip_frame, text="Select a ZIP file", anchor="center")
zip_file_label.pack(side="left", padx=10)

select_zip_button = ttk.Button(zip_frame, text="Browse", command=select_zip_file)
select_zip_button.pack(side="right")

wordlist_frame = ttk.Frame(root, padding="10")
wordlist_frame.pack(fill="x", padx=20, pady=10)

wordlist_label = ttk.Label(wordlist_frame, text="No custom wordlist selected", anchor="center")
wordlist_label.pack(side="left", padx=10)

select_wordlist_button = ttk.Button(wordlist_frame, text="Browse Wordlist", command=select_custom_wordlist)
select_wordlist_button.pack(side="right")

start_button = ttk.Button(root, text="Start Cracking", command=on_start_cracking)
start_button.pack(pady=20)

footer_label = ttk.Label(root, text="Developed with Python & Tkinter", font=("Helvetica", 10), anchor="center")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
