balance = 1000

amount = float(input("enter the amount:"))

if balance < amount :
    print ("insufficient balance ")

else:
    balance -= amount 
    print (f"withdrawal succesfull balance is {balance}")
    