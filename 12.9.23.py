"""
students = []
students.append(("Amir", (20,30,40,90,100)))
students.append(("Timo", (20,30,80,90,100)))
students.append(("Outi", (80,30,40,100,98)))
found = False
print (students)
for student in students:
    if student[0]=="Amir":
        print(f"The name: {student[0]}")
        print(f"The grades: {student[1]}")
        avg = sum(student[1])/len(student[1])
        print(f"The average of the {student[0]}, is {avg}")
        found = True
        break
    if not found:
        print("Sorry wrong name")
students.append(("David", (45,90,38.98,8)))
"""

myList = []
while True:
item = input("Enter items to add to the shopping list (enter 'done' when finished):\n")
if item.lower() == 'done':
break
# Append the item to the shopping list
myList.append(item)
# Display the contents of the shopping list
print("\nYour shopping list:")
for index, item in enumerate(myList, start=1):
print(f"{index}. {item}")
# Ask the user to enter an item to remove
remove_item = input("\nEnter an item to remove from the list: ")
# Attempt to remove the item, handling if it's not in the list
if remove_item in myList:
myList.remove(remove_item)
print("\nUpdated shopping list:")
for index, item in enumerate(myList, start=1):
print(f"{index}. {item}")
else:
print(f"\n'{remove_item}' is not in the shopping list.")
# Display the total number of items in the shopping list
total_items = len(myList)
print(f"\nTotal number of items in the shopping list: {total_items}")




