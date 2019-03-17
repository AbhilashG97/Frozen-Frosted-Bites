# This is a sample code which explains how to use 
# the BeautifulSoup library.

from bs4 import BeautifulSoup
import requests as req

watermelon_page = req.get('https://www.watermelon.org/Recipes/Watermelon-Mojito')
print(watermelon_page)


print(watermelon_page.status_code)

# To view the html of the downloaded webpage

print(watermelon_page.content)

# Parsing the HTML of a webpage

