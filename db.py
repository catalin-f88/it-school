import sqlite3
from pathlib import Path

class Database:

    def __init__(self, db_file_path: Path, create_table_query: str) -> None:
        self.connection = sqlite3.connect(db_file_path)
        self.cursor = self.connection.cursor()
        self.create_table_query = create_table_query

""" Metoda care creaza tabelul pe baza query-ului """

    def read_all(self):
        rows = self.cursor.execute("SELECT * FROM ?;", (self.table))
        return rows.fetchall()
    
    def create (self, name, telefon)
    def update
    def delete

class ContactsDb:
    """ query hardcoded cu tabelul de contacts; primeste ca argument doar db_file_path""" 
    pass