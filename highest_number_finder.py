# Define highest_number
def highest_number(num1, num2, num3, num4, num5):
# Make a variable "highest"
    highest = num1  # Assume that the first input number is the highest

# Compare num2 to "highest"
    if num2 > highest:  # If num2 is greater than "highest"
        highest = num2  # Update "highest"
 # If not, do not change "highest"

    # Compare num3 to "highest"
    if num3 > highest:  # If num3 is greater than "highest"
        highest = num3  # Update "highest"
# If not, do not change "highest"

    # Compare num4 to "highest"
    if num4 > highest:  # If num4 is greater than "highest"
        highest = num4  # Update "highest"
 # If not, do not change "highest"

    # Compare num5 to "highest"
    if num5 > highest:  # If num5 is greater than "highest"
        highest = num5  # Update "highest"
 # If not, do not change "highest"

    return highest  # Return the highest number


# Ask the user to input five numbers
num1 = int(input("Please input the 1st number: ")) 
num2 = int(input("Please input the 2nd number: "))  
num3 = int(input("Please input the 3rd number: "))   
num4 = int(input("Please input the 4th number: ")) 
num5 = int(input("Please input the 5th number: ")) 

# Store the value returned in the variable "result"
result = highest_number(num1, num2, num3, num4, num5)

# Print the result
print("The highest number is:", result)
