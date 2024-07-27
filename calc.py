def main():
    try:
        typ = input("What kind of calculation [add,multiply,subtract,divide,reminder,raise_to]: ").strip().lower()
        #amount = int(input("Enter the amount of values: "))
        calc(typ)
    except ValueError:
        print("The entered value is not a valid value")
        
def calc(typ):
    try:
        first = int(input("Enter the first value: "))
        second = int(input("Enter the second value: "))
    except ValueError:
        print("The entered value is invalid")
    if typ == "add":
        print(f"{first} + {second}= {first+second}")
    elif typ == "multiply":
        print(f"{first} x {second}= {first*second}")
    elif typ == "subtract":
        print(f"{first} - {second}= {first-second}")
    elif typ == "divide":
        print(f"{first} / {second}= {first/second}")
    elif typ == "reminder":
        print(f"{first} % {second}= {first%second}")
    elif typ == "raise_to":
        print(f"{first}^{second}= {first**second}")
    else:
        print("Smthing went wrong. Please try again ¯\_(ツ)_/¯")
    
def rerun():
    while True:
        main()
        ask = input("Do you want to run this again [yes,no]: ").strip().lower()
        if ask == "yes":
            print("Running the program again")
        else:
            break    
rerun()
