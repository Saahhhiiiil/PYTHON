print("Program 1 : string")
name = "sahil" # " "is used to represent value of a string
print(name)
another = 'heroiya' # ' ' is also used to represent value of a string
print(another)
print("\n")

print("Program 2 : using \" ")
print('he said "sahil is a hero" ') #if we want to use " " in a string we can use ' ' to represent string
print("he said 'sahil is a hero' ") #if we want to use ' ' in a string we can use " " to represent a string
print("he said \"sahil is a hero \" ") #we can also use escape sequence character to print " "inside a string
print("he said \'sahil is a hero \' ") #we can also use escape sequence character to print ' ' inside a string
print("\n")

print("Program 3 : combining")
print(name + " kumar")
print("\n")

print("Program 4 :multi line string")
print("""sahil is a good boy
he is a hero
his fav hero is iron man
he is intelligent""")   #"""  """ is used for multi line strings 
print("\n")

print('''sahil is a good boy
he is a hero
his fav hero is iron man
he is intelligent''')   #'''   ''' is used for multi line strings 
print("\n")


print("Program 5 : indexing") #accessing characters of a string
print(name[0]) #indexing of an array always starts with 0
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print("\n")

#print(name[5]) it will generate error

print("program 6 : using for loop to print characters")

for character in name:
    print(character),

name1 ='''sahil is a good boy
he is a hero
his fav hero is iron man
he is intelligent'''

for character in name1:
    print(character),