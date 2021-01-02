from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
#import docx
#import msoffcrypto
#import io
#import pandas as pd



def getPDF(path, key):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams(char_margin=20, line_margin=1, detect_vertical=True)
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    caching = True
    pagenos = set()

    for PageNumer, page in enumerate(PDFPage.get_pages(fp, pagenos, password=key, caching=caching, check_extractable=False)):
        interpreter.process_page(page)
    key = None
    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()
    return text


# def getDoc(path, password):

#     file = msoffcrypto.OfficeFile(open(path, "rb"))

#     # Use password
#     file.load_key(password=password)

#     decrypted = io.BytesIO()
#     file.decrypt(decrypted)

#     doc = docx.Document(decrypted)
#     password = None
#     fullText = []
#     for para in doc.paragraphs:
#         fullText.append(para.text)
#     return '\n'.join(fullText)
