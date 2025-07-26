import os
from PIL import Image
import PyPDF2

def preview_file(file_path):
    if file_path.endswith((".jpg", ".png")):
        img = Image.open(file_path)
        img.show()
    elif file_path.endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            print("PDF Preview: ", reader.pages[0].extract_text())
    else:
        print("No preview available.")

if __name__ == "__main__":
    preview_file("recovered_files/recovered_1.jpg")

