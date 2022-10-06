
import sqlite3


class Select:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('src/database/database.db')
    
    def select_data_by_ein(self, query):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT DATA FROM TC_DATA where COMPANY_EIN=?",(query,))
        except Exception:
            return []
        rows = cur.fetchall()
        return rows
        
    
    def select_data_by_name(self, query):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT DATA FROM TC_DATA where COMPANY_NAME=?",(query,))
        except Exception:
            return []
        rows = cur.fetchall()
        return rows
    