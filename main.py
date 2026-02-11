from txt_reader import TxtFileReader
from pdf_reader import PdfFileReader
from validator import ValidationService

def main():
    info = TxtFileReader.read("system.txt")
    # info = PdfFileReader.read("system.pdf")

    validator = ValidationService()

    if validator.is_valid(info.hostname, info.ip):
        print("✅ File is OK")
    else:
        print("❌ Error: Hostname or IP not found")

if __name__ == "__main__":
    main()
