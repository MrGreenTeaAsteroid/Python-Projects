# x is hourly wage
# y is hours
# z is holiday wage
def wage():
    x = float(input("What is your hourly wage? "))
    week1 = float(input("How many hours did you work in the first week? (including holidays) ")) 
    week2 = float(input("How many hours did you work in the second week? (including holidays) ")) 
    y = week1 + week2
    print("Did you work during holidays?") 
    answer = input("yes/no? ").lower()
    
    if answer == "yes":
        week1Holiday = float(input("How many holiday hours in the first week? ")) 
        week2Holiday = float(input("How many holiday hours in the second week? "))
        z = ((week1Holiday + week2Holiday) * 2 * x)
        y = (week1 - week1Holiday) + (week2 - week2Holiday)
    else: 
        z = 0
    
    annual_income = x * 52 * 40
    if annual_income < 53359:
        tax = 15 / 100
    elif annual_income < 106717:
        tax = 20.5 / 100
    elif annual_income < 165430:
        tax = 26 / 100
    else: 
        tax = 33 / 100
    
    net_income = (x * y + z) * (1 - tax)
    
    print("You will receive: ")
    print(net_income)

wage()