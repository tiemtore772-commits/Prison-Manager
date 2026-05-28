import json
import os

ARCHIVE_FILE = "archives.json"


class ArchiveManager:
        def __init__(self):
            if not os.path.exists(ARCHIVE_FILE):
                with open(ARCHIVE_FILE, "w") as f:
                    json.dump([], f)

        def archive_prisoner(self, prisoner_data):
            with open(ARCHIVE_FILE, "r") as f:
                archives = json.load(f)

            archives.append(prisoner_data)

            with open(ARCHIVE_FILE, "w") as f:
                json.dump(archives, f, indent=4)

            print("✅ Prisonnier archivé avec succès.")

        def show_archives(self):
            with open(ARCHIVE_FILE, "r") as f:
                archives = json.load(f)

            if not archives:
                print("Aucune archive disponible.")
                return

            print("\n===== ARCHIVES =====")
            for prisoner in archives:
                print(f"""
ID : {prisoner.get('id')}
Nom : {prisoner.get('name')}
Crime : {prisoner.get('crime')}
Peine : {prisoner.get('sentence')} ans
-------------------------
""")
                