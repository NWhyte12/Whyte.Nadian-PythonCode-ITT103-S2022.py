# Author: Nadian Whyte
# Date Created: April 26, 2022
# Course: ITT103
# Purpose: The purpose of this program is to calculate the commission received by a salesperson. This is determined by the amount of sales and the class to which a salesperson belongs.

shouldTerminate = ""

while 1 == 1:
    SalespersonNum = input("Enter sales person number: ")
    SalesAmt = int(input("Enter sales amount: "))
    class_ = int(input("Enter class: "))
    commission = 0

    if class_ == 1 and SalesAmt <= 1000:
      commission = SalesAmt * 0.06 
                                             
    elif class_ == 1 and SalesAmt > 1000 and SalesAmt < 2000:
      commission = SalesAmt * 0.07 
                                                             
    elif class_ == 1 and SalesAmt >= 2000:
      commission = SalesAmt * 0.10 
            
    #Calculating the commission for class_ 2
    elif class_ == 2 and SalesAmt < 1000:
      commission = SalesAmt * 0.04
                                           
    elif class_ == 2 and SalesAmt >= 1000:
      commission = SalesAmt * 0.06 
            
    #Calculating the commission for class_ 3
    elif class_ == 3:
      commission = SalesAmt * 0.045 
      
    else:
      print("Sorry, you are not eligible for commissions")
    print("The commission for Salesperson is", commission)

    shouldTerminate = input("Would you like to terminate the process (yes/no) ? ")

    if shouldTerminate == "yes":
        print("Process Terminated")
        break
