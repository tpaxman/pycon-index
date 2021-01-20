import re
import bs4
import pathlib as pl
import pandas as pd
import sys


def main():

    inputfolder, outputfile = sys.argv[1:]

    df_tables = []
    for x in pl.Path(inputfolder).glob('*.html'):
        print(x)
        with open(x, encoding='utf-8') as f:
            html = f.read()
            year = int(re.sub(r'.*-(\d+)', r'\1', x.stem))
            soup = bs4.BeautifulSoup(html, features='lxml')
            if year > 2013:
                chunks = soup.find_all(id='video-title')
                urls = [x['href'] for x in chunks]
                titles = [x['title'] for x in chunks]
            else:
                chunks = soup.find_all(id='content', class_='style-scope ytd-playlist-video-renderer')
                urls = [re.sub(r'(.*)&list.*', r'\1', x.find('a', class_='yt-simple-endpoint style-scope ytd-playlist-video-renderer')['href'])
                        for x in chunks]
                titles = [x.find('span', id='video-title')['title'] for x in chunks]
            items = list(zip(titles, urls)) 
            df = pd.DataFrame(items).rename(columns={0: 'title', 1: 'url'})
            df['year'] = year
            df['url'] = "https://www.youtube.com" + df['url']
            df_tables.append(df)

    df = pd.concat(df_tables)



    df.to_csv(outputfile, index=False)




if __name__ == '__main__':
    main()
