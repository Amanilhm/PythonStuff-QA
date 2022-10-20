marks = float(input("Please insert the marks: "))

if marks >= 70:
    print("Distinction")
elif  60 <= marks < 70:
    print("Merit")
elif  50 <= marks < 60:
    print("Pass")
else:
    print("Fail")
