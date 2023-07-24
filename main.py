from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd
from modules.catalog import Catalog
import json

book1 = Book(
    'Title',
    'Ini subject',
    None,
    '1345-4533',
    'Singgih',
    '08526437658678'
)

book2 = Book(
    'Title 2',
    'Ini subject 2',
    None,
    '1345-4533',
    'Singgih',
    '08526437658678'
)

book3 = Book(
    'Title 3',
    'Ini subject 3',
    None,
    '1345-4533',
    'Singgih',
    '08526437658678'
)

magazine1=Magazine(
    'media cnn 1',
    'edisi 14 Juli 2023',
    None,
    'volume 1',
    '-'
)

magazine2=Magazine(
    'media cnn 2',
    'edisi 14 Juli 2023',
    None,
    'volume 2',
    '-'
)

dvd1=Dvd(
    'Test DVD 1',
    'Ini test dvd 1',
    None,
    None,
    None,
    'Comedy'
)

cd1=Cd(
    'Cd 1',
    'Subject cd 1',
    None,
    None
)

#input search
input_search='media'

#collect data per jenis
book = [book1,book2,book3]
magazine=[magazine1,magazine2]
dvd=[dvd1]
cd=[cd1]

#get data from json
f=open('files/catalog.json')
data_json=json.load(f)

#create object from data json
for item in data_json:
    if item['source']=='book':
        book.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            issbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number']
        ))
    elif item['source']=='magazine':
        magazine.append(Magazine(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            volume=item['volume'],
            issue=item['issue']
        ))
    elif item['source']=='dvd':
        dvd.append(Dvd(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            actors=item['actors'],
            directors=item['directors'],
            genre=item['genre']
        ))   
    elif item['source']=='cd':
       cd.append(Cd(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            artist=item['artist']
       )) 
    
#collect data
catalog_all=[book,magazine,dvd]

input_search='test'

result=Catalog(catalog_all).search(input_search)

if result:
    for index,result in enumerate(result):
        print(f'result ke-{index+1}|{result}')
else:
    print('no result')