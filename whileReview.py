# while loops allow you to repeat code until a condition is met
# while loops are defined with the while keyword
# while loops are used when you dont know how mnay times you need to repeat the code


# studentList = ["Citlali", "Praise", "Aaron", "Fiona", "Xavier"]
# studentName = 0
# while studentName < len(studentList):
#     print(studentList[studentName])
#     studentName += 1

# fruitList = ["apple", "banana", "cherry", "date", "elderberry" ]

#for loop to print the fruitList
#for loop is when you know how many times
#you need to repeat the code
# for fruit in fruitList:
#     print(fruit + "is a fruit.")

studentList = ["Citlali", "Praise", "Aaron", "Fiona", "Xavier"]

for student in studentList:
    ask = input("What is your last name? ")
    print(student + " " + ask)
