import pathlib as pl
import bs4
import pandas as pd
import re

df_tables = []
for x in pl.Path('./html-data/').glob('*.html'):
    with open(x) as f:
        html = f.read()
        year = int(re.sub(r'.*-(\d+)', r'\1', x.stem))
        soup = bs4.BeautifulSoup(html, features='lxml')
        items = [(x['title'], f"https://www.youtube.com{x['href']}") for x in soup.find_all(id='video-title')]
        df = pd.DataFrame(items)
        df['year'] = year
        df_tables.append(df)

df = pd.concat(df_tables).rename(columns={0: 'title', 1: 'url'})
df.to_csv('pycon_talks.csv', index=False)
