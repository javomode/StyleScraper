from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://en.wikipedia.org/wiki/List_of_most-visited_websites" #site containing the most visited websites
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")

table = soup.find('table')



titles = table.find_all('th')
titles = [title.text.strip() for title in titles] #don't want Ranking
titles = titles[0:2] + titles[-2:] + titles[3:6] #rearrange to match table on site



df = pd.DataFrame(columns=titles)



column_data = table.find_all('td')



for idx in range(0,len(column_data), 7):
    individual_row_data = [column_data[idx+col_idx].text.strip() for col_idx in range(7)]

    df.loc[len(df)] = individual_row_data

