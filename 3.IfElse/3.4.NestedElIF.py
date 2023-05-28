num = int(input("Enter number :"))

if(num > 0) :
    if(num <= 10) :
        print("Number is between 1 - 10 ")
    elif(num > 10 and num <= 20) :
        print(" Number is between 11 - 20 ")
    elif(num > 20 and num <= 30) :
        print(" Number is between 21 - 30 ")
    else :
        print("Number is greater than 30")
elif(num == 0) :
    print("Number is Zero")
else :
    print("Number is Negative")