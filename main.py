

from detainees import menu_detaines , inmates
from cell import cells_menu
from finances import finances_menu
from date import show_data_menu
from archive import show_archives_menu


PRISON_NAME : str = "PRISON MANAGER"
VERSION     : str = "v1.0"


def display_welcome() -> None:
    """Displays the welcome screen when the program starts."""
    print("\n" + "═" * 45)
    print(f"   {'WELCOME TO':^39}")
    print(f"   {PRISON_NAME:^39}")
    print(f"   {VERSION:^39}")
    print("═" * 45)
    print("   Burkina Institute of Technology")
    print("   Prison Management System")
    print("═" * 45)


def display_main_menu() -> None:
    """Displays the main navigation menu options."""
    print("\n ")
    print("          PRISON MANAGER                ")
    print("")
    print("  1. Manage Detainees                   ")
    print("     → Add / Search / Delete            ")
    print("                                        ")
    print("  2. Manage Cells                       ")
    print("     → Create / Assign detainees        ")
    print("                                        ")
    print("  3. Bail & Finance                     ")
    print("     → Record bail / View balance       ")
    print("                                        ")
    print("  4. Trial Dates                        ")
    print("     → Set / View trial dates           ")
    print("                                        ")
    print("  5. Archives                           ")
    print("     → Archive / View closed files      ")
    print("                                        ")
    print("  0. Exit                               ")
    print(" ")


def handle_choice(choice: str) -> bool:
    """
    Handles the user's menu choice and calls the correct module.

    Args:
        choice : The option entered by the user

    Returns:
        bool : False if user wants to exit, True otherwise
    """
    if choice == "1":
        menu_detaines()

    elif choice == "2":
        cells_menu()

    elif choice == "3":
        finances_menu(inmates)

    elif choice == "4":
        show_data_menu()

    elif choice == "5":
        show_archives_menu()

    elif choice == "0":
        print("\n Goodbye! Prison Manager closed.")
        print("   Burkina Institute of Technology\n")
        return False

    else:
        print(" Invalid choice. Please enter a number between 0 and 5.")

    return True


def main_menu() -> None:
    """
    Main loop that keeps the program running.
    Displays the menu and processes user input until exit.
    """
    running : bool = True

    while running:
        display_main_menu()
        choice : str = input("\nYour choice : ").strip()
        running = handle_choice(choice)

if __name__ == "__main__":
    display_welcome()
    main_menu()