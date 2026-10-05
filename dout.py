
    date = int(input("enter the date:"))
    if 1<=date<=31 :
        vechal=input("enter the cars :")
        vechal_plate=[int(x) for x in vechal.split()]
        exempt= []
        toll= []
        toll_count=0
        is_even_day=(date%2==0)
        for plate in vechal_plate:
            is_even_plate=(plate%2==0)
            if is_even_day==is_even_plate:
                exempt.append(plate)
            else:
                toll_count +=1
                toll.append(plate)
        total_revanue =10*toll_count
        print("Exempt Vehicles",exempt)
        print("Tolled vehicles",toll)
        print("toltal ravanued:",total_revanue)
    else:
        print("enter the valid date :")
        






