password = input ("enter password:")
if len(password )>=8 and any (c.isdigit() for c in password )and any (c.isupper() for c in password )and any(c in "()!@$^*&" for c in password) :
    
    print ("strong password")
    
else :
    print ("weak password use upper case digit and special characters ")
    