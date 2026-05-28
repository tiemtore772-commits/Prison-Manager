# main.py
# Main navigation menu — BIT Prison Manager

from detainees import menu_detenus
from cell import menu_cellules


# ──────────────────────────────────────────
#  CONSTANTS
# ──────────────────────────────────────────

PRISON_NAME : str = "BIT PRISON MANAGER"
VERSION     : str = "v1.0"


# ──────────────────────────────────────────
#  MAIN FUNCTIONS
# ──────────────────────────────────────────

def display_welcome() -> None:
    """Displays the welcome screen."""
    print("\n" + "═" * 45)
    print(f"   {'WELCOME TO':^39}")
    print(f"   {PRISON_NAME:^39}")
    print(f"   {VERSION:^39}")
    print("═" * 45)
    print("   Burkina Institute of Technology")
    print("   Prison Management System")
    print("═" * 45)


def main_menu() -> None:
    """
    Displays the main navigation menu.
    Links all modules together.
    """
    running : bool = True

    while running:
        print("\n╔═══════════════════════════════════════╗")
        print("║         BIT PRISON MANAGER            ║")
        print("╠═══════════════════════════════════════╣")
        print("║  1. Manage Detainees                  ║")
        print("║  2. Manage Cell                       ║")
        print("║  3. Bail & Finance                    ║")
        print("║  4. Trial Dates        (coming soon)  ║")
        print("║  5. Statistics         (coming soon)  ║")
        print("║  6. Archives           (coming soon)  ║")
        print("║  0. Exit                              ║")
        print("╚═══════════════════════════════════════╝")

        choice = input("Your choice : ").strip()

        if choice == "1":
            menu_detenus()
        elif choice == "2":
            menu_cellules()
        elif choice == "3":
           print("⏳ Coming soon — finance.py not coded yet.")
        elif choice == "4":
            print("⏳ Coming soon — dates.py not coded yet.")
        elif choice == "5":
            print("⏳ Coming soon — stats.py not coded yet.")
        elif choice == "6":
            print("⏳ Coming soon — archives.py not coded yet.")
        elif choice == "0":
            print("\n👋 Goodbye! BIT Prison Manager closed.")
            running = False
        else:
            print("❌ Invalid choice. Please try again.")


# ──────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────

if __name__ == "__main__":
    display_welcome()
    main_menu()