import argparse
import io
import os
import sys
import time
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from google import genai
from google.genai import types
from google.genai.errors import APIError
from pdf2image import convert_from_path

CONFIG_FILE = "api_key.txt"


def save_api_key(api_key):
    """Saves the API key to a local file."""
    with open(CONFIG_FILE, "w") as f:
        f.write(api_key.strip())
    print(f"API key saved successfully to '{CONFIG_FILE}'.")


def load_api_key():
    """Loads the saved API key from file or environment variable."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            key = f.read().strip()
            if key:
                return key
    return os.getenv("GEMINI_API_KEY")


def set_rtl(paragraph):
    """Enforces Right-to-Left (RTL) text flow in the Word document."""
    p_pr = paragraph._p.get_or_add_pPr()
    bidi = OxmlElement("w:bidi")
    bidi.set(qn("w:val"), "1")
    p_pr.append(bidi)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT


def process_page_with_retry(client, image_bytes, system_instruction, max_retries=5):
    """Sends page bytes to Gemini with automatic retry on rate limit errors."""
    delay = 5
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=[
                    types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
                    "Transcribe this image keeping the exact Kurdish text, words, punctuation, and structural alignment.",
                ],
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction, temperature=0.1
                ),
            )
            return response.text
        except APIError as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                print(f"Rate limit reached. Retrying in {delay} seconds... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(delay)
                delay *= 2
            else:
                raise e
    raise Exception("Exceeded maximum retries due to persistent API rate limits.")


def convert_pdf(pdf_path, output_path, api_key):
    """Converts PDF to Word document using Gemini API."""
    if not output_path.endswith(".docx"):
        output_path += ".docx"

    client = genai.Client(api_key=api_key)

    print(f"Converting '{pdf_path}' pages to visual images...")
    pages = convert_from_path(pdf_path, dpi=300)

    doc = Document()

    system_instruction = (
        "You are an expert Kurdish (Sorani) linguist and transcription engine. "
        "Your job is to accurately extract text from document images. "
        "Pay extremely close attention to Kurdish character connections, specifically preserving "
        "letters like 'ڵ', 'ڕ', 'ێ', 'ۆ', and making sure 'ە' is never replaced with standard Arabic 'ه'. "
        "Maintain the structural layout (headers, lists, tables) using Markdown formatting. "
        "Output ONLY the transcribed Kurdish text. Do not include any english explanations or introductory text."
    )

    print("Sending document images to Vision AI for transcription...")
    for idx, page in enumerate(pages):
        img_byte_arr = io.BytesIO()
        page.save(img_byte_arr, format="PNG")
        image_bytes = img_byte_arr.getvalue()

        ai_text = process_page_with_retry(client, image_bytes, system_instruction)

        if ai_text:
            for line in ai_text.split("\n"):
                clean_line = line.strip()
                if clean_line:
                    p = doc.add_paragraph(clean_line)
                    set_rtl(p)

        print(f"Finished processing page {idx + 1}/{len(pages)}")

    doc.save(output_path)
    print(f"\nSuccess! Perfect Kurdish document saved to '{output_path}'")


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF to RTL Word document using Gemini API"
    )
    parser.add_argument(
        "-api", "--api-key", type=str, help="Save Gemini API Key for future use"
    )
    parser.add_argument(
        "-t", "--target", type=str, help="Target PDF file to convert"
    )
    parser.add_argument(
        "-p", "--path", type=str, help="Output DOCX path (without or with extension)"
    )

    args = parser.parse_args()

    if args.api_key:
        save_api_key(args.api_key)
        if not args.target:
            return

    api_key = load_api_key()

    if not api_key:
        print(
            "Error: No API key found. Please register your key first using:\n"
            '  python converting.py -api "<YOUR_GEMINI_API_KEY>"'
        )
        sys.exit(1)

    if args.target and args.path:
        convert_pdf(args.target, args.path, api_key)
    elif not args.api_key:
        parser.print_help()


if __name__ == "__main__":
    main()