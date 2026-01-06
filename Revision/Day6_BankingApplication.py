# Banking Application

# Deposit
# Withdrawn
# BalanceCheck
# UserExit
pin = 1425
Userpin=int(input("Enter Your Pin: "))
if pin ==Userpin:
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
    print("Wrong Pin")
    

            
            
    
    
            
    
