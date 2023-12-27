#convert camel case string to snake case

#sentence = input("Enter a sentence: ")
# def camel_case_split(str):
#     words = [[str[0]]]
 
#     for c in str[1:]:
#         if words[-1][-1].islower() and c.isupper():
#             words.append(list(c))
#         else:
#             words[-1].append(c)
 
#     return [''.join(word) for word in words]
     
# str = "helloWorld"
# print(camel_case_split(str))
# camelcase = input("Enter a camel case string: ")

# snakecase = ''
# for char in camelcase:
#     if char.isupper():
#         snakecase += '_' + char.lower()
#     else:
#         snakecase += char

# snakecase = snakecase.lstrip('_')

# print("Snake case:", snakecase)

import string
str1 = input("Enter string: ")
str2 = ""

index = 0
for i in str1:
    if i.isupper():
        str2 = str1[:index] + "_" + str1[index:].lower()
    index+=1
    
print(str2)
