sentence = input("enter sentence:").lower()
vowels = "a ,e ,i ,o, u"
count = sum(1 for char in sentence if char in vowels )
print (f"number of vowels is {count}")