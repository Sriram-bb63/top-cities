from bs4 import BeautifulSoup
import requests
import csv

wiki_url = "https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
google_base_url = "https://www.google.com/search?q="

wiki_request = requests.get(url=wiki_url)
wiki_soup = BeautifulSoup(wiki_request.content, "html5lib")
wiki_table = wiki_soup.find("table", attrs={"class": "wikitable sortable"})
wiki_table_body = wiki_table.find("tbody")
wiki_table_rows = wiki_table_body.find_all("tr")

coordinates = []

number_of_cities = int(input("Enter top n cities to plot: "))

for row in wiki_table_rows[1:number_of_cities+1]:
    a_tags = row.find_all("a")[0]
    city = a_tags.contents[0]

    google_searc_url = google_base_url + city + "+lat" + "+long"
    google_request = requests.get(url=google_searc_url)
    google_soup = BeautifulSoup(google_request.content, "html5lib")
    google_table = google_soup.findAll("div", attrs={"class": "BNeawe iBp4i AP7Wnd"})
    tag = google_table[-1]
    city_coordinate = tag.contents
    city_coordinate = city_coordinate[0]
    city_coordinate = city_coordinate.split()
    lat = city_coordinate[0][:6]
    lon = city_coordinate[2][:6]
    
    coordinates.append(
        {
            "city": city,
            "lat": lat,
            "lon": lon
        }
    )


field_names = ["city", "lat", "lon"]

with open("coordinates.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(coordinates)