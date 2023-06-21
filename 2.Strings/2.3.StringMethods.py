# strings are immutable means we cannot change a string

# upper() is used to convert the string in UPPERCASES
a = "sahil sahil sahil"
print("uppercase format of a is :",a.upper()) 
print("\n")

# lower() is used to convert the string in LOWERCASES
print("lowecase format of a is :",a.lower()) 
print("\n")

# rstrip() is used to eliminate the following trailing characters
b = "!!! sahil !!!!!!!!!"
print("b without the following trailing charcaters is :",b.rstrip("!"))
print("\n")

# replace() is used to change all occurances of a string with another string
print("after replacing sahil with hero we get :", a.replace("sahil","hero"))
print("\n")

# split(" ") is used to convert the provided string in list whre the string must contain space
print("when b is splitted then it will look as :",b.split(" "))
print("\n")

# capitalize() is used to turn only the first letter of string into uppercase and others into lowercase
name = "sahil Kumar"
print("capitalizing name we get :",name.capitalize()) #lowercase s of sahil will turn into S and the uppercase K of Kumar will turn into k
print("\n")

#center () is used to move the string into center 
print("when name is aligned center then it will look as :",name.center(50))
print(len(name))
print(len(name.center(50))) #length of name is 11 such that pyhton puts 39 spaces before the string so that it will be aligned in middle
print("\n")

# count()is used to count the number of characters or words in a string
name1 = "abracadabra"
name2 = " sahil is a good boy . sahil is intelligent . sahil is hero"
print("No. of a in name1 is :",name1.count("a"))
print("no. of sahil in name1 is :",name2.count("sahil"))
print("\n")

# endswith() provides boolean data type where we can check whether a string is ends with a given value. true if yes and false if no
name = "sahil is a hero !!!"
print("name string ends with !!! :",name.endswith("!!!"))
print("name string ends with hero :",name.endswith("hero"))

print(name.endswith("hero",4,15)) #it is also used to check value in between the string by providing start and end index positions
print("\n")

# startswith() returns true if the string starts with the given value , otherwise false
name = "sahil is a hero !!!"
print("name string starts with sahil :",name.startswith("sahil"))
print("name string starts with hero :",name.startswith("hero"))
print("\n")

# find() method searches for the first occurance of given value and return the index of the given value and if it is not present it will return -1
name = ("He's name is sahil kumar and sahil is a good hero")
print("the index of first occurance of \"is \" is :",name.find("is"))
print("the index of first occurance of \"is \" is :",name.find("ishh"))
print("\n")

# index() is same as find() , there is only one difference that if the given value is not present it will return a error "ValueError: substring not found"
name = ("He's name is sahil kumar and sahil is a good hero")
print("the index of first occurance of \"is \" is :",name.index("is"))
# print("the index of first occurance of \"is \" is :",name.index("ishh"))
print("\n")

# isalnum() will return true if the string contains a-z A-z 0-9 , otherwise false
name = "SahilFavoriteNumberIs28" #spaces are also considered as other characters
print("the given string is alphanumeric or not :",name.isalnum())

name = "Sahil Favorite Number Is 28"
print("the given string is alphanumeric or not :",name.isalnum())
print("\n")

# isalpha() will return true if the string contains a-z A-Z , otherwise false even in case of 0-9
name = "SahilFavoriteNumberIs"
print("the given string is alphanumeric or not :",name.isalpha())

name = "SahilFavoriteNumberIs28"
print("the given string is alphanumeric or not :",name.isalpha())
print("\n")

#islower() returns true if all the letters in the string is in lower case , otherwise false
name = "sahil"
print("is all letters in name is in lower case :",name.islower())

name = "Sahil"
print("is all letters in name is in lower case :",name.islower())
print("\n")

#isupper() returns true if all the letter in the given string is in uppercase , otherwise false
name = "SAHIL KUMAR HERO"
print("is all the cases in the string is in uppercase :",name.isupper())

name = "sahil kumar HERO"
print("is all the cases in the string is in uppercase :",name.isupper())
print("\n")

#isprintable() returns true if the string is printable , otherwise false
name = "sahil is a good boy"
print("is the string printable :",name.isprintable())

name = "sahil is a good boy \n"
print("is the string printable :",name.isprintable())
print("\n")

# isspace() method returns true if string only contains white spaces , otherwise false
name = "   " #by spacebar
print("name consists white spaces :",name.isspace())

name = "        " # by tab button
print("name cosists white spacesn :",name.isspace())

name = "sahil is hero"
print("name cosists white spacesn :",name.isspace())
print("\n")

# istitle() method returns true is first letter of each word in string is uppercase , otherwise false
name = "Sahil Is Hero"
print("each first letter of string is capital or not:",name.istitle())

name = "sahil Is hero"
print("each first letter of string is capital or not:",name.istitle())
print("\n")

#swapcase() converts uppercase into lowercase and lowercase into uppercase
name = "Sahil Is Hero"
print("before swapping :",name)
print("after swapping :",name.swapcase())

# title() converts first letter of each word into uppercase and the other into lowercase
name = "sahil iS hero"
print("using title method :",name.title())