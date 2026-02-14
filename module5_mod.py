"""
Module 5 
Author : Gargi Vaidya
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