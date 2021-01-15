from cs50 import get_string


text = get_string("text: ")
letters = 0
words = 1
sentences = 0
for char in text:
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        letters += 1 
    elif char == " ":
        words += 1
    elif char == "." or char == "?" or char == "!":
        sentences += 1
L = (float(letters / words)) * 100
S = (float(sentences / words)) * 100
     
index = 0.0588 * L - 0.296 * S - 15.8   
if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {round(index)}")