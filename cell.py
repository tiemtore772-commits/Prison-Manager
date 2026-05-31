from detainees import Detainers, inmates


class Cell:

    def __init__(self, number, max_capacity):
        self.number    = number
        self.capacity  = max_capacity
        self.detainees = []

    def is_full(self):
        return len(self.detainees) >= self.capacity

    def add_detainee(self, detainee_id):
        if self.is_full():
            print("Cell is full.")
            return False

        if detainee_id in self.detainees:
            print("Detainee already in this cell.")
            return False

        self.detainees.append(detainee_id)
        print("Detainee added to cell " + self.number + ".")
        return True

    def remove_detainee(self, detainee_id):
        if detainee_id in self.detainees:
            self.detainees.remove(detainee_id)
            print("Detainee removed from cell " + self.number + ".")
            return True

        print("Detainee not found in this cell.")
        return False

    def show(self):
        print("\nCell: " + self.number)
        print("Capacity: " + str(len(self.detainees)) + "/" + str(self.capacity))

        if self.detainees:
            for detainee_id in self.detainees:
                if detainee_id in inmates:
                    d = inmates[detainee_id]
                    print("  " + detainee_id + " - " + d.get_prenom() + " " + d.get_nom())
        else:
            print("  Empty cell.")

    def to_dict(self):
        return {
            "number"    : self.number,
            "capacity"  : self.capacity,
            "detainees" : self.detainees
        }


cells = {}


def create_cell():
    number   = input("Cell number: ").strip().upper()
    capacity = int(input("Max capacity: "))

    if number in cells:
        print("Cell already exists.")
        return

    cells[number] = Cell(number, capacity)
    print("Cell " + number + " created.")


def assign_detainee():
    if not inmates:
        print("No detainees registered.")
        return

    if not cells:
        print("No cells created.")
        return

    detainee_id = input("Detainee ID: ").strip()
    cell_number = input("Cell number: ").strip().upper()

    if detainee_id not in inmates:
        print("Detainee not found.")
        return

    if cell_number not in cells:
        print("Cell not found.")
        return

    ok = cells[cell_number].add_detainee(detainee_id)
    if ok:
        inmates[detainee_id].set_cellule(cell_number)


def remove_detainee():
    cell_number = input("Cell number: ").strip().upper()
    detainee_id = input("Detainee ID: ").strip()

    if cell_number not in cells:
        print("Cell not found.")
        return

    ok = cells[cell_number].remove_detainee(detainee_id)
    if ok and detainee_id in inmates:
        inmates[detainee_id].set_cellule("Unassigned")


def list_cells():
    if not cells:
        print("No cells.")
        return

    for cell in cells.values():
        status = "full" if cell.is_full() else "available"
        print("  " + cell.number + " - " + str(len(cell.detainees)) + "/" + str(cell.capacity) + " - " + status)


def view_cell():
    number = input("Cell number: ").strip().upper()

    if number not in cells:
        print("Cell not found.")
        return

    cells[number].show()


def cells_menu():
    running = True

    while running:
        print("\n--- Cell management ---")
        print("1. Create a cell")
        print("2. Assign a detainee")
        print("3. Remove a detainee")
        print("4. List all cells")
        print("5. View a cell")
        print("0. Back")

        choice = input("Choice: ").strip()

        if choice == "1":
            create_cell()
        elif choice == "2":
            assign_detainee()
        elif choice == "3":
            remove_detainee()
        elif choice == "4":
            list_cells()
        elif choice == "5":
            view_cell()
        elif choice == "0":
            running = False
        else:
            print("Invalid choice.")