import sqlite3

class DatabaseArchive:
    def __init__(self, db_name="prison.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def show_archives_menu(self):
        self.cursor.execute("""
            SELECT archive_id, prisoner_id, name, entry_date, release_date, sentence_duration
            FROM archives
            ORDER BY release_date DESC
        """)
        rows = self.cursor.fetchall()

        print("\n" + "="*60)
        print(" MENU ARCHIVES - DETENUS LIBERES")
        print("="*60)
        print(f"{'ID':<5} {'Nom':<20} {'Entrée':<12} {'Sortie':<12} {'Peine':<6}")
        print("-" * 60)
        if rows:
            for row in rows:
                print(f"{row[0]:<5} {row[2]:<20} {row[3]:<12} {row[4]:<12} {row[5]:<6}")
        else:
            print("Aucune archive")

def menuarchive():
    db = DatabaseArchive()
    while True:
        print("\n" + "="*60)
        print(" MENU ARCHIVES")
        print("="*60)
        print("1. Afficher archives")
        print("2. Quitter")
        choix = input("Votre choix: ")

        if choix == "1":
            db.show_archives_menu()
            input("\nAppuyez sur Entrée pour revenir...")
        elif choix == "2":
            break
        else:
            print("Choix invalide")
    db.conn.close()

if __name__ == "__menuarchive__":
    main()