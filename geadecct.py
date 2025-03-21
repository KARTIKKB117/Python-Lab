m1 = float(input("Enter the m1 :"))
m2 = float(input("Enter the m2 :"))
m3 = float(input("Enter the m3 :"))

marks = (m1+m2+m3)/3

if marks >=90:
    grade = "A"
    
elif (marks >= 75):
    grade = "B"
    
elif (marks >= 60):
    grade = "C"

else:
    grade = "D"
    
print(f"your grade is {grade}")