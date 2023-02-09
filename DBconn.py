import sqlite3

conn = sqlite3.connect('Records.db')
c = conn.cursor()


c.execute("""CREATE TABLE Inventory (
         PID int,
         name text,
         avail text,
         stocks int,
         price real,
         size text,
         category text
      )""")

conn.commit()

conn.close()