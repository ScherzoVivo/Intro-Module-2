#==================================================#
# Basic Math Script -- basicmath.py --
# C:\Users\Alleg\Python\UW Course\Week 2\basicmath.py
# Assignment #2 - Perform basic math functions
# DJP -- 2021-07-14 -- Initial script composition
#==================================================#
# "Title"
print("\n\n=====================")
print("==Basic Math Solver==")
print("=====================\n")
####################
# Input and processing
first = float(input("Please enter a number || "))
second = float(input("\nPlease enter a second number || "))

sum     = round(first + second, 2)
diff    = round(first - second, 2)
product = round(first * second, 2)
quot    = round(first / second, 2)

floorDv = int(first // second)
remain  = round(first % second, 2)
####################
# Output to screen
print("==========================================\n")
print("(Numbers are rounded to two decimal places.)\n")
print(f"The sum of {first} and {second} is || {sum} ||.\n")
print(f"The difference between {first} and {second} is || {diff} ||.\n")
print(f"The product of {first} and {second} is || {product} ||.\n")
print(f"The quotient of {first} and {second} is || {quot} ||.")
print(f"(Or {floorDv} with a remainder of {remain}!)")

# basicmath.py
