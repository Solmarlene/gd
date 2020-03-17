from bs4 import BeautifulSoup

from genders.models import Entry

def convert_dictionary():
    print("starting convertor")
    with open("dictionary.xml", "r", encoding="utf-8") as f:
        content = f.read()
        soup = BeautifulSoup(content)
       # import pdb; pdb.set_trace() 
        for record in soup.find_all("w"):
            word = record.c
            tags = record.t
            gender = None

            # tags is a string
            # {m} or {f} or {fm}
            if 'm' in tags and 'f' in tags:
                gender = 'B'
            elif 'm' in tags:
                gender = 'M'
            elif 'f' in tags:
                gender = 'F'

            entry = Entry(word=word, gender=gender)


if __name__ =='__main__':
    convert_dictionary()

