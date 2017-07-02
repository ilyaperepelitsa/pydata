import pandas as pd

pew = pd.read_csv("/Users/ilyaperepelitsa/Downloads/cancer/training_text",
                    sep = "\|\|", engine='python', header = None,
                    skiprows=1, names=["ID","Text"], index_col = "ID")


pew = pd.read_csv("/Users/ilyaperepelitsa/Downloads/cancer/training_text",
                    sep = "\|\|", engine='python', header = None,
                    skiprows=1, names=["ID","Text"])
# pew = pd.read_table("/Users/ilyaperepelitsa/Downloads/cancer/training_text")
pew


result = pd.read_table('ch06/ex3.txt', sep='\s+')
pd.read_csv('ch06/ex4.csv', skiprows=[0, 2, 3])
result = pd.read_csv('ch06/ex5.csv', na_values=['NULL'])

## specifying NAs for each column
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('ch06/ex5.csv', na_values=sentinels)


data.to_csv(sys.stdout, na_rep='NULL')
data.to_csv(sys.stdout, index=False, header=False)



class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
reader = csv.reader(f, dialect=my_dialect)



obj = """ {"name": "Wes",
"places_lived": ["United States", "Spain", "Germany"], "pet": null,
"siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
{"name": "Katie", "age": 33, "pet": "Cisco"}]
} """

import json
result = json.loads(obj)
result
asjson = json.dumps(result)
asjson



## scraping and parsing
from lxml.html import parse
from urllib.request import urlopen
parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))
doc = parsed.getroot()
urls = [lnk.get('href') for lnk in doc.findall('.//a')]
urls

links = doc.findall('.//a')
lnk = links[28]
lnk.get('href')
lnk.text_content()



tables = doc.findall('.//table')
pew = tables[2]
rows = pew.findall('.//tr')
rows
def unpack(row, kind='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text_content() for val in elts]

unpack(rows[0], kind='th')


from pandas.io.parsers import TextParser
def parse_options_data(table):
    rows = table.findall('.//tr')
    header = unpack(rows[0], kind='th')
    data = [unpack(r) for r in rows[1:]]
    return TextParser(data, names=header).get_chunk()

call_data = parse_options_data(calls)
put_data = parse_options_data(puts)





frame.save('ch06/frame_pickle')
pd.load('ch06/frame_pickle')


xls_file = pd.ExcelFile('data.xls')
table = xls_file.parse('Sheet1')
