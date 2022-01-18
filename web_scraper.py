from bs4 import BeautifulSoup
from nbformat import write
import requests
import csv

wiki_url = "https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
google_base_url = "https://www.google.com/search?q="
r1 = requests.get(url=wiki_url)
soup1 = BeautifulSoup(r1.content, "html5lib")
table1 = soup1.find("table", attrs={"class": "wikitable sortable"})
table_body = table1.find("tbody")
rows = table_body.find_all("tr")
coordinates = []
for row in rows[1:11]:
    a_tags = row.find_all("a")[0]
    city = a_tags.contents[0]
    google_searc_url = google_base_url + city + "+lat" + "+long"
    r2 = requests.get(url=google_searc_url)
    soup2 = BeautifulSoup(r2.content, "html5lib")
    table2 = soup2.findAll("div", attrs={"class": "BNeawe iBp4i AP7Wnd"})
    tag = table2[-1]
    lst = tag.contents
    s = lst[0]
    s = s.split()
    lat = s[0][:6]
    lon = s[2][:6]
    coordinates.append(
        {
            "city": city,
            "lat": lat,
            "lon": lon
        }
    )

print(coordinates)

field_names = ["city", "lat", "lon"]

with open("coordinates.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(coordinates)