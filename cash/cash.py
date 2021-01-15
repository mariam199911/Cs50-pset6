from cs50 import get_float


def main():
    while True:
     n = 0
     cents = 0 
     
     
     dollars = get_float("Change owed: ")
     if dollars > 0:
        cents = round(dollars * 100)
        while cents > 24:
            cents = cents - 25
            n += 1 
        while cents > 9:
            cents = cents - 10
            n += 1
        while cents >= 5:
            cents = cents - 5
            n += 1
        while cents > 0:
            cents = cents - 1
            n += 1
        print(n)
        break
    
    
if __name__ == "__main__":
    main()