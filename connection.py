import sqlite3

conn = sqlite3.connect('Records.db')

c = conn.cursor()
c.execute("""CREATE TABLE Records (
         numuber int,
         name text,
         status text,
         department text,
         subjects text
     )""")

conn.commit()

conn.close()