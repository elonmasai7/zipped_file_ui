# Zipped File Password Cracker UI 🔓

A modern Python-based tool with a sleek **Graphical User Interface (GUI)** for cracking password-protected ZIP files using a wordlist. Whether you're a casual user or an advanced one, this tool provides an easy-to-use interface and command-line support for handling ZIP files with forgotten passwords.

### Features ✨
- **Modern GUI**: A clean, dark-themed UI for a user-friendly experience.
- **Command-Line Integration**: Use the tool from the terminal with command-line arguments for automation.
- **Custom Wordlist Support**: Option to use your own password wordlist or auto-generate one.
- **Threading for Performance**: Ensures a responsive GUI during password-cracking attempts.
- **Wordlist Generation**: Automatically generates a basic wordlist if none is provided.

---

## Installation 🚀

### GUI Version

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/elonmasai7/zipped_file_ui.git
   cd zipped_file_ui
   ```

2. **Install Required Libraries**:
   Ensure you have Python 3.x installed, and install `tkinter` if it's not already included with your Python installation:
   ```bash
   pip install tkinter
   ```

3. **Run the GUI Tool**:
   ```bash
   python zip_cracker_gui.py
   ```

This will launch the GUI interface where you can select your ZIP file, load a custom wordlist, and start cracking the password.

### Command-Line Version

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/elonmasai7/zipped_file_ui.git
   cd zipped_file_ui
   ```

2. **Install Locally as a Command-Line Tool**:
   Run the following command to install the tool as a command-line utility:
   ```bash
   pip install .
   ```

3. **Usage**:
   After installation, you can use the `zipcracker` command directly from your terminal.

   Example:
   ```bash
   zipcracker path_to_zip_file.zip --wordlist path_to_wordlist.txt
   ```

   If you don't specify a wordlist, the tool will generate a basic one for you.

---

## Usage 📖

### GUI Instructions

1. **Select ZIP File**: Click on **"Browse"** to choose the ZIP file you want to crack.
2. **Select Custom Wordlist (Optional)**: You can provide a custom wordlist file for cracking passwords. If no wordlist is provided, a basic one will be generated.
3. **Start Cracking**: Press **"Start Cracking"** to begin the password recovery process.

### Command-Line Instructions

```bash
usage: zipcracker [-h] [--wordlist WORDLIST] zipfile

A command-line ZIP password cracker.

positional arguments:
  zipfile          Path to the ZIP file

optional arguments:
  -h, --help       show this help message and exit
  --wordlist       Path to a custom wordlist (if not provided, a basic one will be generated)
```

**Example**:

To crack `secret.zip` using a custom wordlist:
```bash
zipcracker secret.zip --wordlist passwords.txt
```

---

## Screenshots 🖼️

### GUI Interface:
![Zipped File Password Cracker GUI](screenshots/gui-screenshot.png)

- **Sleek Dark Mode**: Eye-catching dark theme with a modern layout.
- **File Selection**: Simple file picker for selecting ZIP files and wordlists.
- **Live Status**: Progress updates during the password-cracking process.

---

## Contributing 🤝

We welcome contributions, feature requests, and bug reports! Follow the steps below to contribute:

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature/your-feature`).
3. **Commit your changes** (`git commit -m 'Add your feature'`).
4. **Push to the branch** (`git push origin feature/your-feature`).
5. **Open a pull request**.

---

## License 📄

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact & Socials 📬

Feel free to reach out if you have any questions or suggestions!

- **Email**: elonmasai7@gmail.com
- **GitHub**: [Elon Masai](https://github.com/elonmasai7)
- **LinkedIn**: [Elon Masai on LinkedIn](https://www.linkedin.com/in/elonmasai)
- **Twitter**: [@elonmasai7](https://twitter.com/elonmasai7)

---

Enjoy cracking passwords responsibly! 🎉🔐

---
