import os
import glob
import spacy
import pytextrank
import en_core_web_sm
#import pt_core_news_sm
from collections import defaultdict
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from collections import defaultdict
import pandas as pd


def get_file_name(path):
    return os.path.basename(path)

def convert_pdf(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

def extract_keyterms():
    nlp = en_core_web_sm.load()
    tr = pytextrank.TextRank()
    nlp.add_pipe(tr.PipelineComponent, name='textrank', last=True)

    texts = glob.glob("./text-extraction/*.txt")
    for text in texts:
        final_result_name = './results/' + get_file_name(text).replace('txt', 'csv')
        print('Extracting key terms from text: ' + get_file_name(text) + '.')
        print('This process may take time, please wait ...')
        # Reading the text file
        arquivo = open(text, 'r', encoding='utf8')
        text = arquivo.read()
        doc = nlp(text)
        # examine the top-ranked phrases in the document
        dictFinal = defaultdict(list)
        for p in doc._.phrases:
            # print('{:.4f} {:5d}  {}'.format(p.rank, p.count, p.text))
            if (len(p.text) > 3):
                dictFinal['phrases'].append(p.text)
                dictFinal['count'].append(p.count)
                dictFinal['rank'].append(p.rank)

        dictFinal

        print('process finished, the result is in the ' + final_result_name + ' file')
        df = pd.DataFrame(dictFinal)
        df.sort_values(by=['rank', 'count'], ascending=False, inplace=True)
        df.to_csv(final_result_name)
        #print(df)


def remove_old_files():
    print('remover')


def start():

    pdflist = glob.glob("./articles/*.pdf")
    for pdf in pdflist:
        print("Working on: " + pdf + '\n')
        extract_file_name = get_file_name(pdf).replace('pdf', 'txt')

        fout = open('./text-extraction/' + extract_file_name, 'a')
        fout.write(convert_pdf(pdf))
        fout.close()

    extract_keyterms()


start()