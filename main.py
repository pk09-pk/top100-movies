import requests
from bs4 import BeautifulSoup

website = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(website.text, "html.parser")
Movies = [item.text for item in soup.find_all(name="h3", class_="title")]
Movies.reverse()
for text in Movies:
    print(text)

with open("Movies.txt", mode="w", encoding="utf-8") as file:
    for movie in Movies:
        file.write(f"{movie}\n")












