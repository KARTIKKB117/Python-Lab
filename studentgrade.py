name = input("enter name : ")
regno = int(input("reg no :"))
marks1 = float(input("enter the marks:"))
marks2 = float(input("enter the marks:"))
marks3 = float(input("enter the marks :"))

marks = [marks1, marks2, marks3]
avg =sum(marks) / 3
passed =  avg >= 40
Student_record = {"Name":name , "Reg No":regno,"Marks":marks,"Average":avg, "Passed":passed}
print(Student_record)
