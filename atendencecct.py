total_classes = int(input("Enter total classes: "))
attended_classes = int(input("Enter attended classes: "))

percentage = (attended_classes / total_classes) * 100

if percentage >= 75:
    print(f"Eligible to appear for exam ({percentage:.2f}%)")
else:
    print(f"Not eligible for exam ({percentage:.2f}%)")
