"""
name = []
name = input("Enter your name")
index = 0
while name != "" and index < len(name):
    print(name[index])
    index += 1
    # index = index + 1



name = input("Enter your name: ")
for character in name:
    print(character)


number = list(range(1, 5))
print(number)




for number in range (1, 5, 2):
    print(number)



for greet in range(3):
    print("Good morning! You are cool!")




def greet (times):
    for i in range(times):
        print("I am super!" + str(i+1)+ " times")

greet(3)
greet(4)




def greet (name, times):
    for i in range(times):
        print(name + " " + "You are super!" + str(i+1)+ " " + " times")

greet("chau", 2)


def groccery(items):
    for item in items:
        print("- " + item)

shopping_list = ["cheese", "pasta", "fish"]
groccery(shopping_list)
shopping_list.append("ice cream")
groccery(shopping_list)





def calculation (a, b):
    addition = a + b
    return addition

num1 = int(input("Give me the 1st number: "))
num2 = int(input("Give me the 2st number: "))
addition = calculation(num1, num2)
print("The sum of the numbers is:", addition)





"""
rows = int(input("Enter number of rows (max 15): "))
def spruce_printing (rows)
    print("Happy holidays!")
    i = 1
    while i <= rows:
        space = rows - i
        symbol = 2 * i - 1
        print(" " * empty)
