
# print(int(input('Enter Your Choice: ')))

print("""   
                !!! Welcome To Vaibhav Dryfruit Kirana And Masale !!!
      
      1.Menu
      2.Payment
      3.OrderInfo
      
      """)

payment_method = (
    """"
        1.UPI
        2.Credit Card
        3.Debit Card
        4.Cash
    """
)

if int(input('Enter Your Choice:')) ==1:
    print("""
          Our Menu Is As Follows:
          
          1.Dryfruits
          2.Kirana
          3.Masale
          
          """)
    print("For More Info Contact: 7066050740")
    
    if int(input("Enter Your Choice: "))==1:
        print("""Dryfruits: 
        1.Almonds
        2.Pistachios
        3.Raisins
        4.Walnuts
        5.Figs
        6.Date Palm
        7.Pomegranate Seeds
        8.Kishmish (Grapes)
        9.Apricot Kernel
        10.Cashew Nuts
        """)
        
        if int(input("Enter Your Choice: "))==1:
            print("Almonds Price Per Kg: 800 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 800
            print("Total Price: ", total, "INR")
            
            # payment_method = input("Enter Payment Method (UPI/Credit Card/Debit Card/Cash): ")  
            # print("You have selected", payment_method, "as your payment method.")
            # Here, you can add further processing based on the payment method if needed.
            
        elif int(input("Enter Your Choice: "))==2:
            print("Pistachios Price Per Kg: 1200 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 1200
            print("Total Price: ", total, "INR")
            
        elif int(input("Enter Your Choice: "))==3:
            print("Raisins Price Per Kg: 600 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 600
            print("Total Price: ", total, "INR")
            
            # payment_method = input("Enter Payment Method (UPI/Credit Card/Debit Card/Cash): ")  
            # print("You have selected", payment_method, "as your payment method.")
            
        elif int(input("Enter Your Choice: "))==4:
            print("Walnuts Price Per Kg: 1500 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 1500
            print("Total Price: ", total, "INR")
            
            # payment_method = input("Enter Payment Method (UPI/Credit Card/Debit Card/Cash): ")  
            # print("You have selected", payment_method, "as your payment method.")
            
        elif int(input("Enter Your Choice: "))==5:
            print("Figs Price Per Kg: 700 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 700
            print("Total Price: ", total, "INR")

            # payment_method = input("Enter Payment Method (UPI/Credit Card/Debit Card/Cash): ")
            # print("You have selected", payment_method, "as your payment method.")
            # Here, you can add further processing based on the payment method if needed.
        # Similarly, you can add more elif blocks for other dryfruits if needed.
        
        elif int(input("Enter Your Choice: "))==3:
            print("Raisins Price Per Kg: 600 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 600
            print("Total Price: ", total, "INR")
            
        elif int(input("Enter Your Choice: "))==4:
            print("Walnuts Price Per Kg: 1500 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 1500
            print("Total Price: ", total, "INR")
            
        elif int(input("Enter Your Choice: "))==5:
            print("Figs Price Per Kg: 700 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 700
            print("Total Price: ", total, "INR")
            
        elif int(input("Enter Your Choice: "))==6:
            print("Date Palm Price Per Kg: 900 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 900
            print("Total Price: ", total, "INR")
            
            
            
        elif int(input("Enter Your Choice: "))==7:
            print("Pomegranate Seeds Price Per Kg: 1100 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 1100
            print("Total Price: ", total, "INR")
            
        elif int(input("Enter Your Choice: "))==8:
            print("Kishmish (Grapes) Price Per Kg: 650 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 650
            print("Total Price: ", total, "INR")
            
        elif int(input("Enter Your Choice: "))==9:
            print("Apricot Kernel Price Per Kg: 1300 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 1300
            print("Total Price: ", total, "INR")
            
        elif int(input("Enter Your Choice: "))==10:
            print("Cashew Nuts Price Per Kg: 1400 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 1400
            print("Total Price: ", total, "INR")

            if payment_method == input("Enter Payment Method : "):  
                print("You have selected", payment_method, "as your payment method.")
                
                

    if int(input("Enter Your Choice: "))==2:
        print("""Kirana:
        1.Sugar
        2.Rice
        3.Oil
        4.Salt
        5.Ginger Powder
        6.Turmeric Powder
        7.Wheat Flour
        8.Lentils
        9.Pulses
        10.Tea Leaves
        """)
        
    elif int(input("Enter Your Choice: "))==3:
        print("Kirana Selected")
        print("Prising Information Unavailable At The Moment")
        

if int(input("Enter Your Choice: "))==3:
        print("""Masale:
        1.Red Chilli Powder
        2.Black Pepper Powder
        3.Cumin Powder
        4.Garam Masala Powder
        5.Coriander Powder
        6.Fenugreek Seeds
        7.Mustard Seeds
        8.Cardamom
        9.Cloves
        10.Nutmeg
        11.Cinnamon
        12.Asafetida
        13.Curry Leaves
        14.Bay Leaves
        15.Saffron
        16.Tamarind
        """)
        
        if int(input("Enter Your Choice: "))==1:
            print("Red Chilli Powder Price Per Kg: 400 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 400
            print("Total Price: ", total, "INR")
            
        elif int(input("Enter Your Choice: "))==2:
            print("Black Pepper Powder Price Per Kg: 900 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 900
            print("Total Price: ", total, "INR")
        
        elif int(input("Enter Your Choice: "))==3:
            print("Cumin Powder Price Per Kg: 500 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 500
            print("Total Price: ", total, "INR")
            
        elif int(input("Enter Your Choice: "))==4:
            print("Garam Masala Powder Price Per Kg: 600 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 600
            print("Total Price: ", total, "INR")
            
        elif int(input("Enter Your Choice: "))==5:
            print("Coriander Powder Price Per Kg: 350 INR")
            print("Enter Quantity in Kgs: ")
            quantity = int(input())
            total = quantity * 350
            print("Total Price: ", total, "INR")
      

else:
    print("Invalid Choice, Please Try Again")
    
    