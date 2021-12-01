import sqlite3

db = sqlite3.connect("database.db")
db.isolation_level = None

db.execute(
    "CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY, author TEXT, title TEXT, published DATE")
#db.execute("CREATE TABLE IF NOT EXISTS Blogs (id INTEGER PRIMARY KEY, blog_name TEXT, post TEXT, post_date DATE")
#db.execute("CREATE TABLE IF NOT EXISTS Videos (id INTEGER PRIMARY KEY, ...")
#db.execute("CREATE TABLE IF NOT EXISTS Tips (id INTEGER PRIMARY KEY, book_id INTEGER REFERENCES Books(id), blog_id INTEGER REFERENCES Blogs(id), video_id INTEGER REFERENCES Videos(id)")


def add_book(author, title, published):
    db.execute("INSERT INTO Books (author, title, published) VALUES (?, ?, ?)", [
               author, title, published])


def find_tips():
    tips = db.execute("SELECT * FROM Books ORDER BY published")
    return tips
