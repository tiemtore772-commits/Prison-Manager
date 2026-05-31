class Detainers:
    def __init__(self, identifier, name, age, crime, sentence_duration, cell):
        self.identifier = identifier
        self.name = name
        self.age = age
        self.crime = crime
        self.sentence_duration = sentence_duration
        self.cell = cell

    def display_info(self):
        print("\n===== INMATE INFORMATION =====")
        print(f"ID: {self.identifier}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years old")
        print(f"Crime: {self.crime}")
        print(f"Sentence duration: {self.sentence_duration} years")
        print(f"Cell: {self.cell}")

inmates = []

def add_inmate():
    print("\n===== ADD AN INMATE =====")

    identifier = int(input("Enter inmate ID: "))
    name = input("Enter inmate name: ")
    age = int(input("Enter inmate age: "))
    crime = input("Enter crime committed: ")
    sentence_duration = int(input("Enter sentence duration: "))
    cell = input("Enter cell number: ")

    inmate = Detainers(identifier, name, age, crime, sentence_duration, cell)
    inmates.append(inmate)

    print("\nInmate added successfully!")

def display_inmates():
    print("\n===== INMATE LIST =====")

    if len(inmates) == 0:
        print("No inmates registered.")
    else:
        for inmate in inmates:
            inmate.display_info()

def search_inmate():
    print("\n===== SEARCH FOR AN INMATE =====")

    search_id = int (input("Enter inmate ID: "))

    found = False

    for inmate in inmates:
        if inmate.identifier == search_id:
            inmate.display_info()
            found = True
            break

    if not found:
        print("Inmate not found.")

def edit_inmate():
    print("\n===== EDIT AN INMATE =====")

    edit_id = input("Enter the ID of the inmate to edit: ")

    for inmate in inmates:
        if inmate.identifier == edit_id:
            print("\nEnter new information:")

            inmate.name = input("New name: ")
            inmate.age = int(input("New age: "))
            inmate.crime = input("New crime: ")
            inmate.sentence_duration = int(input("New sentence duration: "))
            inmate.cell = input("New cell: ")

            print("\nInformation updated successfully!")
            return

    print("Inmate not found.")

def delete_inmate():
    print("\n===== DELETE AN INMATE =====")

    delete_id = int (input("Enter the ID of the inmate to delete: "))

    for inmate in inmates:
        if inmate.identifier == delete_id:
            inmates.remove(inmate)
            print("\nInmate deleted successfully!")
            return

    print("Inmate not found.")

def menu_detaines():
    while True:
        print("\n                             ")
        print("        Detainers              ")
        print("")
        print("   1. Add an inmate            ")
        print("   2. Display inmates          ")
        print("   3. Search for an inmate     ")
        print("   4. Edit an inmate           ")
        print("   5. Delete an inmate         ")
        print("   0. Quit                     ")
        print("")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_inmate()

        elif choice == "2":
            display_inmates()

        elif choice == "3":
            search_inmate()

        elif choice == "4":
            edit_inmate()

        elif choice == "5":
            delete_inmate()

        elif choice == "0":
            print("\nThank you for using the system.")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__=="__main__":
    menu_detaines()
