
# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.
#ask user to input the range of alphabet
alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
inputed_letter= input("Enter the range of letter(ex. A-Z or a-z):")

start, end = inputed_letter.split("-")
start_index= alphabet.index(start)
end_index= alphabet.index(end)+1

#display the result
print(alphabet[start_index:end_index])
