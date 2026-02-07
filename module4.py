"""
Module 4 
Author : Gargi Vaidya
The program asks the user for input N (positive integer) and reads it
Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.
"""
while True:
    N = int(input("Enter N (positive integer): "))
    numbers = []
    if N > 0:
        for i in range(N):
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
        X = int(input("Enter X (integer): "))
        if X in numbers:
            print(numbers.index(X) + 1)
            break
        else:
            print(-1)
            break
    else:
        print("Invalid Input")

