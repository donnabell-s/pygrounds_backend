from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, dpi=200):
    """
    Converts PDF pages into a dictionary of PIL images indexed by page number.
    """
    images = convert_from_path(pdf_path, dpi=dpi)
    return {i+1: img for i, img in enumerate(images)}
