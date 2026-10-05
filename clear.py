try:
    date = int(input("enter the date: "))
    
    if 1 <= date <= 31:
        # Read multiple plates separated by space (e.g., "1024 3051 8812")
        plate_input = input("enter car plates separated by spaces: ")
        vechal = [int(x) for x in plate_input.split()]
        
        exempt_vehicles = []
        tolled_vehicles = []
        toll_count = 0

        is_even_day = (date % 2 == 0)

        for plate in vechal:
            is_even_plate = (plate % 2 == 0)
            
            if is_even_day == is_even_plate:
                exempt_vehicles.append(plate)
            else:
                tolled_vehicles.append(plate)
                toll_count += 1

        total_revenue = toll_count * 10

        print("Exempt Vehicles:", exempt_vehicles)
        print("Tolled Vehicles:", tolled_vehicles)
        print("total revenue:", total_revenue)
    else:
        print("enter valid date")

except ValueError:
    print("enter the valid value")