print("DISCLAIMER:INVALID FOR MUSCLE BUILDERS , LONG DISTANCE ATHELETS , PREGNANT WOMEN , ELDERLY PEOPLE AND YOUNG CHILDREN")
a=float(input("WEIGHT IN KILOGRAMS:"))
b=float(input("HEIGHT IN CENTIMETERS:"))
c=str(input("GENDER(MALE OR FEMALE):"))
d=int(input("ENTER AGE:"))
BMI=a/(b/100)**2
if(d>20):
    if(c=="MALE" or "FEMALE"):
        print("BMI=",BMI)
        if(BMI<18.5):
            print("Oops!You are UNDERWEIGHT....Take care of your health")
        elif(BMI<=24.9):
            print("Awesome!You are NORMAL")
        elif(BMI<=29.9):
            print("Oh No!You are overweight")
        elif(BMI>=30.0):
            print("Oops!You are OBESE")
        RecentBMI=float(input("Enter your Recent BMI:"))
        if(RecentBMI>BMI):
            print("YOUR BMI HAS INCREASED")
        elif(RecentBMI==BMI):
            print("YOUR BMI IS SAME AS RECENT BMI")
        else:
            print("YOUR BMI HAS DECREASED")
if(d<20):
    BMI=a/(b/100)**2
    m=BMI/100
    print("BMI=",m,"%")
    if(m<5/100):
        print("Oops!The little one is UNDERWEIGHT")
    elif(m<85/100):
        print("Awesome!The little one is NORMAL")
    elif(m<95/100):
        print("Oh No!The little one is OVERWEIGHT")
    elif(m>95/100):
        print("Oops!The little one is OBESE")
    RecentBMI=float(input("Enter your Recent BMI:"))
    if(RecentBMI<m):
        print("YOUR BMI HAS INCREASED NOW")
    elif(RecentBMI==m):
        print("YOUR BMI IS SAME AS RECENT BMI")
    else:
        print("YOUR BMI HAS DECREASED NOW")

        
