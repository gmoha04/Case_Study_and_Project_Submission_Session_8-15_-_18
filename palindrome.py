# piggy bank
# pre code
money=float(input("Intial money(For testing we can give intial money but in real case bank would store this amount) : "))

# function to add money to current amount
def addMoney():
    print(" ")
    userAdd = float(input("Add money : "))
    print(" ")
    money = money + userAdd
    print("After adding current Money you have is " + str(money) + " rupees")

# function to withdraw money from current amount
def withdrawMoney():
    print(" ")
    userWithdraw = float(input("Withdraw Amount : "))
    print(" ")
    money = money - userWithdraw
    if(money < 0):
        print("You dont have sufficient amount to withdraw")
    else:
        print("After Withdrawing current Money you have is " + str(money) + " rupees")

# function to display current amount
def currentMoney():
    print(" ")
    current = "Current money you have is " + str(money) + " rupees"
    print(current)
# main code
print(" ")
print("--------------------Start-------------------")
while True:
    print(" ")
    user = input("Start or End : ")
    if user.strip() == "Start":
        controlPiggy = input("Add Withdraw or Check : ")
        if controlPiggy.strip() == "Add":
            print(addMoney())
            continue
        elif controlPiggy.strip() == "Withdraw":
            print(withdrawMoney())
            continue
        elif controlPiggy.strip() == "Check":
            print(currentMoney())
            continue
        else :
            print(" ")
            print("Invalid Input.Try again")
            continue

    elif user.strip() == "End" :
        print(" ")
        print("------------Program Ended-----------")
        print(" ")
        break

    else :
        print(" ")
        print("Invalid Input. Try again")
        continue
