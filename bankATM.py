def bank():

      balance = 200
      limiter = "Done"
      limit = ""
      limitcount=0
      limitmax = 2
      limitreach=False
      while limit!=limiter and not (limit):
         if limitcount < limitmax:
           print("Your balance is sufficient for withdraw")
           amount=int(input("Amount to withdraw: "))
           if amount != 00:
             newbalance=balance-amount
             print("Your new balance is: ")
             print(newbalance)
             print("Thanks for using MeBank.Press 00 if you have no other withdrawal to make")
             limitcount += 1
           else:
                print("Exiting........")
                exit()
              
         else:
             limitreach = True
             print("Daily withdraw limit reached,Thank you for banking with us")
             exit()
      else:
         print("Our bank,our society")
      
      
         print("Done")
      
bank()

