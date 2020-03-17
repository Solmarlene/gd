import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gd.settings")
django.setup()

from bs4 import BeautifulSoup

from genders.models import Entry

def convert_dictionary():
    print("starting convertor")
    Entry.objects.all().delete()
    print("deleted entries")
    with open("dictionary.xml", "r", encoding="utf-8") as f:
        content = f.read()
        soup = BeautifulSoup(content)
       # import pdb; pdb.set_trace() 
        for index, record in enumerate(soup.find_all("w")):
            word = record.c.text
            tags = record.t.text
            gender = None

            # tags is a string
            # {m} or {f} or {fm}
            if "{mf}" in tags:
                gender = 'B'
            elif "{m}" in tags:
                gender = 'M'
            elif "{f}" in tags:
                gender = 'F'
            if gender is not None:
                entry = Entry(word=word, gender=gender)
                entry.save()
            
            print ("Procesing entry No %s, the word is %s, %s" 
            % (index, word, gender))


if __name__ =='__main__':
    django.setup()
    convert_dictionary()

