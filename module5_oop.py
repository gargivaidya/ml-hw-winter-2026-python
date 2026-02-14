"""
Module 5 
Author : Gargi Vaidya
The program asks the user for input N (positive integer) and reads it

Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputted it before.

The basic functionality of data processing (data initialization, data insertion, data search) should be done via Object-Oriented Programming Paradigm (i.e. using Classes) if the user inputed it before.
"""

class DataSet:
    def __init__(self):
        self.numbers = []

    def insert_number(self, num):
        self.numbers.append(num)

    def search_x(self, x):
        try:
            return self.numbers.index(x) + 1
        except ValueError:
            return -1

def main():
    data0 = DataSet()

    try:
        N = int(input("Enter the number of elements (N): "))
        if N <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    for i in range(N):
        while True:
            try:
                number = int(input(f"Enter number {i+1}: "))
                data0.insert_number(number)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    try:
        X = int(input("Enter the number to search for (X): "))
        result = data0.search_x(X)
        print(result)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()