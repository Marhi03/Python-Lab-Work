#Write a program that accepts two strings from the user, concatenates them, 
#and then repeats the concatenated string n times, where n is entered by the user.

s1 = input('Enter a string: ')
s2 = input('Enter another string: ')
s3=' '
s = s1 + s3 + s2 +s3
n = int(input('How many times do you want to repeat the string?: '))
print(s*n)
