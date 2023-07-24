from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd
from modules.catalog import Catalog
import json

#get data from json
f=open('files/catalog.json')
data_json=json.load(f)

#collect data from json(tidak memerlukan object yang banyak,karena membaca dari json)
book = []
magazine=[]
dvd=[]
cd=[]

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
catalog_all=[book,magazine,dvd,cd]

input_search='test'

result=Catalog(catalog_all).search(input_search)

if result:
    for index,result in enumerate(result):
        print(f'result ke-{index+1}|{result}')
else:
    print('no result')