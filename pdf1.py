from PyPDF2 import PdfReader
from pathlib import Path

ROOT = Path(__file__).parent
PDF_PATH = ROOT / "Nick Morgan - JavaScript Crash Course-No Starch (2023).pdf"

reader = PdfReader(PDF_PATH)

# page = reader.pages[11]

print(len(reader.pages))

for page in reader.pages:
    print(page.extract_text())

# print(page.extract_text())