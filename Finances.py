from datetime import datetime


def register_bail(data):
    print("\n── REGISTER BAIL ──")
    
    # Enter inmate ID

 
    inmate_id = input("Inmate ID: ").strip().upper()

     # Search for the inmate

    
    inmate = next((d for d in data["inmates"] if d["id"] == inmate_id), None)
    

# Check if the inmate exists

    if not inmate:
        print("Inmate not found.")
        return data
# Enter amount 

    try:
        amount = float(input("Bail amount (FCFA): ").strip())
    except ValueError:
        print(" Invalid amount.")
        return data

    # Create financial record 

    bail = {
        "inmate_id": inmate_id,
        "inmate_name": f"{inmate['first_name']} {inmate['last_name']}",
        "amount": amount,
        "type": input("Type (bail/fine/fees): ").strip().lower(),
        "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "notes": input("Notes (optional): ").strip()
    }
# Add to finance list
    data["finances"].append(bail)
    print(f"Bail of {amount:,.0f} FCFA registered for {bail['inmate_name']}.")

    return data

def view_summary(data):
    print("\n--FINANCIAL SUMMARY --")
 
# Check if transactions exist

    if not data["finances"]:
        print("No transactions recorded.")
        return

    total = 0

# Sort transactions by type


    bails = [f for f in data["finances"] if f["type"] == "bail"]
    fines = [f for f in data["finances"] if f["type"] == "fine"]
    fees  = [f for f in data["finances"] if f["type"] == "fees"]

# Display header
    
    print(f"\n  {'TYPE':<12} {'INMATE':<25} {'AMOUNT':>15}  {'DATE'}")
    print("  " + "─" * 65)

    # Display transactions 

    for f in data["finances"]:
        total += f["amount"]

        print(
            f"  {f['type'].capitalize():<12} "
            f"{f['inmate_name']:<25} "
            f"{f['amount']:>13,.0f}F  "
            f"{f['date']}"
        )

# Display totale 
    
    print("  " + "─" * 65)
    print(f"  {'TOTAL':>38} {total:>13,.0f} FCFA")

# Summary by category
    
    print(f"\n  Bail  : {sum(x['amount'] for x in bails):>10,.0f} FCFA ({len(bails)} entries)")
    print(f"  Fines : {sum(x['amount'] for x in fines):>10,.0f} FCFA ({len(fines)} entries)")
    print(f"  Fees  : {sum(x['amount'] for x in fees):>10,.0f} FCFA ({len(fees)} entries)")


def inmate_summary(data):
    print("\n── SUMMARY BY INMATE ──")

# Enter inmate ID
    
    inmate_id = input("Inmate ID: ").strip().upper()

# Search inmate transactions

    transactions = [f for f in data["finances"] if f["inmate_id"] == inmate_id]


    if not transactions:
        print(" No transactions found for this inmate.")
        return

# Calculate total

    total = sum(f["amount"] for f in transactions)

# Display transactions

    for f in transactions:
        print(
            f"  {f['date']} | "
            f"{f['type'].capitalize()} | "
            f"{f['amount']:,.0f} FCFA | "
            f"{f['notes']}"
        )
    print(f"  TOTAL: {total:,.0f} FCFA")


def finances_menu(data):

    while True:
        print("\n FINANCES    ")
        print("")
        print("  1. Register a bail/fine")
        print("  2. View overall summary")
        print("  3. Summary by inmate")
        print("  0. Back")
        print("")

        choice = input(" ").strip()

        if choice == "1":
            data = register_bail(data)

        elif choice == "2":
            view_summary(data)

        elif choice == "3":
            inmate_summary(data)

        elif choice == "0":
            break

        return data