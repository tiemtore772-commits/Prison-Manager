import sqlite3
from detainees import inmates

class DatabaseData:
    def _init_(self, db_name="prison.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        # Crée la table si elle n'existe pas
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS detainees (
            identifier INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            crime TEXT,
            sentence_duration INTEGER,
            cell INTEGER
        )
        """)
        self.conn.commit()

    def sync_inmates(self):
        """Copie les inmates de la liste vers la base SQLite"""
        for inmate in inmates:
            self.cursor.execute("""
            INSERT OR REPLACE INTO detainees
            VALUES (?,?,?)
            """, (inmate.identifier, inmate.name, inmate.age,
                  inmate.crime, inmate.sentence_duration, inmate.cell))
        self.conn.commit()

    def show_data_menu(self):
        self.sync_inmates() # on met à jour la base

        print("\n===== DATA VIEW =====")

        self.cursor.execute("SELECT * FROM detainees")
        detainees = self.cursor.fetchall()

        if not detainees:
            print("No detainees registered yet.")
        else:
            print("\n--- Detainees ---")
            for d in detainees:
                print(f"ID: {d[0]} | Name: {d[1]} | Age: {d[2]} | Crime: {d[3]} | Sentence: {d[4]}y | Cell: {d[5]}")

def show_data_menu():
    db = DatabaseData()
    db.show_data_menu()