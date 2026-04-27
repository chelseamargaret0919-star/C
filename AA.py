###This program is designed to help the school community keep track of payments inside the cafeteria

students = {"1001": {"name": "Juan","balance": 100,"debt": 0,"transactions": []}}

def student_system():
    optionstate = 0

    students = {
        100001: {
            "Current Balance": 0.00,
            "Transactions": [],
            "Loan": 0.00,
            "Reminders": []
        }
    }

    student = 100001

    while True:
        try:
            print("\nSelect action by number:")
            print("1. Deposit Number")
            print("2. Buy Food")
            print("3. Take a Loan")
            print("4. View Transactions and Status")
            print("5. Log off the Program")

            optionstate = int(input("Enter number: "))

            if optionstate < 1 or optionstate > 5:
                print("Invalid option, try again.")
                continue

            print("Loading...")

            if optionstate == 1:
                depo = float(input("Enter amount to deposit (Php): "))
                students[student]["Current Balance"] += depo
                students[student]["Transactions"].append(f"Deposited ₱{depo}")
                print("Deposit successful!")

            elif optionstate == 2:
                item = input("Enter product: ")
                quan = int(input("Enter quantity: "))
                cost = float(input("Enter price (Php): "))
                totcost = quan * cost

                if students[student]["Current Balance"] >= totcost:
                    students[student]["Current Balance"] -= totcost
                    students[student]["Transactions"].append(f"Bought {quan} {item}(s) for ₱{totcost}")
                    print("Purchase Successful")
                    print("Remaining Balance: ₱", students[student]["Current Balance"])
                else:
                    print("Insufficient balance. Purchase cancelled.")

            elif optionstate == 3:
                loan = float(input("Enter loan amount (Php): "))
                students[student]["Current Balance"] += loan
                students[student]["Loan"] += loan
                students[student]["Transactions"].append(f"Loaned ₱{loan}")
                print("Loan Taken!")

            elif optionstate == 4:
                print("-------------------- Account Summary --------------------")

                print("Current Balance:", students[student]["Current Balance"])
                print("Loan Taken:", students[student]["Loan"])

                if len(students[student]["Transactions"]) == 0:
                    print("No transactions yet")
                else:
                    for t in students[student]["Transactions"]:
                        print("-", t)

                if len(students[student]["Reminders"]) == 0:
                    print("No reminders")
                else:
                    for r in students[student]["Reminders"]:
                        print("-", r)

            else:
                print("Logging off...")
                break

        except:
            print("Invalid input, try again.")

def staff_menu():
    userid = input("Enter Student User ID: ")

    if userid in students:
        student = students[userid]

        print("\nStudent Name:", student["name"])
        print("Current Balance:", student["balance"])

        price = int(input("Enter price of food: "))

        if student["balance"] >= price:
            student["balance"] -= price
        else:
            remaining = price - student["balance"]
            student["debt"] += remaining
            student["balance"] = 0

        student["transactions"].append(price)

        print("Transaction recorded.")
        print("Updated Balance:", student["balance"])
        print("Current Debt:", student["debt"])

    else:
        print("Student not found.")


def parent_menu():
    userid = input("Enter your child's User ID: ")

    if userid in students:
        student = students[userid]

        print("\nStudent Name:", student["name"])
        print("Remaining Balance:", student["balance"])
        print("Debt:", student["debt"])

        print("\nTransaction History:")
        for j in student["transactions"]:
            print("Purchased item worth:", j)

    else:
        print("Student not found.")


choice = ""

while choice.lower() != "x":
    print("""
    O. Login Menu
    X. EXIT
    """)
    print(" ")
    
    choice = input("-CHOICE- : ")

    if choice.lower() == "o":
        print("-== ENTERING LOGIN MENU . . ==-")
        
       
        while True:
            username = input("Enter User ID: ")
            
            if username == "123":
                password = input("Enter Password: ")
                print(" -== LOGIN ACCEPTED ==- ")
                print(" ")
                break
            else:
                print("ID INVALID")

        
        while True:
            print("""
1. Identification
2. Student
3. Staff (Add Transaction)
4. Parent (View Info)
5. EXIT
            """)

            choice2 = input("--Enter Choice-- : ")

            if choice2 == "1":
                print("-== CARD DETAILS ==-")
                print(f"""
== User ID ==
{username}
== Password ==
•••••••••••
            """)

            elif choice2 == "2":
                print("-== STUDENT MENU ==-")
                student_system()
       

            elif choice2 == "3":
                print("-== STAFF MENU ==-")
                staff_menu()  

            elif choice2 == "4":
                print("-== PARENT MENU ==-")
                parent_menu() 

            elif choice2 == "5":
                print(". . LOGGING OUT . . ")
                break

            else:
                print("Invalid choice.")
