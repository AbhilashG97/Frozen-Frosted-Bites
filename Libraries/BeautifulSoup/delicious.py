# This is another sample python script which scraps 
# data from a website.
# Link - https://www.watermelon.org/Recipes/Category/Sandwiches

from bs4 import BeautifulSoup
import requests
import pandas as pd 
import webbrowser 

# Get the website and check the status code 
website = requests.get('https://www.watermelon.org/Recipes/Category/Sandwiches')
base_image_url = 'https://www.watermelon.org/img/Recipes/'
assert(website.status_code == 200)

# Initialize BeautifulSoup to parse the website

watermelon = BeautifulSoup(website.content, 'html.parser')

# Display the webpage after fixing the identation 
print(watermelon.prettify())

watermelon_sandwiches = watermelon.find_all("ul", class_="small-block-grid-2 medium-block-grid-3 large-block-grid-4 text-center")
print(watermelon_sandwiches[0].prettify())

print("\n\n--------------------------------------------\n\n")

dishes = [dish.get_text() for dish in watermelon_sandwiches[0].find_all("span")]
print(dishes)

image_urls = [base_image_url.__add__(dish.replace(" ", "")).__add__(".jpg") for dish in dishes]
print(image_urls)

# opening all the images in the web browser
for image_url in image_urls:
    webbrowser.open_new_tab(image_url)

# compiling the data to a pandas DataFrame
data = pd.DataFrame({
    'dishes' : dishes,
    'image_url' : image_urls 
})

# Analyzing the DataFrame
print(data.head())

# Exporting the pandas DataFrame as a csv file
data.to_csv("watermelon_dishes.csv", ",")