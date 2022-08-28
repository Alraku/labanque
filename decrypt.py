# Decrypt password-protected PDF in Python.
# 
# Requirements:
# pip install PyPDF2, PyCryptodome, pikepdf

from PyPDF2 import PdfFileReader, PdfFileWriter


def decrypt_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as input_file, \
            open(output_path, 'wb') as output_file:
        reader = PdfFileReader(input_file)
        reader.decrypt(password)

        writer = PdfFileWriter()

        for i in range(reader.getNumPages()):
            writer.addPage(reader.getPage(i))

        writer.write(output_file)


def main():
    import pikepdf

    with pikepdf.open("encrypted.pdf", password="") as pdf:
        num_pages = len(pdf.pages)
        print("Total pages:", num_pages)


if __name__ == '__main__':
    # example usage:
    decrypt_pdf('encrypted.pdf', 'decrypted.pdf', '')
    # main()
