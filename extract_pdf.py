import re
from PyPDF2 import PdfReader


def extract_itinerary(pdf_path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF file.

    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        # Replace unpaired surrogates with a placeholder
        text = re.sub(r"[\ud800-\udfff]", "�", text)

        return text
    except Exception as e:
        print(e)
        return ""


if __name__ == "__main__":
    pdf_path = "/home/ubuntu/Desktop/golfthing/pdfs/event_3.pdf"
    print(extract_itinerary(pdf_path))
