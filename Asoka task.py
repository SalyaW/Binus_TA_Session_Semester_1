number = int(input("Input Number:"))

for i in range(1,number+1):
    print("*" * i )

number = int(input("Input Number:"))

for i in range(1,number+1):
    print(" " * (number-i),"*" * i)

number = int(input("Input Number:"))

for i in range(1,number+1):
    print("*" * (number-i+1))

number = int(input("Input Number:"))

for i in range(0,number+1):
    print(" "* i,"*"*number)
    number = number-1
#IDK the same side triangles so i googled it
number = int(input("Input Number:"))

for i in range(0,number):
    for o in range(0,number-i):
        print(end=" ")
        print(end=" ")
    for o in range (0,i+1):
        print("*",end=" ")
    for o in range (0,i):
        print ("*",end=" ")
    print("")
print(" ")

number = int(input("Input Number:"))

for i in range(0,number):
    for o in range(0, i+1):
        print(end=" ")
        print(end=" ")
    for o in range(0,number-i):
        print(" ",end="*")
    for o in range(0, number - i-1):
        print(" ",end="*")
    print("")
print("")

number = int(input("Input Number:"))

for i in range(0, number):
    for o in range(0, number - i):
        print(end=" ")
        print(end=" ")
    for o in range(0, i + 1):
        print("*", end=" ")
    for o in range(0, i):
        print("*", end=" ")
    print("")
for i in range(0,number):
    for o in range(1):
        print(" ",end="")
    for o in range(0, i+1):
        print(end=" ")
        print(end=" ")
    for o in range(0,number-i-1):
        print(" ",end="*")
    for o in range(0, number - i-2):
        print(" ",end="*")
    print("")
print("")