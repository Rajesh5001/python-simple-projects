def billing():
    # Inputs of phone number,quantity
    try:
        pno = int(input("Enter your Phone number :"))
        idly, dosa, poori = 5, 10, 15
        idly_q = int(input("How many have You Idly ate:"))
        dosa_q = int(input("How many have You Dosa ate :"))
        poori_q = int(input("How many have You Poori ate :"))
        # Process
        bill = (idly * idly_q) + (dosa * dosa_q) + (poori * poori_q)

        print()
        # outputs
        print("--------------Welcome To Dhamotharan Bhavan Hotel----------------------")
        print("Phone Number :", pno)
        print("Idly         :", idly_q,"   -   RS=", idly)
        print("Dosa         :",dosa_q,"   -   RS=", dosa)
        print("Poori        :", poori_q,"   -   RS=", poori)
        print("Total Bill   :", float(bill))
        print("..............Thank You.....................")

    except ValueError:
        print(" !This is not a valid number ")


billing()
