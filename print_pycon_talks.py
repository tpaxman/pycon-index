import pandas as pd
df = pd.read_csv('pycon_talks.csv')
df['title'] = df['title'].str.replace('   ', ' - ')
df['formatlist'] = '- [' + df.title + ']' + '(' + df.url + ')'
df2  = df.groupby('year')['formatlist'].agg('\n'.join).reset_index()

g = '\n\n\n'.join('# ' + df2.year.astype(str) + '\n\n' + df2.formatlist)

with open('pycon-talks.md', 'w') as f:
    f.write(g)
