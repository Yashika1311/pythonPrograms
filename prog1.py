#To count no of vowels in given string considering uppercase and lower case

# vowel = ["A","E","I","O","U"]

# a = input("Enter the word : ").upper()

# count = 0

# for i in a:
#     if a.upper() in vowel:
#         count+=1
    
# print(count)

a = input("Enter a word: ").upper()

count = 0

vowels = set("AEIOU")

for char in a:
    if char in vowels:
        count += 1

print("Number of vowels: ", count)

