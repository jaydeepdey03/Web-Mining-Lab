import requests
from bs4 import BeautifulSoup
import re
root_URL = "https://www.vit.ac.in/"

response = requests.get(root_URL)

soup = BeautifulSoup(response.content, 'html.parser')

print(response.content)