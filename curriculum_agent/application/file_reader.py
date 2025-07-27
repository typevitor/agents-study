from PyPDF2 import PdfReader

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_pdf(self):
        try:
            with open(self.file_path, 'rb') as file:
                reader = PdfReader(file)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() or ''
                return text
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return None