import re
from PyPDF2 import PdfReader
from io import BytesIO


def extract_text_from_pdf(pdf_content):
    pdf_stream = BytesIO(pdf_content)
    reader = PdfReader(pdf_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    # Replace unpaired surrogates with a placeholder
    text = re.sub(r"[\ud800-\udfff]", "�", text)

    return text
