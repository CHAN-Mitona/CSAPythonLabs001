# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
user = input("Enter anything: ")
for i in user:
    print(i, i, sep = "", end ="")
print("")

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "


# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.


# alphabet = "abcdefghijklmnopqrstuvwxyz"
# start, end = alphabet.split('-')
# user_range = input("Enter a range of letters (e.g., a-z): ")

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# user_range = input("Enter a range of letters (e.g., a-z): ")
# start, end1 = user_range.split("-")
# for i in alphabet:
#     if start == i:
#          print(i)
#          for j in alphabet:
#             if end1 == j:
#                 print(j)

# print(start, end1)
user_range = input("Enter a range of letters (e.g., a-z): ")
start, end1 = user_range.split("-")
convert  = ord(start)
convert2 = ord(end1)
convert3 = convert2 + 1
i = convert
while i < convert3:
    print(chr(i), end="")
    i += 1


# print(convert)
# print(convert2)
# print(chr(convert))
