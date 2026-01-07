# Banking Application

# Deposit
# Withdrawn
# BalanceCheck
# UserExit

pin = 1425
Userpin=int(input("Enter Your Pin: "))
if pin ==Userpin:
    print("Pin Verified🏧")
    print('*'*60)
    print(" Welcome To Aryan Python Bank!")
    print("*"*60)
    
    print("""
    1.Deposit:
    2.Withdrawn:
    3.BalanceCheck:
    4.Exit:      
        """)
    
    print("-"*60)
    Balance = 10000

    Choice = int(input(("Enter Your Choice: ")))
    if Choice==1:
        Deposit =float(input("Enter Your Deposited: "))
        print("^"*60)
        if Deposit>0:
            Balance+=Deposit
            print("Rs",Deposit,"Amount Has Been Successfully Creadited, Balance Is Rs ",Balance)
            
        else:
            print("Invalid Amount")
            
    elif Choice ==2:
        
        Withdrawn =float(input("Enter Your Withdrawn Amount: "))
        if Withdrawn>0:
            
            if Withdrawn<=Balance:
                Balance -= Withdrawn
                print("Rs",Withdrawn,"Amount Had Been  Debited Successfully, New Balance Rs ",Balance)
                # print('^'*60)
            else:
                print("Insufficient Balance")
                
        else:
            print("Invalid Amount")
                
    elif Choice ==3:
        print("Your Balance Is Rs ",Balance)
        
    elif Choice ==4:
        print("!!! ThankYou For Using Our Application!!!")
        
    else:
         print("Invalid Chioce")
         
else:
    print("Incorrect Pin ❌")
    print("Please Try Again")
    
print("\n")
print("💖 Have A Nice Day 💖")

print("\n")
# print("*"*60)
# print(" Developed By Aryan Sapsod")