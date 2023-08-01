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


# def get_api_data():
#     connection = sql.connect('article.db')
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM api_data")
#     results = cursor.fetchall()
#     connection.close()
#
#     return results


def get_api_data():
    connection = sql.connect('article.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM api_data")

    # Pobierz nazwy kolumn
    column_names = [description[0] for description in cursor.description]

    # Utwórz listę słowników dla wyników zapytania
    results = [dict(zip(column_names, row)) for row in cursor.fetchall()]

    connection.close()  # Zamknij połączenie

    return results
