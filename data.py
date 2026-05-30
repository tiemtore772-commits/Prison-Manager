import sqlite3

class DatabaseData:
    def __init__(self, db_name="prison.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def show_data_menu(self):
        self.cursor.execute("""
            SELECT p.prisoner_id, p.name, p.entry_date, p.sentence_duration, c.cell_number
            FROM prisoners p
            LEFT JOIN cells c ON p.cell_id = c.cell_id
        """)
        prisoners = self.cursor.fetchall()

        self.cursor.execute("""
            SELECT c.cell_id, c.cell_number, c.capacity, COUNT(p.prisoner_id) as occupied
            FROM cells c
            LEFT JOIN prisoners p ON c.cell_id = p.cell_id
            GROUP BY c.cell_id
        """)
        cells = self.cursor.fetchall()

        print("\n" + "="*60)
        print(" MENU DATA - DETENUS ACTUELS")
        print("="*60)

        print("\n--- LISTE DES DETENUS ---")
        print(f"{'ID':<5} {'Nom':<20} {'Entrée':<12} {'Peine':<6} {'Cellule':<8}")
        print("-" * 55)
        if prisoners:
            for row in prisoners:
                print(f"{row[0]:<5} {row[1]:<20} {row[2]:<12} {row[3]:<6} {row[4] if row[4] else 'N/A':<8}")
        else:
            print("Aucun détenu en cours")

        print("\n--- LISTE DES CELLULES ---")
        print(f"{'ID':<5} {'N° Cellule':<12} {'Capacité':<10} {'Occupée':<8}")
        print("-" * 40)
        if cells:
            for row in cells:
                print(f"{row[0]:<5} {row[1]:<12} {row[2]:<10} {row[3]:<8}")
        else:
            print("Aucune cellule")

def menu_data():
    db = DatabaseData()
    while True:
        print("\n" + "="*60)
        print(" MENU DATA")
        print("="*60)
        print("1. Afficher détenus et cellules")
        print("2. Quitter")
        choix = input("Votre choix: ")

        if choix == "1":
            db.show_data_menu()
            input("\nAppuyez sur Entrée pour revenir...")
        elif choix == "2":
            break
        else:
            print("Choix invalide")
    db.conn.close()

if __name__ == "__main__":
    menu_data()