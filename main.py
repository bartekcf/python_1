import sqlite3 as sql


con = sql.connect('article.db')
c = con.cursor()
c.execute("select * from article")
data = c.fetchall()

for article in data:
    print(article)