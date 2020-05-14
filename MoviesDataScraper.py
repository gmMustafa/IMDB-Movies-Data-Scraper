# Friday, 15 May 2020 (GMT+5)
# MOVIE DATA SCRAPER
# BY : GHULAM MUSTAFA

# Disclaimer : Data scraped from "www.imdb.com" only for development purpose

# import libraries
import urllib.request as req
from bs4 import BeautifulSoup
import csv


print("Processing....")

# url of the page to scrap data from
url_page = 'https://www.imdb.com/chart/top/'

# Getting data from url
page = req.urlopen(url_page)

# parse the html using beautiful soup and store in 'raw_soup'
raw_soup = BeautifulSoup(page, 'html.parser')

# parse the table with all the data
table = raw_soup.find('table', attrs={'class': 'chart full-width'})
body = table.find('tbody')
results = body.find_all('tr')

# check for entries found
print('Number of results', len(results))

# create and write headers to a list
rows = [['Rank', 'Title', 'year', 'Rating', 'Mains', 'Thumbnail']]

# iterate for results
for result in results:
    # find all attributes per result
    data = result.find_all('td')

    # if found empty skip
    if len(data) == 0:
        continue

    # Rank for the movie
    rank = data[1].contents[0]
    rank = rank.split('.')
    # Remove white spaces
    rank = rank[0].strip()

    # Thumbnail Image
    thumbnail = data[0].find('img').get('src')

    # Title of the Movie
    title = data[0].find('img').get('alt')

    # Main leads and director
    mains = data[1].find('a').get('title')

    # year of release
    year = data[1].find('span').contents[0][1:5]
    rating = data[2].find('strong').contents[0]

    # Append data in list
    rows.append([rank, title, year, rating, mains, thumbnail])

# Create csv and write rows to output file
with open('top250.csv', 'w', newline='') as file_output:
    csv_output = csv.writer(file_output)
    csv_output.writerows(rows)

# Completed
print("Done. Check your CSV FILE")
