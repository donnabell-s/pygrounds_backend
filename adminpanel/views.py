from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from uploadPdf.upload_handler import handle_pdf_upload
from pdfParser.page_to_image import convert_pdf_to_images
from pdfParser.chunk_extractor_utils import extract_chunks_from_pages
from pdfParser.chunk_storage import store_chunks
from pdfParser.chunk_storage import store_chunks_in_chroma  # You’ll create this helper

from adminpanel.models import TOCEntry  # Assuming you're using this
from django.shortcuts import get_object_or_404
from vector_db.chroma_manager import client as chroma_client

class UploadPDFView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        uploaded_file = request.FILES.get('file')
        title = request.POST.get('title', None)

        if not uploaded_file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Step 1: Save Document in DB
        document = handle_pdf_upload(uploaded_file, title)

        # Step 2: Convert PDF pages to images
        images_dict = convert_pdf_to_images(document.file.path)

        # Step 3: Use dummy TOC for now
        toc_entry = TOCEntry.objects.create(document=document, title="Default Section", order=0)

        # Step 4: Extract and classify chunks
        chunks = extract_chunks_from_pages(images_dict)

        # Step 5: Save to Django DB
        store_chunks(document, toc_entry, [chunk['text'] for chunk in chunks])

        # Step 6: Store in Chroma vector DB
        store_chunks_in_chroma(document.id, toc_entry, chunks)

        # ✅ Step 7: Persist Chroma to disk
        chroma_client.persist()

        return Response({
            "id": document.id,
            "title": document.title,
            "file_url": document.file.url,
            "uploaded_at": document.uploaded_at,
            "chunks_saved": len(chunks)
        }, status=status.HTTP_201_CREATED)