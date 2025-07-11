import uuid
from django.utils.text import slugify
from adminpanel.models import UploadedDocument

def handle_pdf_upload(file, title=None):
    """
    Handles saving an uploaded PDF using Django's FileField system.

    Args:
        file (UploadedFile): The uploaded PDF.
        title (str, optional): Optional title for the document.

    Returns:
        UploadedDocument: The saved model instance.
    """
    # Generate a clean title if not given
    if not title:
        title = slugify(file.name.rsplit('.', 1)[0])

    # Generate a unique filename if needed (optional)
    ext = file.name.split('.')[-1]
    file.name = f"{uuid.uuid4()}.{ext}"

    # Save the document via model
    document = UploadedDocument.objects.create(
        title=title,
        file=file  # This will auto-save to MEDIA_ROOT/pdfs/
    )
    return document
