import sqlite3
from Menu import Menu
from Struk import last_IDpemesanan

conn = sqlite3.connect('kedaikopi.db') #Make or Connect to Database
c = conn.cursor() #Activate syntax of SQL

# def update_seq():
#     with conn:
#         c.execute ("UPDATE sqlite_sequence SET seq = 135 WHERE NAME = 'Orang'") 

# update_seq()
# conn.commit()

# conn.close()