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

watermelon = BeautifulSoup(watermelon_page.content, 'html.parser')

# prettify() the watermelon webpage so that it is easier to read

print(watermelon.prettify())

# Parsing each tag of the html document

print([type(item) for item in watermelon.children])

# selecting the html tag from the list of BeautifulSoup objects

html = list(watermelon.children)[2]

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('HTML Content')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# Get all nested tags inside the html tag

print([item for item in html.children])

# print all the tags nested inside body tag

print([element for element in html.children])

# get all the tags inside the body tag

body = list(html.children)[3]

print()
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('BODY Content')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print(list(body.children))

print()
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('ACTUAL Content')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# Get the actual content

content = list(body.children)[7]
print(content.get_text())

# Shortcut method

# Get all the tags of a specific type

tags = watermelon.find_all('p')

# print the content of all the tags 
print([tag.get_text() for tag in tags])

# Using css classes and ids

# Get all the tags are p and have their id as RecipeModal
more_tags = watermelon.find_all(class_='small-4 columns text-center')

# Iterate the list of tags and print their content 
print([tag.get_text() for tag in more_tags])
 