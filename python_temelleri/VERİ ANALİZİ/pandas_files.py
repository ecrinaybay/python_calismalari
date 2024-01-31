import pandas as pd
import sqlite3

# df = pd.read_csv('sample.csv') #csv dosyasını alıp okuyoruz.
# df = pd.read_json('sample.json',encoding = "UTF-8") #json dosyasını alıp okuyoruz.
# df = pd.read_excel("sample.xlsx") #excel dosyasını alıp okuyoruz.  pip install openpyxl

connection = sqlite3.connect("sample.db")
df = pd.read_sql_query("SELECT * FROM students",connection)






print(df)





