import argparse
import os
import sys
from pathlib import Path


def search_single_folder(
    folder_path: Path, the_word: str, file_type: str = "*"
):
    clean_ext = file_type.lstrip(".").lower()
    search_term = the_word.lower()
    pattern = f"*.{clean_ext}" if clean_ext != "*" else "*"

    try:
        for file_path in folder_path.glob(pattern):
            if file_path.is_file():
                _search_file_content(file_path, search_term, the_word)
    except (PermissionError, OSError):
        pass


def search_recursive_folder(
    folder_path: Path, the_word: str, file_type: str = "*"
):
    clean_ext = file_type.lstrip(".").lower()
    search_term = the_word.lower()
    pattern = f"*.{clean_ext}" if clean_ext != "*" else "*"

    try:
        for file_path in folder_path.rglob(pattern):
            try:
                if file_path.is_file():
                    _search_file_content(file_path, search_term, the_word)
            except (PermissionError, OSError):
                continue
    except (PermissionError, OSError):
        pass


def _search_file_content(file_path: Path, search_term: str, raw_word: str):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            for line_num, line in enumerate(file, 1):
                if search_term in line.lower():
                    print(
                        f"[FOUND] Match: '{raw_word}' -> File: {file_path} (Line {line_num})"
                    )
    except (PermissionError, FileNotFoundError, OSError):
        pass


def main():
    parser = argparse.ArgumentParser(
        description="Fast File Content Searcher - Search for words inside text files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python3 main.py -p /home/user/Desktop/my_folder -w "hello kurdistan"
  python3 main.py -rp /home/user/Desktop -w "hello kurdistan" -t txt
  python3 main.py -S -rp /root -w "secret"
        """,
    )

    path_group = parser.add_mutually_exclusive_group(required=True)
    path_group.add_argument(
        "-p",
        "--path",
        type=Path,
        metavar="FOLDER",
        help="Search ONLY in the target folder (single level)",
    )
    path_group.add_argument(
        "-rp",
        "--recursive-path",
        type=Path,
        metavar="FOLDER",
        help="Search in target folder AND all subfolders (recursive)",
    )

    parser.add_argument(
        "-w",
        "--word",
        type=str,
        required=True,
        metavar="TEXT",
        help="The search string/word to look for",
    )

    parser.add_argument(
        "-t",
        "--type",
        type=str,
        default="*",
        metavar="EXT",
        help="File extension filter (e.g. txt, py). Default: * (all files)",
    )

    parser.add_argument(
        "-S",
        "--sudo",
        action="store_true",
        help="Re-run the script with root privileges (sudo) to access protected files",
    )

    args = parser.parse_args()

    if args.sudo and os.geteuid() != 0:
        print("[+] Re-running script with sudo privileges...")
        cmd = ["sudo", sys.executable] + sys.argv
        os.execvp("sudo", cmd)

    target_path = args.path if args.path else args.recursive_path

    if not target_path.exists():
        print(f"Error: Path '{target_path}' does not exist.")
        sys.exit(1)

    if args.path:
        print(
            f"\n--- Searching Single Level for '{args.word}' in '{target_path}' ---"
        )
        search_single_folder(target_path, args.word, args.type)
    else:
        print(
            f"\n--- Searching Recursively for '{args.word}' in '{target_path}' ---"
        )
        search_recursive_folder(target_path, args.word, args.type)

    print("\nSearch finished successfully.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Search cancelled by user. Exiting cleanly...")
        sys.exit(0)