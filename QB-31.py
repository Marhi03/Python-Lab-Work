#Write a Python program to convert a temperature from Celsius to Fahrenheit using a
#function.
#Accept a temperature in Celsius from the user.
#Create a function that takes the Celsius value as input.
#Return the Fahrenheit value from the function.
#Display the result.

def temp_conversion(t):
    f=(t*(9/5))+32
    return f
t=int(input('Enter the temperature in celsius: '))
f=temp_conversion(t)
print('Temperature in farenheit is: ', f)
