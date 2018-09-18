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
for i in range(1,number+1):
    print(" " * (number+1),"*" * (number-1+i))
