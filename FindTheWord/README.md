# FindTheWord 🔍

A fast, lightweight, and robust Python command-line utility for searching specific words or text strings inside files across your file system. 

Built with `pathlib` for high-performance directory traversal, **FindTheWord** easily handles recursive searches, file-type filtering, permission errors on restricted folders, and root (`sudo`) privilege escalation.

---

## ✨ Features

- ⚡ **High Performance**: Uses native C-backed `pathlib.rglob` pattern matching to scan thousands of files in seconds.
- 📁 **Single-Folder & Recursive Search**: Choose between scanning a single directory (`-p`) or recursively diving through all nested subfolders (`-rp`).
- 🎯 **File Extension Filtering**: Narrow searches down to specific file extensions (e.g., `.txt`, `.py`, `.md`) or search across all file types (`*`).
- 🔐 **Root/Sudo Elevation (`-S`)**: Seamlessly re-executes with `sudo` privileges to inspect system files without manually typing `sudo` at the front of your command.
- 🛡️ **Fault Tolerant**: Silently handles permission errors (`PermissionError`) and encoding anomalies without breaking or crashing mid-search.
- 🛑 **Graceful Cancellation**: Handles `Ctrl + C` (`KeyboardInterrupt`) cleanly without dumping noisy Python stack traces.

---

## 🚀 Installation & Requirements

- **Python**: `Python 3.8+` (No third-party libraries required — uses standard library modules only).
- Works on **Linux**, **macOS**, **Windows**, and **Termux/Android**.

```bash
git clone https://github.com/YOUR_USERNAME/Scripts.git
cd Scripts/FindTheWord
```

---

## 📖 Usage & Flags

```bash
python3 main.py [-p FOLDER | -rp FOLDER] -w "TEXT" [-t EXT] [-S]
```

### Command Line Arguments

| Flag | Long Flag | Description | Required |
| :--- | :--- | :--- | :---: |
| `-p` | `--path` | Search **ONLY** in the target directory (single level). | Yes* |
| `-rp` | `--recursive-path` | Search in target directory **AND all subfolders** recursively. | Yes* |
| `-w` | `--word` | The text string or word to search for (case-insensitive). | **Yes** |
| `-t` | `--type` | File extension to filter by (e.g., `txt`, `py`). Default: `*` (all files). | No |
| `-S` | `--sudo` | Re-run script with `sudo` root privileges to inspect protected files. | No |
| `-h` | `--help` | Show help message and exit. | No |

*\* Note: You must provide either `-p` or `-rp` (they are mutually exclusive).*

---

## 💡 Examples

### 1. Search in a single folder for `.txt` files
```bash
python3 main.py -p /home/user/Desktop/my_folder -w "hello kurdistan" -t txt
```

### 2. Recursive search across all subdirectories and file types
```bash
python3 main.py -rp /home/user/Desktop -w "hello kurdistan"
```

### 3. Recursive search with `sudo` privileges for restricted directories
```bash
python3 main.py -S -rp /var/log -w "error" -t log
```

### 4. Display help documentation
```bash
python3 main.py -h
```

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.