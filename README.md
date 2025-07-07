

# 📧 TempMail CLI

A Python CLI tool to generate temporary email addresses and read incoming messages right in your terminal.

---

## 🚀 Features

* ✉️ Generate a temporary email address
* ⏳ Wait for incoming emails with a 4-minute timeout
* 🔄 Convert HTML emails to plain text
* 🎨 Colorful, styled console output with logs and warnings
* 🖥️ Simple interactive command line interface

---

## ⚙️ Installation

1. Clone this repository or download the `main.py` file.

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   *If you don’t have a `requirements.txt`, install manually:*

   ```bash
   pip install tempmail pystyle html2text colorama raducord
   ```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Follow the prompt:

* Type `1` and press Enter to generate a temporary email and wait for incoming messages.
* Any other input will exit the program with a message.

---

## ⚠️ Disclaimer

This tool is strictly for educational and testing purposes. Misuse is neither encouraged nor supported.

---

## 🛠️ Technologies

* Python
* [tempmail](https://pypi.org/project/tempmail/)
* [pystyle](https://pypi.org/project/pystyle/)
* [html2text](https://pypi.org/project/html2text/)
* [colorama](https://pypi.org/project/colorama/)
* [raducord](https://pypi.org/project/raducord/)

---
