import sqlite3

conn = sqlite3.connect('huyquang.db')
c = conn.cursor()

command = f"insert into parking values(100, '123', '123', '123', '123', '123', '123')"

c.execute(command)
# datas = c.fetchall()
# for data in datas:
#     print(data)
