#web scrapper
import requests
from bs4 import BeautifulSoup as bs

#gathering input from the user
github_user = input("imput github user ")

#concatanating the url to make it dynamic
url = "https://github.com/" + github_user

#making the request variable
r = requests.get(url)
soup = bs(r.content, "html.parser")

#telling bs4 what data to scrape
profile_image = soup.find('img', {'alt' : 'Avatar'})["src"]
print(profile_image)


