import argparse
import sys
import os
import importlib

# Map font names from command line to python file module names
FONT_MODULES = {
    "3d_diagonal": "ascii_letters_3d_diagonal",
    "bulbhead": "ascii_letters_bulbhead",
    "ghost": "ascii_letters_ghost",
    "graffiti": "ascii_letters_graffiti",
    "roman": "ascii_letters_roman",
    "standard": "ascii_letters_standard",
}


def print_side_by_side(art_strings, gap=1):
    """Combines multi-line ASCII strings and prints them horizontally."""
    if not art_strings:
        return

    split_arts = [art.split("\n") for art in art_strings]
    max_lines = max(len(art) for art in split_arts)

    padded_arts = []
    for art in split_arts:
        max_width = max(len(line) for line in art) if art else 0
        padded_lines = [line.ljust(max_width) for line in art]
        while len(padded_lines) < max_lines:
            padded_lines.append(" " * max_width)
        padded_arts.append(padded_lines)

    spacing = " " * gap
    for line_idx in range(max_lines):
        combined_line = spacing.join(art[line_idx] for art in padded_arts)
        print(combined_line)


def render_block(text, ascii_dict):
    """Renders a single line of text side-by-side using the ASCII dictionary."""
    art_list = []
    for char in text:
        if char in ascii_dict:
            art_list.append(ascii_dict[char])
        else:
            # Fallback for characters not found in dict
            art_list.append(char)
    print_side_by_side(art_list)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Render ASCII text banners from custom font files.\n\n"
            "AVAILABLE FONTS:\n"
            "  • 3d_diagonal\n"
            "  • bulbhead\n"
            "  • ghost\n"
            "  • graffiti\n"
            "  • roman\n"
            "  • standard (default)\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example:\n  python3 terminal_font.py -f ghost -t \"ABC abc -br 123 !@#\""
    )

    parser.add_argument(
        "-f",
        "--font",
        choices=list(FONT_MODULES.keys()),
        default="standard",
        metavar="FONT",
        help="Select the ASCII art font to use",
    )

    parser.add_argument(
        "-t",
        "--text",
        required=True,
        metavar="TEXT",
        help="The text string to display. Use '-br' inside quotes to break lines.",
    )

    args = parser.parse_args()

    # Load the requested font module dynamically
    module_name = FONT_MODULES[args.font]
    try:
        font_module = importlib.import_module(module_name)
        ascii_dict = getattr(font_module, "ascii_dict")
    except (ImportError, AttributeError) as e:
        print(f"Error: Could not load font file '{module_name}.py'. Make sure it exists.")
        sys.exit(1)

    # Split text by '-br' for line breaks
    text_lines = args.text.split("-br")

    # Render each block separated by line breaks
    for line in text_lines:
        clean_text = line.strip()
        if clean_text:
            render_block(clean_text, ascii_dict)


if __name__ == "__main__":
    main()