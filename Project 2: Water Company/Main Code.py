# get user inputs for customer code and meter readings
user_code = input("Enter Customer's Code: ")
bm_reading = int(input("Enter Customer's Beginning Meter Reading: "))
em_reading = int(input("Enter Customer's Ending Meter Reading:    "))
print()

# checks to see if customer code and meter readings are accepted values and in range
if (user_code == 'R' or user_code == 'C' or user_code == 'I' or user_code == 'r' or user_code == 'c' or
        user_code == 'i') and (bm_reading in range(0, 1_000_000_000)) and (em_reading in range(0, 1_000_000_000)):
    # checks if the em reading flipped over to 000_000_000
    if em_reading < bm_reading:
        # calculates gallons of water used if previous statement is true
        new_em_reading = em_reading + 1_000_000_000
        water_used = new_em_reading - bm_reading
        gallons_used = water_used / 10
    else:
        # calculates gallons of water used if previous statement is false
        water_used = em_reading - bm_reading
        gallons_used = water_used / 10
    if user_code == 'R' or user_code == 'r':
        # calculates amount billed if user_code is residential
        billed = 5.00 + (0.0005 * gallons_used)
    elif user_code == 'C' or user_code == 'c':
        # calculates amount billed if user_code is commercial
        if gallons_used > 4_000_000:
            # checks how much water was used to determine billing tier
            extra = gallons_used - 4_000_000
            billed = 1000.00 + (extra * 0.00025)
        else:
            billed = 1000.00
    else:
        # calculates amount billed if user_code is industrial
        if gallons_used > 10_000_000:
            # checks how much water was used to determine billing tier
            extra = gallons_used - 10_000_000
            billed = 2000.00 + (extra * 0.00025)
        elif gallons_used >= 4_000_000:
            billed = 2000.00
        else:
            billed = 1000.00
    # prints user inputs, water used, and amount billed if inputs were valid
    print("Customer Code:", user_code)
    print(f"Customer's Beginning Meter Reading: {bm_reading:0>9}")
    print(f"Customer's Ending Meter Reading:    {em_reading:0>9}")
    print(f"Gallons of Water Used: {gallons_used:.1f}")
    print(f"Amount Billed: ${billed:.2f}")
# prints user inputs, water used, and amount billed if inputs were invalid
else:
    print("Customer Code:", user_code)
    print(f"Customer's Beginning Meter Reading: {bm_reading:0>9}")
    print(f"Customer's Ending Meter Reading:    {em_reading:0>9}")
    print("Invalid Entry")
    print("Gallons of Water Used: 0.0")
    print("Amount Billed: $0.00")
