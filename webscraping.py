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