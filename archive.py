from detainees import inmates

class DatabaseArchive:
    def show_archives_menu(self):
        print("\n===== ARCHIVES =====")
        
        if not inmates:
            print("No inmates registered yet.")
            return
        
        for inmate in inmates:
            inmate.display_info()
            print("-" * 30)

def show_archives_menu():
    archive = DatabaseArchive()
    archive.show_archives_menu()