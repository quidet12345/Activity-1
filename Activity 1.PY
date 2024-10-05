number = int(input("Enter Number : "))
mynumbers = []

for i in range(number):
    number = input("Enter Number")
    mynumbers.append(number)


    if number > "0":
        print("positive")

    if number < "0":
        print("negative")