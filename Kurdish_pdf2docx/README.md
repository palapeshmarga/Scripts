# Kurdish PDF to Word Converter

A Python command-line utility that extracts text from PDF documents using the Google Gemini Vision API and outputs a formatted Microsoft Word (`.docx`) file. The tool is optimized specifically for **Kurdish (Sorani)** text transcription, ensuring correct character handling (e.g., preserving `ڵ`, `ڕ`, `ێ`, `ۆ`, `ە`) and applying proper **Right-to-Left (RTL)** formatting to the generated Word document.

---

## Features

* **High-Accuracy Vision Transcription**: Converts PDF pages into high-resolution images (300 DPI) and uses Gemini's vision capabilities (`gemini-3.6-flash`) for precise text extraction.
* **Kurdish Character Preservation**: Customized system instructions prevent character substitution errors common with Arabic OCR engines.
* **Automatic RTL Formatting**: Forces Right-to-Left alignment and bidirectionality (`w:bidi`) on paragraphs created in the resulting Word document.
* **Rate Limit Management**: Built-in exponential backoff automatically handles `429` / `RESOURCE_EXHAUSTED` API errors.
* **Persistent API Key Management**: Saves your API key locally to avoid entering it repeatedly or setting manual environment variables.

---

## Prerequisites

### 1. External Dependencies
This script relies on `pdf2image`, which requires **Poppler** installed on your system.

* **Linux**:
  ```bash
  sudo apt-get install poppler-utils
  ```

* **macOS**:
  ```bash
  brew install poppler
  ```
### 2. Python Packages

Install the required dependencies via `pip`:
  ```bash
  pip install google-genai python-docx pdf2image
```

## Configuration & Usage
### 1. Setting Up Your API Key

You can save your API key locally to `api_key.txt`:

```python
python converting.py -api "YOUR_GEMINI_API_KEY"
```

Alternatively, you can set the `GEMINI_API_KEY` environment variable directly in your environment.
<br><br>

### 2. Converting a PDF

To convert a PDF file into a Word document, pass the source PDF via `-t` / `--target` and the output document name/path via `-p` / `--path`[cite: 1]:

```python
python converting.py -t input.pdf -p output.docx
```
<hr><br>

# Command Line Arguments


| Argument     |  Short Flag  |  Description |
|--------------|--------------|--------------|
| `--api-key`  | `-api` | Save your Google Gemini API key to `api_key.txt` for persistent use. |
| `--target` | `-t` | Path to the target PDF file you wish to transcribe.
| `--path` | `-p` | Path where the output `.docx` file will be saved.

<hr><br>


# How It Works
1. **Rasterization**: `pdf2image` converts each page of the input PDF into a 300 DPI PNG image in memory.
2. **AI Processing**: The script sends each image byte stream to the `gemini-3.6-flash` model alongside system instructions tailored to Sorani Kurdish.
3. **DOCX Generation**: Extracted text lines are processed and added to a `python-docx` Document object. OpenXML elements (`w:bidi`) are appended to enforce right-to-left alignment on every output paragraph