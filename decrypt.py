# Decrypt password-protected PDF in Python.
# 
# Requirements:
# pip install PyPDF2, PyCryptodome, pikepdf

import PyPDF2
import camelot

from pprint import pprint


def decrypt_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as input_file, \
            open(output_path, 'wb') as output_file:
        reader = PyPDF2.PdfFileReader(input_file)
        reader.decrypt(password)

        writer = PyPDF2.PdfFileWriter()

        for i in range(reader.getNumPages()):
            writer.addPage(reader.getPage(i))

        writer.write(output_file)


def filter_list(list: list[list]):
    new_list = []

    for row in list:
        if 'Saldo' in row[0]:
            continue
        if 'Data' in row[0]:
            continue
        for col in row:
            new = col.strip()
            col = new[0]
            new_list.append(col)
    return new_list


def clean_data(list):
    index = 0
    for item in list:
        item['Date'] = item.pop(0)
        item['Title'] = item.pop(1)
        item['Amount'] = item.pop(2)
        item.pop(3)
        
    for item in list:
        item['Date'] = item['Date'].split('\n')[0]
        item['Title'] = item['Title'].replace('\n', '')
        
    pprint(list)    
    return list


def read_tables():
    tables = camelot.read_pdf("decrypted.pdf", pages='all')
    list = []

    for table in tables[1:]:
        temp = table.df.to_dict('records')
        list = list + temp
    
    return clean_data(list)
    

def sort_data(dicts):
    total = 0
    for item in dicts:
        if 'DOJADE' in item['Title'].upper():
            # print(item['Amount'])
            total += float(item['Amount'].replace(',', '.'))
    print(total)

if __name__ == '__main__':
    # decrypt_pdf('encrypted.pdf', 'decrypted.pdf', '')
    sort_data(read_tables())
