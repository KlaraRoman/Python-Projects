distance=int(input("Enter the distance of your destination(kms): "))
choice=str(input("Are you a regular [1] or a discounted [0] passenger? "))
if choice=='1':
    print("Regular")
elif choice=='0':
    print("Discounted")
else:
    print("Invalid. Only put 1 or 0.")


if 1<=distance<=4 and choice=='1':
    fee='8.00'
elif 1<=distance<=4 and choice=='0':
    fee='7.00'
elif 5<=distance<=10 and choice=='1':
    fee='9.50'
elif 5<=distance<=10 and choice=='0':
    fee='8.00'
elif 11<=distance<=15 and choice=='1':
    fee='11.00'
elif 11<=distance<=15 and choice=='0':
    fee='9.00'
elif 16<=distance<=20 and choice=='1':
    fee='12.00'
else:
    fee='10.00'
    



print("For",distance,",",choice,",you need to pay",fee)

amount=int(input("Enter amount paid: "))
if amount<=fee:
    print("Insufficient.")
elif amount>=fee:
    change=amount-fee
    print("Please get your change: ")
else:
    print("\n")


print("Thank you for riding with us.")

 
