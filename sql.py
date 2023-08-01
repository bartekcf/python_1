import sqlite3 as sql


def add_to_database(author_p, title_p, description_p, url_p, urlToImage_p, publishedAt_p, content_p):
    connection = sql.connect('article.db')
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO article(author, title, description, url, urlToImage, publishedAt, content) VALUES (?,?,?,?,?,?,?)",
        (author_p, title_p, description_p, url_p, urlToImage_p, publishedAt_p, content_p)
    )
    connection.commit()  # Zatwierdź transakcję
    connection.close()  # Zamknij połączenie
