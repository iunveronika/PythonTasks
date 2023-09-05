"""
myList = [5,6,7]
print(myList)
print(myList[0])
myList[2] = "Software 1"
print(myList)

myList.append(8)
print(myList)
myList.remove(myList[2])
print(myList)



grade = ["A", "B", "C", "D", "See you later"]

score = int(input("What is your score (0-100)?"))
if 90<= score <=100:
    print(f"Your grade is {grade[0]}")
elif 80<= score <=89:
    print(f"Your grade is {grade[1]}")
elif 70<= score <=79:
    print(f"Your grade is {grade[2]}")
elif 60 <= score <= 69:
    print(f"Your grade is {grade[3]}")
elif 0<= score <=59:
    print(grade[4])
elif  score<0 or score>100:
    print("Invalid score")



mylist = [1, "rainbow"]
print(mylist)
newline = input("Enter the new list unit ")
line_no = 0
while newline != "-1":
    mylist.append(newline)
    line_no += 1
    newline = input("Enter the new list unit ")
print(mylist)

"""

shop = []
while True:
    product = input("Enter the product, done to finish the list: ")
    if product == "done":
        break
    shop.append(product)
print("\nShopping list: ")
for index, item in enumerate(shop, start=1):
    print(f"{index}. {item}")









