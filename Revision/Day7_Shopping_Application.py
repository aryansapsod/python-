
# print(int(input('Enter Your Choice: ')))1

print("""   
                !!! Welcome To Vaibhav Dryfruit Kirana And Masale !!!
      
      1.Menu
      2.Payment
      3.OrderInfo
      
      """)

if int(input('Enter Your Choice:')) ==1:
    print("""
          Our Menu Is As Follows:
          
          1.Dryfruits
          2.Kirana
          3.Masale
          
          """)
    print("For More Info Contact: 7066050740")
    
elif int(input('Enter Your Choice:')) ==2:
    print("Payment Gateway Is Under Maintenance, Please Try Again Later")
    
elif int(input('Enter Your Choice:')) ==3:
    print("Your Order Is Being Processed, You Will Receive It Soon")   
    
else:
    print("Invalid Choice, Please Try Again")