#  Banking Project

#  Project Using Elif And Nested If-Else Statements

# Student Age

#  Student College Admisssion Process

age = int(input("Enter Your Age: "))
if age>=18 and age<=25:
    print("You Are Eligible For Addmission")
    
    Percentage=int(input("Enter Your Percentage: "))
    if Percentage>=70:
        print("You need to pay 7 Lakh ")
        
    elif Percentage>=80:
        print("Your Addmission IS Successful")
        
    elif Percentage>60 and Percentage<70:
        print("You Need to Pay 7 Lakh + Additional Charges")
        
    elif Percentage>00 and Percentage<60:
        print("Not Eligible Due To Inefficient Percentage")
        
    else:
        print("You Are Not Eligible For Addmission!")
        
else:
    print("You Are Not Eligible For Addition Due To  Age!")
        

     