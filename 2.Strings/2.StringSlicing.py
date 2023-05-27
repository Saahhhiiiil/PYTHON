name="sahil,kumar"
print("length of name is :",len(name)) #len() function is used to get the length of a  string

print(name[0:5]) #here if we want to print sahil only then the required characters will be 5 but the indexing will start from 0

#if we want to print only 3 characters of sahil then

print("the first 3 characters of sahil is :" ,name[0:3])

#if we want to print 2nd to 4th character of sahil then

print("2nd to 4th character of sahil is :",name[1:4])

#if we don't put the initial indexing value then python will automatically consider it as 0

print("length of sahil is :",name[:5])

#if we dont set the limit of the character required then python will print the value of variable

print("length of name variable is :",name[:])

#when negative value of n is given then python will automatically subtract it the len()of variable

print(name[0:-3])
print(name[0:len(name)-3])

#when the indexing is  initialised with negative then python will again subtract it with len() of the variable and start the index from that particilar no.

print(name[-5:-2])
print(name[len(name)-5 : len(name)-2])