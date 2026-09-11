# Terminal Font Generator 🎨

A lightweight Python command-line utility that renders multi-line ASCII art text banners using custom font definitions. Easily generate styled text directly in your terminal with support for custom line breaks.

---

## 🚀 Features

* **Multiple Custom Fonts:** Render text using 3D Diagonal, Bulbhead, Ghost, Graffiti, Roman, and Standard fonts.
* **Side-by-Side Line Rendering:** Automatically arranges ASCII characters side-by-side horizontally.
* **Line Break Support:** Break long sentences into multiple ASCII lines using the custom `-br` flag.
* **Full ASCII Support:** Handles uppercase, lowercase, numbers, and standard keyboard symbols.
* **Zero External Dependencies:** Runs natively using built-in Python modules.

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/palapeshmarga/Scripts.git
   cd terminal-font-generator
    ```

## 🛠️ Usage

Run `terminal_font.py` from your terminal using the `-f` (font) and `-t` (text) flags.

```bash
python3 terminal_font.py -f <font_name> -t "<your_text>"
```
---
## Examples

1. ***Basic Text Rendering:***
```bash
python3 terminal_font.py -f ghost -t "HELLO WORLD"
```

2. ***Multi-Line Banners (using `-br` for line breaks):***
```bash
python3 terminal_font.py -f graffiti -t "ABC abc -br 123 !@#"
```

## 🔤 Available Fonts
You can select from any of the following fonts using the `-f` flag:
- 3d_diagonal
- bulbhead
- ghost
- graffiti
- roman
- standard (default)

## 📖 Command-Line Options

```
usage: terminal_font.py [-h] [-f FONT] -t TEXT

Render ASCII text banners from custom font files.

AVAILABLE FONTS:
  • 3d_diagonal
  • bulbhead
  • ghost
  • graffiti
  • roman
  • standard (default)

options:
  -h, --help            Show this help message and exit.
  -f FONT, --font FONT  Select the ASCII art font to use.
  -t TEXT, --text TEXT  The text string to display. Use '-br' inside quotes to break lines.
  ```

  ## 📁 Repository Structure

  ```
  .
├── terminal_font.py              # Main CLI execution script
├── ascii_letters_3d_diagonal.py  # 3D Diagonal font dictionary
├── ascii_letters_bulbhead.py     # Bulbhead font dictionary
├── ascii_letters_ghost.py        # Ghost font dictionary
├── ascii_letters_graffiti.py     # Graffiti font dictionary
├── ascii_letters_roman.py        # Roman font dictionary
├── ascii_letters_standard.py     # Standard font dictionary
└── README.md                     # Project documentation
```

## 📄 License
This project is licensed under the MIT License — feel free to use, modify, and distribute it!