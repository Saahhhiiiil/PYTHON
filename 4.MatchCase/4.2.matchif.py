x = int (input ("Enter value of x :"))

match x :
    case 1 : 
        print("number is 1")
    case 2 :
        print("number is 2")
    case 6 :
        print("number is 6")
    case _ if x > 10 and x < 20 :
        print("number between 10 and 20")
    case _ if x > 20 and x < 30 :
        print("number between 20 and 30")
    case _ if x > 30 and x < 40 :
        print("number between 30 and 40")
    case _ if x == 55 :
        print("Number is 55")
    case _ if x != 60 :
        print("Number is not equal to 60")
    case _ :
        print(x)