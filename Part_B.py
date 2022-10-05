from sre_compile import isstring


myList = []
while True:
    num = input("Enter a Marks: ")
# try block For capture ValueError
    try:
        if num == "end":
            break
# append the entered number to list if valid
        myList.append(float(num))
        
        if float(num)<0:
             print("Marks must be positive!")
             myList.pop()
           
        if float(num)>100:
             print("That's not a valid mark!")
             myList.pop()
# catches value error and ignores it
    except ValueError as e:  
        print(e)
        continue

print("Total marks: " + str(sum(myList)))
print("Average marks: " + str(sum(myList)/len(myList)))
print("Highest mark: " + str(max(myList)))
print("Lowest mark: " + str(min(myList)))
