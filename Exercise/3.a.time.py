hour = int(input("Hour :"))
min = int(input("Minutes :"))
sec = int(input("Seconds :"))

if(hour > 0 and hour < 12 and min <= 59 and sec <= 59):
    print("GOOD MORNING SIR")
elif(hour > 13 and hour < 18 and min <= 59 and sec <= 59):
    print("GOOD EVENING SIR")
elif(hour >19 and hour < 23 and min <= 59 and sec <= 59):
    print("GOOD NIGHT SIR")
else :
    print("NOT A VALID TIME")