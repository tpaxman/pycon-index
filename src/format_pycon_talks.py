import re
import bs4
import pathlib as pl
import pandas as pd
import sys


def main():

    inputfile, outputfile = sys.argv[1:]

    # formatting to markdown style
    df = pd.read_csv(inputfile)
    df['formatlist'] = '- [' + df.title + ']' + '(' + df.url + ')'
    df  = df.groupby('year')['formatlist'].agg('\n'.join).reset_index()
    g = '---\ntitle: Pycon YouTube Videos\n---\n\n' + '\n\n\n'.join('## ' + df.year.astype(str) + '\n\n' + df.formatlist)
    pl.Path(outputfile).parent.mkdir(exist_ok=True)  
    with open(outputfile, 'w') as f:
        f.write(g)


if __name__ == '__main__':
    main()
