#Write a program to print all 24 hours of the day with appropriate suffixes such as AM, PM, Noon, and Midnight.

for i in range(1, 12):
    print(i, 'AM')
print(12, 'Noon')
for i in range(1,12):
    print(i, 'PM')
print(12, 'Midnight')
