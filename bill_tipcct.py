bill= float(input("enter bill amount:"))
tipamt = float(input ("enter tip percentage:"))

tip = (bill*tipamt)/100
total = bill + tip

print (f"the total tip is {tip}")
print (f"the total bill is {total}")