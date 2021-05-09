"""
Structured English
This program has four useful functions that a user can use.
The first function ask the user to input a number to calculate to celsius 
We ask the user for the number, then take the number and insert to the formula
Then print out the result and concatenate with text.

The second function estimates the time of arrival entered by the user.
Ask the user for the distance travelled and store it in a value 
Then ask the user for the speed and store the number in a variable.
Then take distance and divide it by speed * 60 to calculate the formula
Print time arrived in minutes.

The third function sorts the numbers entered the user from least to greatest
Create an empty list to store the numbers entered by the user
Create a loop that only takes four values from the user.
Continues to ask user until four values are entered
Print the list of numbers sorted from least to greatest

The fourth function prints get the greatest common factor of two numbers
Ask the user for the first number and store the input 
Ask the user for the second number and store the input
Create a while loop that takes the first number and use modulo on the second number 
Print the greatest common number between the two numbers.

Last function called main invokes all the functions

"""

"""
pseudocode
# fahrenheit_calculator()
Far_num = input()
Result = far_num - 32 / 1.8
print(far_num)

# eta()
Distance = input()
Speed = input()
Time = distance / speed * 60
print(time)

#list_of_numbers()
List[]
I = 0
While i <=3
Iterate i 
Append input()
print(list)

#greatest factor()
First_num = input()
Second_num = input()
While second_num != 0
Hold = second_num
Second_num = first_num % second_num
First_num = hold
print(first_num)

main()

"""


#Converts farenheit to celcius.
def farenheit_calculator(far_num):
    far_num = input("Enter the farenheit you want to convert: ")
    result = (int(far_num) - 32) / 1.8
    print(far_num, "degrees converted to celcius is: ",result)
 

#Calculates the estimated time of arrival by user entering speed and time.
def eta():
    distance = int(input("Enter the distance you are traveling: "))
    speed = int(input("Enter your speed: "))
    time = distance/speed * 60
    print("You will arrive in" , time , "minutes.")
 

 #Sorts numbers entered by user.
def list_of_numbers():
    char = []
    i = 0
    while i <= 3:
        i += 1
        char.append(input("Enter the numbers you want to sort: "))
     
    print(sorted(char))
    
   
    
 #Gets the greatest common factor of two numbers imputed by user.
def greatest_factor():
    first_num = int(input("Enter the first value: "))
    second_num = int(input("Enter the second value: "))
    while second_num != 0:
        hold = second_num
        second_num = first_num % second_num
        first_num = hold
        print("Greatest common divisor is: ", first_num)


def main():
    farenheit_calculator(5)
    eta()
    list_of_numbers()
    greatest_factor()

main()    
