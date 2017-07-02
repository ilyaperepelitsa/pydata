import sqlite3
import pandas as pd
from pandas import DataFrame

query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL, d INTEGER );"""

con = sqlite3.connect(":memory:")
con.execute(query)
con.commit()

data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]

stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

con.executemany(stmt, data)
con.commit()


cursor = con.execute("select * from test")
rows = cursor.fetchall()

rows

DataFrame(rows, columns = list(zip(*cursor.description))[0])

import pandas.io.sql as sql
# just a much easier way to read the same data into DataFrame

sql.read_sql('select * from test', con)






### MONGODB

import pymongo
con = pymongo.Connection("localhost", port = 27017)
