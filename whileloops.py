# name = input("Enter your name: ")

# while name =="":
#     print("You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print ("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("enter a food you like (q to quit): ")

# while not food == "q":
#     print (f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")

# num = int(input("Enter a # between 1 - 10: "))\

# while num < 1 or num > 10:
#     print (f"{num} is not valid")
#     num - int(input("Enter a # between 1 - 10: "))

# print(f"Your number is {num}")

# nums = range(1,10000)

# for num in nums:
#     if num == 3:
#         print('Found!')
#         continue
#     print(num)

#nested for loops
# for num in nums:
#     for letter in 'abc':
#         for letter2 in 'abc':
#             for letter3 in 'abc':
#                 for letter4 in 'abc':
#                     print(num, letter, letter2, letter3, letter4)

# while loop
# when you dont know the number of iterations
# for i in range(10):
#     print(i)

# for i in range(1, 11):
#     print(i)

# x = 0

# while True:
#     if x == 5:
#         break
#     print(x)
#     x += 4  

while True:
    print("Enter your name: ")
    name = input()
    if name == 'your name':
        print("your name is " + name)
        break
    else:
        print("Thank you!")
