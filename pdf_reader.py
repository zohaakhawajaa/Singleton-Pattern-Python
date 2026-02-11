import PyPDF2
from model import SystemInfo

class PdfFileReader:
    @staticmethod
    def read(path):
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = reader.pages[0].extract_text()

        lines = text.splitlines()
        return SystemInfo(lines[0], lines[1], lines[2])
