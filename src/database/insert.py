
import sqlite3

class Insert:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('src/database/database.db')
    
    def insert_link_and_data(self,link,data):
        
        link_db = self.conn.execute(f"INSERT INTO TC_LINK (NAME,DOWNLOAD_LINK) \
            VALUES (?,?)",(link.name,link.download_link))
        
        self.conn.execute("INSERT INTO TC_DATA (COMPANY_EIN,COMPANY_NAME, DATA, LINK_ID) \
            VALUES (?,?,?,?)",(data.company_ein,data.company_name,data.data, link_db.lastrowid))
        
        self.conn.commit()
        return True
