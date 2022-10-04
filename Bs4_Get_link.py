import os.path

import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
   'authority': 'www.google.com',
   # 'method': 'GET',
   # 'path': '/search?channel=fs&client=ubuntu&q=beautifulsoup+python',
   # 'scheme': 'https',
   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
   # 'accept-encoding': 'gzip, deflate, br',
   'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
   'cache-control': 'max-age=0',
   # 'cookie': 'AEC=AakniGPs_gkDeVXSJczHhxpc50QcNh1Hv2HNCr28K5CHIRbwGdxSnc1aXw; OTZ=6697986_34_34__34_; NID=511=Uc5f58IxwrcXP8lScsSkFgUH7inLZXUxo32OKwW68tDvb2OMpe471nX8vKHL4tbD6s8_8ElnUgmfg4eU638_Ye3BArNebV_YG2WTaiS8ER_Mnd-BzuwqlbiVb9Go8ZUNvYE8jpmKwTuK_lu9-ohBA1PtjC0CTwDv3mKxz4_OdUw; DV=0_Z9bSv4tsAgQL5Nu0W6IhdZ2USTN1iMYpTpdNrEaQIAAAA; 1P_JAR=2022-09-26-09',
   'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
   # 'sec-ch-ua-arch': '"x86"',
   # 'sec-ch-ua-bitness': '"64"',
   # 'sec-ch-ua-full-version': '"105.0.5195.125"',
   # 'sec-ch-ua-full-version-list': '"Google Chrome";v="105.0.5195.125", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.125"',
   # 'sec-ch-ua-mobile': '?0',
   # 'sec-ch-ua-model': '""',
   'sec-ch-ua-platform': '"Linux"',
   # 'sec-ch-ua-platform-version': '"5.15.0"',
   # 'sec-ch-ua-wow64': '?0',
   'sec-fetch-dest': 'document',
   # 'sec-fetch-mode': 'navigate',
   # 'sec-fetch-site': 'same-origin',
   # 'sec-fetch-user': '?1',
   # 'upgrade-insecure-requests': '1',
   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}
# resp = requests.get("https://www.google.com/search?channel=fs&client=ubuntu&q=beautifulsoup+python",headers=headers)
# print(resp.text)
# print(resp.status_code)
# abc = resp.text
with open("index_3.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# soup = BeautifulSoup(abc, 'html.parser')
links_tag = soup.find(class_="v7W49e")
# links_tag = soup.find(id="rso")
# links_tag = soup.find(id="main")
# print(len(links_tag))
name_ls = []
link_ls = []
for div_tag in links_tag:
    # print(div_tag.find_next('div').find_next('div').attrs['class'])
    # print(div_tag.attrs['class'])
    data_ls = []
    if 'ULSxyf' not in div_tag.attrs['class']:
        name_and_link = div_tag.find_next('div',class_='yuRUbf').find_next('a')
        link_ls.append(name_and_link.get('href'))
        name_ls.append(name_and_link.find_next('h3').string)

# df = pd.DataFrame(name_ls,columns=['link','Name'])
df = pd.DataFrame()
df['link'], df['Name'] = link_ls, name_ls
df.to_csv('files/link_data.csv', index=False)
df.to_excel('files/link_data.xlsx', index=False)

df.to_json('files/link_data.json', orient='split', index=False)
df.to_parquet('files/link_data.parquet', index=False)
df.to_feather('files/link_data.ftr')

