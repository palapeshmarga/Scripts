# Python Scripts

A collection of small Python command-line utilities for file management, text search, networking, image processing, and terminal text art.

Each utility is self-contained in its own directory and can be run independently.

## Contents

| Directory | Description | Dependencies |
| --- | --- | --- |
| [`FindTheWord`](FindTheWord/) | Search for text inside files, either in one folder or recursively. | Python standard library |
| [`Cleaning`](Cleaning/) | Sort files into folders such as `Documents`, `Photos`, `Videos`, `Musics`, `System_Files`, and `Unknown`. | Python standard library |
| [`NetworkScanner`](NetworkScanner/) | Display devices discovered on the local network using ARP. | `arp-scan` on Linux/macOS; built-in `arp` on Windows |
| [`BG_Remover`](BG_Remover/) | Remove an image background and save a transparent PNG. | `rembg`, `Pillow` |
| [`Terminal Font`](Terminal%20Font/) | Render text as ASCII-art banners using custom fonts. | Python standard library |

## Requirements

- Python 3.8 or newer is recommended.
- Some utilities require additional system packages or Python libraries; see the README inside each directory.
- Linux and macOS commands generally use `python3`; Windows commands generally use `python`.

Create a virtual environment if you want to keep optional dependencies isolated:

```bash
python3 -m venv venv
source venv/bin/activate       # Linux/macOS
# Windows PowerShell: .\venv\Scripts\Activate.ps1
```

## Quick start

Run commands from the relevant directory. For example:

### Search files

```bash
cd FindTheWord
python3 main.py --recursive-path /path/to/folder --word "search text" --type py
```

### Organize a folder

```bash
cd Cleaning
python3 cleaning_folder.py --path "/path/to/folder"
```

### Scan the local network

```bash
cd NetworkScanner
python3 scanning.py
```

### Remove an image background

```bash
cd BG_Remover
pip install rembg pillow
python3 bgRemover.py target=/path/to/image.jpg saveto=/path/to/result.png
```

### Generate terminal ASCII art

```bash
cd "Terminal Font"
python3 terminal-font-generator.py --font ghost --text "HELLO WORLD"
```

Use `-br` inside the text argument to create separate banner lines:

```bash
python3 terminal-font-generator.py -f graffiti -t "HELLO-br-WORLD"
```


## Important notes

- `Cleaning/cleaning_folder.py` moves files in the target directory. Review the target path before running it and keep backups of important files.
- If a destination file already exists, the cleaning script removes the existing destination file before moving the new file.
- `NetworkScanner/scanning.py` may require administrator/root privileges and should only be used on networks you are authorized to inspect.
- For complete options and examples, see the README inside each utility directory.

## Project structure

```text
python_Scripts/
├── BG_Remover/
├── Cleaning/
├── FindTheWord/
├── NetworkScanner/
├── Terminal Font/
└── README.md
```

## License

No top-level license file is currently included. Add a license before distributing the collection if you want to define reuse and distribution terms.
