from django.db import models

class UploadedDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="pdfs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    parsed = models.BooleanField(default=False)

class DocumentChunk(models.Model):
    document = models.ForeignKey(UploadedDocument, on_delete=models.CASCADE, related_name="chunks")
    chunk_type = models.CharField(max_length=50, choices=[
        ("Header", "Header"),
        ("Module", "Module"),
        ("Lesson", "Lesson"),
        ("Section", "Section"),
        ("Subsection", "Subsection"),
        ("Text", "Text"),
        ("Table", "Table"),
        ("Figure", "Figure"),
        ("Code", "Code"),
        ("Caption", "Caption"),
    ])
    text = models.TextField()
    page_number = models.IntegerField(null=True, blank=True)
    order_in_doc = models.IntegerField()

    x0 = models.FloatField(null=True, blank=True)
    y0 = models.FloatField(null=True, blank=True)
    x1 = models.FloatField(null=True, blank=True)
    y1 = models.FloatField(null=True, blank=True)

class TOCEntry(models.Model):
    document = models.ForeignKey(UploadedDocument, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_page = models.IntegerField()
    end_page = models.IntegerField(null=True, blank=True)
    order = models.IntegerField()

    linked_chunk = models.ForeignKey(
        DocumentChunk,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Chunk extracted from these pages"
    )

    chunked = models.BooleanField(
        default=False,
        help_text="Set to True once this TOC entry has been parsed and linked to chunks"
    )
