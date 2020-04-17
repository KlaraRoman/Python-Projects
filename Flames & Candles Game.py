print("Let's play FLAMES & CANDLES!",end="\n\n")

while True:

    #FLAMES
    boy=str(input("Enter a male's name: ")).upper()
    girl=str(input("Enter a female's name: ")).upper()
    
    new_word=""

    print("\n")
     
    for i in boy:
        if i in list(girl) and i.isalnum():
            new_word += i
            continue

    FLAMES=["F - Friends","L - Lovers","A - Acquaintances","M - Marriage","E - Enemy","S - Sweetheart"]
    boylen=len(new_word)

    print("Male Count: ",boylen)

    if boylen%6==0:
        print("Male result: ",FLAMES[-1])
    elif boylen%6==1:
        print("Male result: ",FLAMES[0])
    elif boylen%6==2:
        print("Male result: ",FLAMES[1])
    elif boylen%6==3:
        print("Male result: ",FLAMES[2])
    elif boylen%6==4:
        print("Male result: ",FLAMES[3])
    elif boylen%6==5:
        print("Male result: ",FLAMES[4])
    else:
        print("Male result: ",FLAMES[5])



    #CANDLES

    new_word2=""
    
    for i in girl:
        if i in list(boy) and i.isalnum():
            new_word2 += i
            continue
            

    CANDLES=["C - Crush","A - Acquaintance","N - Never","D - Darling","L - Live-in","E - Engaged"]
    girllen=len(new_word2)

    print("Female Count: ",girllen)

    if girllen%6==0:
        print("Female result: ",CANDLES[-1])
    elif girllen%6==1:
        print("Female result: ",CANDLES[0])
    elif girllen%6==2:
        print("Female result: ",CANDLES[1])
    elif girllen%6==3:
        print("Female result: ",CANDLES[2])
    elif girllen%6==4:
        print("Female result: ",CANDLES[3])
    elif girllen%6==5:
        print("Female result: ",CANDLES[4])
    else:
        print("Female result: ",CANDLES[5])




    #REMAINING NUMBER

    new_word3=""

    for i in boy+girl:
        if i.isalnum():
            new_word3 +=i
            continue

    y=len(new_word3)

    x=boylen+girllen

    remaining=(y-x)
    print("Remaining Letters Count: ",remaining)


    #FINAL RESULT

    FLAMESCANDLES=["F - Friends","L - Lovers","A - Acquaintances","M - Marriage","E - Enemy","S - Sweetheart","C - Crush","A - Acquaintance","N - Never","D - Darling","L - Live-in","E - Engaged"]

    if remaining%12==0:
        print("Final result: ",FLAMESCANDLES[-1])
    elif remaining%12==1:
        print("Final result: ",FLAMESCANDLES[0])
    elif remaining%12==2:
        print("Final result: ",FLAMESCANDLES[1])
    elif remaining%12==3:
        print("Final result: ",FLAMESCANDLES[2])
    elif remaining%12==4:
        print("Final result: ",FLAMESCANDLES[3])
    elif remaining%12==5:
        print("Final result: ",FLAMESCANDLES[4])
    elif remaining%12==6:
        print("Final result: ",FLAMESCANDLES[5])
    elif remaining%12==7:
        print("Final result: ",FLAMESCANDLES[6])
    elif remaining%12==8:
        print("Final result: ",FLAMESCANDLES[7])
    elif remaining%12==9:
        print("Final result: ",FLAMESCANDLES[8])
    elif remaining%12==10:
        print("Final result: ",FLAMESCANDLES[9])
    elif remaining%12==11:
        print("Final result: ",FLAMESCANDLES[10])
    else:
        print("Final result: ",FLAMESCANDLES[11])


    print("\n")
    
    






    

            
