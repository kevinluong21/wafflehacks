import requests
from bs4 import BeautifulSoup

url = "https://go-upc.com/search?q="
upc = "769197404021"  # would be the user's input

search_url = url+upc

# Send a GET request to the URL
response = requests.get(search_url)

# Create a BeautifulSoup object with the response content
soup = BeautifulSoup(response.content, "html.parser")

# Extract the title
# Title: Wish Farms Strawberries, California — UPC 769197404021 — Go-UPC
title = soup.title.text
item = title.split("—", 1)  # split string at first occurrence of (en)hypen
res = item[0].strip()

# Extract the image URL
# Image URL: https://go-upc.s3.amazonaws.com/images/68385481.jpeg
image = soup.find("img")["src"]

print("Title:", res)
print("Image URL:", image)

## NOTES ##
# install pip(3) install requests beautifulsoup4

## OUTPUT ##
# Title: Wish Farms Strawberries, California
# Image URL: https://go-upc.s3.amazonaws.com/images/68385481.jpeg
