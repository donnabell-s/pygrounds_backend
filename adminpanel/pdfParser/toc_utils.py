import fitz  # PyMuPDF
import re

def extract_toc(pdf_path):
    """
    Extracts table of contents from PDF metadata if available.
    
    Returns:
        List of [level, title, page] entries from PDF TOC.
    """
    doc = fitz.open(pdf_path)
    return doc.get_toc()

def fallback_toc_text(doc, page_limit=9):
    """
    Scans the first few pages of the PDF for 'Table of Contents' text 
    if no metadata-based TOC is found.

    Returns:
        List of page texts that may contain TOC-like structure.
    """
    toc_pages = []
    for page_num in range(min(page_limit, len(doc))):
        text = doc.load_page(page_num).get_text()
        if "contents" in text.lower():
            toc_pages.append(text)
    return toc_pages

def parse_toc_text(toc_text_block):
    """
    Parses a block of text to extract TOC-style entries using a regex pattern.

    Expected format:
        Section Title ......... PageNumber

    Returns:
        List of dictionaries with 'title', 'start_page', and 'order'.
    """
    entries = []
    lines = toc_text_block.split('\n')
    for i, line in enumerate(lines):
        match = re.match(r"(.+?)\s+\.{2,}\s+(\d+)$", line.strip())
        if match:
            title = match.group(1).strip()
            page = int(match.group(2)) - 1  # Convert to 0-based index
            entries.append({
                "title": title,
                "start_page": page,
                "order": i
            })
    return entries

def assign_end_pages(toc_entries, total_pages):
    """
    Adds 'end_page' field to each TOC entry by looking at the start of the next one.

    Args:
        toc_entries: List of dicts with 'start_page' already filled.
        total_pages: Total number of pages in the PDF.

    Returns:
        Same list with added 'end_page' fields.
    """
    for i in range(len(toc_entries)):
        if i < len(toc_entries) - 1:
            toc_entries[i]['end_page'] = toc_entries[i + 1]['start_page'] - 1
        else:
            toc_entries[i]['end_page'] = total_pages - 1  # Last section goes till the end
    return toc_entries
