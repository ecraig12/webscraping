import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get(
    'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=01&ref_=adv_nxt')

soup = BeautifulSoup(response.text, 'html.parser')

films = soup.find_all(class_='lister-item-content')

with open('Films.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Rank', 'Title', 'Year', 'Runtime', 'Genre']
    csv_writer.writerow(headers)

    for film in films:
        rank = film.find(class_='lister-item-index').get_text().replace('\n', '')
        title = film.find('h3').a.text.strip() 
        year = film.find(class_='lister-item-year').get_text().replace('\n', '')
        runtime = film.select('.runtime')[0].get_text()
        genre = film.select('.genre')[0].get_text().replace('\n', '')
        csv_writer.writerow([rank, title, year, runtime, genre])
        print(rank, title, year, runtime, genre)

'''
for film in films:
    #title = film.find(class_='lister-item-header').get_text().replace('\n', '') - doesn't work properly when printing to CSV
    #title = film.find('a').attrs['href']                                        # returns films as /title/tt0057565/
    #title = film.find('a', class_='lister-item-header')['href']                 #NoneType object is not subscriptable
    #title = film.find('a', class_='lister-item-header')                         # returns none
    #title = film.find(class_='lister-item-header').get_text()                   # returns entire div
    #title = film.find('a', class_='lister-item-header')                         # returns none
    #title = film.find('a', href=True).get_text()                                # returns 50 lines of nothing
    #title = film.select_all('a', class_='lister-item-header').get_text()    
    ###title = film.find('h3').a.text.strip()                   
    #title = film.find('href', 'a')
    #title = film.find(class_='lister-item-header').get_text().replace('\n', '')
    #title = film.find('a')['href'].string().get_text()
    #title = film.find('h3').a.text.strip()
    #print(title)
'''