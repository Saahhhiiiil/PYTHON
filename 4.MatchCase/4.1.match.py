x = int(input("Enter value of x: "))

match x :
    # when input number is 0
    case 0 :
        print("Number is 0")
    case 1 : 
        print("Number is 1")
    case 2 :
        print("Number is 2")
    case 3 :
        print("Number is 3")
    case 4 :
        print("Number is 4")
    case 5 :
        print("Number is 5")
    case _ :
        print(x)