# PRINT ALL LETTERS FROM STRING1 THAT ALSO APPEARS IN STRING2 BUT IT SHOULD BE USING (IN) OPERATOR

str1 = 'Yashika'
str2 = 'Sakshi'


common_letters = [letter for letter in str1 if letter in str2]

print("Common letters:", common_letters)