expenses=[]

def add_expense():
    amount=float(input("enter amount"))
    category=input("enter the category")
    expense={'amount':amount,'category':category}
    expenses.append(expense)
    print("expense added")

def show_total():
    total=0
    for e in expenses:
        total=total+e['amount']
        print(f"Total expense is{total}")

while True:
    print("1.add expense")
    print("2. total expense")

    choice=input("choose an option")
    if choice=='1':
        add_expense()
    elif choice=='2':
        show_total()

    else:
        print("invalid")



