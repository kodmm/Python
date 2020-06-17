import requests
from bs4 import BeautifulSoup
# import pandas as pd
import time

#スクレイピングしたデータを入れる表を作成
#list_df = pd.DataFrame(columns=['word_of_song'])

for page in  range(1, 2):
    #曲ページ先頭アドレス
    base_url = 'https://www.uta-net.com'

    #歌詞一覧page
    url = 'https://www.uta-net.com/artist/3891/0' + str(page) + '/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find_all('td', class_="side td1")
    print(links)