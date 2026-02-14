"""
Module 5 
Author : Gargi Vaidya
"""

from module5_mod import DataSet

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