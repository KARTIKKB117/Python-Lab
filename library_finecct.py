days = int (input ("enter days :"))
if days <=5:
    fine = days*2
    
elif days >= 10:
    fine = days*5
    
else:
    fine = days*10
    
print(f"fine is {fine}")