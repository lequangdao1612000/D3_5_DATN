import sqlite3

conn = sqlite3.connect('huyquang.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS parking")
c.execute(
    """CREATE TABLE parking (id INTEGER PRIMARY KEY AUTOINCREMENT, plate TEXT, color TEXT, brand TEXT, in_time TEXT, out_time TEXT, img_path TEXT)""")

# c.execute("INSERT INTO parking VALUES (1, 'ABC123', 'RED', 'TOYOTA', '2020-01-01', '2020-01-01', 'image/path')")

# conn.commit()

# get all columns name of table
# c.execute("PRAGMA table_info(parking)")
# columns = c.fetchall()
# print(columns)
#
# c.execute("SELECT * FROM parking")
# rows = c.fetchall()
# print(rows)
