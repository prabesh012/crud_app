import sqlite3
conn = sqlite3.connect('fuse.db')

c = conn.cursor()

# create a papers table table
c.execute("""CREATE TABLE IF NOT EXISTS papers(
    title text,
    author text,
    published_on text,
    uploaded_by text,
    field text,
    file BLOB
)""")

#create a user table table
c.execute("""CREATE TABLE IF NOT EXISTS users(
    name text,
    email text,
    password text
)""")


#create a fields table table
c.execute("""CREATE TABLE IF NOT EXISTS fields(
    field text
)""")


##put many  fields data into the database
fields  = [
    ('Artificial Intelligence'),
    ('Machine Learning'),
    ('Deep Learning'),('Web Development')
]
# c.executemany("INSERT INTO fields VALUES (?)", fields)

# c.execute("INSERT INTO fields VALUES ('Artifical Intelligence')")
# c.execute("INSERT INTO fields VALUES ('Machine Learning')")
# c.execute("INSERT INTO fields VALUES ('Web Development')")
# c.execute("INSERT INTO fields VALUES ('Deep Learning')")
# c.execute("INSERT INTO fields VALUES ('Networking')")



c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

conn.commit()
conn.close()