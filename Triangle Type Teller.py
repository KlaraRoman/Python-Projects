print("Welcome to our Triangle Type Teller program!\n")

while True:

    a=(input("Enter length of side 1 of triangle: "))
    b=(input("Enter length of side 2 of triangle: "))
    c=(input("Enter length of side 3 of triangle: "))

    print("\n")


    if a==b==c:
        print("This is an EQUILATERAL triangle.")
        
    elif a==b or b==c or a==c:
        print("This is an ISOSCELES traingle.")

    else:
        print("This is a SCALENE triangle.")

    print("\n=== === === === === === ===")   

