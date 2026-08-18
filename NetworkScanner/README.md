# Cross-Platform Local Network ARP Scanner

A lightweight Python utility that automatically detects your operating system (**Linux**, **macOS**, or **Windows**) and performs a local network ARP scan to discover connected devices.

## Features

- **OS Detection:** Automatically identifies your environment using Python's built-in `platform` module.
- **Smart Dependency Management:** Checks if `arp-scan` is installed and offers to install it via your system package manager (`apt-get` or Homebrew).
- **Permission Handling:** Automatically handles root/administrator privileges (`sudo`) when required for network scanning.

## Requirements

- **Python 3.x**
- **arp-scan** (required for Linux and macOS)
  - **Linux:** Uses `arp-scan` (relies on `apt` and `sudo`)
  - **macOS:** Uses `arp-scan` (relies on `brew` and `sudo`)
  - **Windows:** Uses the native built-in `arp -a` command

## Usage

Save the script to your machine and run it from your *`terminal`*/*`CMD`*/*`PowerShell`*:

**Linux/macOS:**
```bash
python3 script.py
```

**Windows:**
```bash
python script.py
```