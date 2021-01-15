from cs50 import get_int
from sys import exit


while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        for i in range(height):
            print(" " * (height-i-1) + "#" * (i+1) + "  "+"#" * (i+1))
        break