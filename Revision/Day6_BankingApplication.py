# Banking Application

# Deposit
# Withdrawn
# BalanceCheck
# UserExit

print(" Welcome To Aryan Python Bank!")

print("""
1.Deposit:
2.Withdrawn:
3.BalanceCheck:
4.Exit:      
      """)

Balance = 10000

Choice = int(input(("Enter Your Choice: ")))

if Choice==1:
    Deposit =float(input("Enter Your Deposited: "))
    if Deposit>0:
        print("Rs",Deposit,"Amount Has Been Successfully Creadited")
        
    else:
        print("Invalid Amount")
        
elif Choice ==2:
    Withdrawn =float(input("Enter Your Withdrawn Amount: "))
    if Withdrawn>0:
        print("Your Amount Is Debited Successfully")
    
