# Name: Miranda Towne
# Description: Program to iterate the numbers from 1 to 100 


# Print Fizz for multiples of 3
for num in range(1, 101):
    #  Print FizzBuzz for multiples of 15.
    if num % 15 is 0:
        print("FizzBuzz")
        # Print Fizz for multiples of 3.
    elif num % 3 is 0:
        print("Fizz")
        # For numbers which are multiples of 5 print Buzz.
    elif num % 5 is 0:
        print("Buzz")
        # adding in else allows Fizz to be printed in place of the number.
    else:
        print(num)