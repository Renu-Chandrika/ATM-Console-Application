users= { "624335621" : ["user1", 5000,1234],
         "624335622" : ["user2", 500,5678],
         "624335623" : ["user3", 15000,9876],
         "624335624" : ["user4", 1000,1230],
         "624335625" : ["user5", 600,3456]
    }

print("***Welcome to ATM***")
print()

user_acc= input("enter your acc number:")
transaction =[]
if user_acc in users:
    max_attempts = 3
    attempts=1
    active_session= False
    while attempts <= max_attempts:
          user_pin= int(input("Enter your PIN:"))
          if user_pin== users[user_acc][-1]:
              print("Login successful. You can proceed with the transaction")
              active_session= True
              break
          else:
              remaining_attempts = max_attempts - attempts
              print("you have",remaining_attempts,"left")  #or print(f"you have (remaining_attempts) left")

              if remaining_attempts==0:
                  print("account locked")
              else:
                  print("Incorrect pin. you have",remaining_attempts,"attempts")
              attempts+=1
              
    while True and active_session:
        print("Choose any of the options:")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Transaction history")
        print("4.Balance enquiry")
        print("5.Pin change")
        print("6.Exit")

        choice = int(input("enter your choice:"))
        if choice==1:
            amount = int(input("Enter amount you want to deposit:"))
            if amount > 0:
               users[user_acc][1] += amount
               print("Amount deposited")
               transaction.append(f"{amount} deposited")
               print(users[user_acc][1])
            else: 
                print("invalid")
                
        elif choice==2:
              amount = int(input("Enter amount you want to withdraw:"))

              if amount<= users[user_acc][1]:
                  users[user_acc][1] -= amount
                  print("Please collect your cash")
                  transaction.append(f"{amount} withdrawn")
                  print("Balance:",users[user_acc][1])
              else:
                  print("insufficient funds")
        elif choice==3:
              for transactions in transaction:
                  print(transactions)
            
        elif choice==4:
              print("Balance:",users[user_acc][1])
              
        elif choice==5:
              userpin= int(input("Enter your current PIN:"))
              if userpin == users[user_acc][-1]:
                  new_pin = int(input("Please enter your new pin:"))
                  confirm = int(input("Please confirm your pin:"))
                  if new_pin == confirm:
                      users[user_acc][-1] = new_pin
                      print("Pin chnaged")
                  else:
                      print("Pin confirmation unsuccessful")
              else:
                  print("Invalid Pin")
        elif choice==6:
            print()
            print("Thank you.Visit again")
            print()
            break
        else:
            print("Invalid choice")
    
        
else:
    print("Invalid account")



   
