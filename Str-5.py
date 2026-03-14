#Given the string s = "PDEU College", write a program to extract the following:
#"PDEU", "College", "U Col", The complete string in reverse order

s = 'PDEU College'
print(s[0:4])
print(s[5:])
print(s[3:8])
print(s[::-1])
