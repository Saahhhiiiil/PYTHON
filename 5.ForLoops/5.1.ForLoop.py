#for loop printing character of a string
print("PROGRAM 1 : characters of a string")
name  = "sahil"

for char in name :
    print(char)
print("\n")

#for loop in list 
print("PROGRAM 2 : words present in a list")
colors = ["red" , "green" , "white" , "blue" , "black"] #this is a list

for col in colors :
    print(col)
print("\n")
 
#nested for loop
print("PROGRAM 3 : conditional statements and nested for loop")
colors = ["red" , "green" , "white" , "blue" , "black"] #this is a list

for col in colors :
    print(col)
    if col == "white":  #coditional statements can alose be used in a for loop
        print("This is White")
    for char in col:   #this shows nested loop
        print(char)
print("\n")

#printing numbers 
print("PROGRAM 4 : PRINTING NUMBERS")
for k in range(5) :  #range() function is used to print a loop of numbers 
    print(k)
    print("\n")
for k in range (5) :
    print(k + 1)
print("\n")

#setting range  between numbers 
print("PROGRAM 5 : RANGE FOR TWO NUMBERS")
for k in range (1 , 100) :
    print(k)
print("\n")
print("PROGRAM 5 : RANGE FOR TWO NUMBERS")
for k in range (1 , 100) :
    print(k+1)
print("\n")

#use of 3 numbers in range function
print("PROGRAM 6 : USE OF 3 PARAMETER IN RANGE FUNCTION")
for i in range(1 , 10 , 2) : #the third paramter in the range function is the step function in which the first number skips the times the third number is
    print(i)