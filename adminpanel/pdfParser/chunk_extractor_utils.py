import layoutparser as lp
import re

# Load a pre-trained layout detection model using PubLayNet
model = lp.Detectron2LayoutModel(
    config_path='lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config',
    extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.6],  # Confidence threshold
    label_map={0: "Text", 1: "Title", 2: "List", 3: "Table", 4: "Figure"}  # Label mapping
)

# Tesseract OCR engine for reading text from image blocks
ocr_agent = lp.TesseractAgent(languages='eng')


# 1️⃣ Detect layout and extract text blocks from each page into structured chunks
def extract_chunks_from_pages(images_dict):
    """
    Extracts layout-based text chunks from PDF page images with block info and inferred type.

    Args:
        images_dict (dict): Mapping of page_number -> PIL image

    Returns:
        list: List of dictionaries with raw text and layout metadata
    """
    all_chunks = []
    for page_num, image in images_dict.items():
        layout = model.detect(image)  # Detect layout blocks
        for i, block in enumerate(layout):
            if block.type in ["Text", "Title"]:  # Filter only relevant blocks
                cropped = block.crop_image(image)  # Crop the image to the block
                text = ocr_agent.detect(cropped).strip()  # OCR the cropped block
                if text:
                    all_chunks.append({
                        "text": text,
                        "chunk_type": infer_chunk_type(text, block.type),  # Use heuristic to classify
                        "page_number": page_num,
                        "order_in_doc": i,
                        "x0": block.block.x1,
                        "y0": block.block.y1,
                        "x1": block.block.x2,
                        "y1": block.block.y2
                    })
    return all_chunks


# 2️⃣ Infer a logical content type for a chunk using simple pattern rules
def infer_chunk_type(text, default="Text"):
    """
    Attempts to classify a text chunk as Code, Lesson, Example, or Exercise.

    Args:
        text (str): The chunk's text content
        default (str): Fallback label if no pattern is matched

    Returns:
        str: Type label
    """
    text_lower = text.lower()

    if text.strip().startswith(">>>") or ">>>" in text or "..." in text:
        return "Code"
    elif text_lower.startswith("try it") or "try this" in text_lower:
        return "Exercise"
    elif re.match(r"(module|chapter|section)\s+\d+", text_lower):
        return "Lesson"
    elif "for example" in text_lower or text_lower.startswith("example:"):
        return "Example"
    elif "exercise" in text_lower:
        return "Exercise"
    else:
        return default


# 3️⃣ Structure chunks specifically for use in RAG pipelines (includes metadata)
def extract_rag_chunks(document_id, toc_entry, images_dict):
    """
    Extracts and returns RAG-ready chunks from document pages with metadata.

    Args:
        document_id (str): Unique identifier of the document
        toc_entry (dict): Table of Contents entry (e.g. {'title': ..., 'level': ..., 'page': ...})
        images_dict (dict): Mapping of page_number -> PIL image

    Returns:
        list: List of RAG-formatted chunk dicts with content and metadata
    """
    all_chunks = []

    for page_num, image in images_dict.items():
        layout = model.detect(image)
        for i, block in enumerate(layout):
            if block.type in ["Text", "Title"]:
                cropped = block.crop_image(image)
                text = ocr_agent.detect(cropped).strip()
                if text:
                    chunk_type = infer_chunk_type(text, block.type)
                    all_chunks.append({
                        "content": text,  # This is what the LLM will read
                        "metadata": {     # This helps RAG filter or rank results
                            "document_id": document_id,
                            "toc_title": toc_entry['title'],
                            "chunk_type": chunk_type,
                            "page_number": page_num,
                            "order_in_doc": i,
                            "position": {
                                "x0": block.block.x1,
                                "y0": block.block.y1,
                                "x1": block.block.x2,
                                "y1": block.block.y2
                            }
                        }
                    })
    return all_chunks
