import sqlite3

conn = sqlite3.connect('src/database/database.db')
query = (''' CREATE TABLE IF NOT EXISTS TC_LINK
            (ID           INTEGER     PRIMARY KEY,
            NAME          VARCHAR(255)     NOT NULL,
            DOWNLOAD_LINK          VARCHAR(255)     NOT NULL);''')
conn.execute(query)

query = (''' CREATE TABLE IF NOT EXISTS TC_DATA
            (ID           INTEGER      PRIMARY KEY,
            COMPANY_EIN TEXT     NOT NULL,
            COMPANY_NAME  CHAR(20) NOT NULL,
            DATA       TEXT,
            LINK_ID     INTEGER      NOT NULL,
            FOREIGN KEY(LINK_ID) REFERENCES LINK(ID)
            );''')
conn.execute(query)
conn.close()
print("DATABASE CREATED")
