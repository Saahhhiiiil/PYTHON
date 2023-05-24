a = 1
b = 2

print("sum of a and b is :",a+b) #will print 3 because a and b are valid integer

#EXPLICIT CONVERSION - typecasting done by user 

c = "1"
d = "2"

print("string value sum of c and is :",c+d) #will print 12 and not 3 because according to python c and d are string value and not a integer

print("sum of c and d is :",int(c)+int(d)) #will print 3 because c and d are specified as INTEGERS

e = "1 sahil"
f = "2"

# print(int(e) + int(f)) #will create an ERROR as e is NOT A VALID integer


#IMPLICIT CONVERSION - typecasting done by python itself

g = 1
h = 2.1

print("sum of g and h is :",g+h) #python will automatically provide us float value

#implicit conversion example

i = 1
print("type of i is : ",type(i))

j = 1.2
print("type of j is : ",type(j))

k = i + j 
print("type of k is : ",type(k))