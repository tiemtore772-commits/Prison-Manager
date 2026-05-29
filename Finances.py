from datetime import datetime

# Function to register a bail, a fine, or fees
def register_bail(data):
    print("\n── REGISTER BAIL ──")
    
    # Ask for the inmate's ID
    inmate_id = input("Inmate ID: ").strip().upper()
    
    # Search for the inmate in the list
    inmate = next((d for d in data["inmates"] if d["id"] == inmate_id), None)
    
    # Check if the inmate exists
    if not inmate:
        print("Inmate not found.")
        return data

    # Enter the amount
    try:
        amount = float(input("Bail amount (FCFA): ").strip())
    except ValueError:
        print(" Invalid amount.")
        return data

    # Create the financial record
    bail = {
        "inmate_id": inmate_id,
        "inmate_name": f"{inmate['first_name']} {inmate['last_name']}",
        "amount": amount,
        "type": input("Type (bail/fine/fees): ").strip().lower(),
        "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "notes": input("Notes (optional): ").strip()
    }

    # Add to the finances list
    data["finances"].append(bail)

    # Confirmation message
    print(f"Bail of {amount:,.0f} FCFA registered for {bail['inmate_name']}.")

    return data


# Function to display the overall financial summary
def view_summary(data):
    print("\n--FINANCIAL SUMMARY --")

    # Check if any transactions exist
    if not data["finances"]:
        print("No transactions recorded.")
        return

    total = 0

    # Separate the different transaction types
    bails = [f for f in data["finances"] if f["type"] == "bail"]
    fines = [f for f in data["finances"] if f["type"] == "fine"]
    fees  = [f for f in data["finances"] if f["type"] == "fees"]

    # Display the table header
    print(f"\n  {'TYPE':<12} {'INMATE':<25} {'AMOUNT':>15}  {'DATE'}")
    print("  " + "─" * 65)

    # Loop through transactions
    for f in data["finances"]:
        total += f["amount"]

        print(
            f"  {f['type'].capitalize():<12} "
            f"{f['inmate_name']:<25} "
            f"{f['amount']:>13,.0f}F  "
            f"{f['date']}"
        )

    # Display the total
    print("  " + "─" * 65)
    print(f"  {'TOTAL':>38} {total:>13,.0f} FCFA")

    # Summary by category
    print(f"\n  Bail  : {sum(x['amount'] for x in bails):>10,.0f} FCFA ({len(bails)} entries)")
    print(f"  Fines : {sum(x['amount'] for x in fines):>10,.0f} FCFA ({len(fines)} entries)")
    print(f"  Fees  : {sum(x['amount'] for x in fees):>10,.0f} FCFA ({len(fees)} entries)")


# Function to display an inmate's financial summary
def inmate_summary(data):
    print("\n── SUMMARY BY INMATE ──")

    # Ask for the inmate's ID
    inmate_id = input("Inmate ID: ").strip().upper()

    # Search for the inmate's transactions
    transactions = [f for f in data["finances"] if f["inmate_id"] == inmate_id]

    # Check if any transactions exist
    if not transactions:
        print(" No transactions found for this inmate.")
        return

    # Calculate the total
    total = sum(f["amount"] for f in transactions)

    # Display the transactions
    for f in transactions:
        print(
            f"  {f['date']} | "
            f"{f['type'].capitalize()} | "
            f"{f['amount']:,.0f} FCFA | "
            f"{f['notes']}"
        )

    # Display the total
    print(f"  TOTAL: {total:,.0f} FCFA")


# Main finances menu
def finances_menu(data):

    while True:
        print("\n╔═══ FINANCES ═══╗")
        print("  1. Register a bail/fine")
        print("  2. View overall summary")
        print("  3. Summary by inmate")
        print("  0. Back")

        choice = input(" ").strip()

        # Handle menu choices
        if choice == "1":
            data = register_bail(data)

        elif choice == "2":
            view_summary(data)

        elif choice == "3":
            inmate_summary(data)

        elif choice == "0":
            break

         return data
