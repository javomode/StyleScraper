from selenium import webdriver
import requests


path = "C:\Users\jaden\Documents\Jaden\Python Projects\StyleScraper\edgedriver_win64\msedgedriver.exe"
wd = webdriver.Edge(path)

url = "https://www.youtube.com/" #example url to test (grabbing youtube logo)
urls
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
response = requests.get(url)  #200 is ok, 404 is not found


page_content = null

if response == 200:
    print('Worked!')
    page_content = response.text
else:
    raise Exception(f"Failed: {response.status_code}")
