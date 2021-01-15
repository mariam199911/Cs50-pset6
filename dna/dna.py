import csv
from sys import argv
import sys 


max_len = 0
STR = []
arr = []


def get_max_ans(m, sub):
    ans = [0] * len(m)
    for i in range(len(m) - len(sub), -1, -1):
        if m[i:i + len(sub)] == sub:
            if i + len(sub) > len(m) - 1:
                ans[i] = 1
            else:
                ans[i] = 1 + ans[i + len(sub)]
    return max(ans)
        
        
def main():
    with open(sys.argv[1], "r") as csvfile:
        read = csv.reader(csvfile)
        STR = next(read)[1:]
        text_path = argv[2]
        with open(text_path) as text_file:
            m = text_file.read()
            arr = [get_max_ans(m, sub) for sub in STR]
###################################################################################
            for line in read:
                name = line[0]
                values = [int(val) for val in line[1:]]
                if arr == values:
                    print(name)
                    exit(0)
            print("no match") 
            
            
if __name__ == "__main__":
    main()            