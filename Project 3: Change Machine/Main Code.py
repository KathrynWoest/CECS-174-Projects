def stock(n_stock, d_stock, q_stock, o_stock, f_stock):  # print stock function, Chris Kau
    """description: prints the stock of the machine
       parameters: each type of possible currency for stock
       returns: a printed stock menu, no values"""
    i_n_stock = int(n_stock)  # each type of stock as integers
    i_d_stock = int(d_stock)
    i_q_stock = int(q_stock)
    i_o_stock = int(o_stock)
    i_f_stock = int(f_stock)
    print(f"\nStock contains:\n\t{i_n_stock} nickels\n\t{i_d_stock} dimes\n\t{i_q_stock} quarters\n\t{i_o_stock} ones\n"
          f"\t{i_f_stock} fives\n")


def menu():  # print menu function, Chris Kau
    """description: prints the possible menu for deposits
       parameters: none
       returns: a printed deposit menu, no values"""
    print("\nMenu for deposits:")
    print("\t'n' - deposit a nickel\n\t'd' - deposit a dime\n\t'q' - deposit a quarter"
          "\n\t'o' - deposit a one dollar bill\n\t'f' - deposit a five dollar bill\n\t'c' - cancel the purchase\n")


def refund_change(q_ref, d_ref, n_ref):  # print refund amount, Chris Kau
    """description: prints the refund amount for each currency if there is any to refund of that type
       parameters: refund amounts for quarters, dimes, and nickels
       returns: printed refund statement, no values"""
    if q_ref > 0:  # if amount to refund is > 0, print the amount.  otherwise, do not print for this type of currency
        print(f"\t{q_ref} quarter(s)")
    if d_ref > 0:
        print(f"\t{d_ref} dime(s)")
    if n_ref > 0:
        print(f"\t{n_ref} nickel(s)")


def change_change(q_ch, d_ch, n_ch):  # print change amount, Chris Kau
    """description: prints the change amount for each currency if there is any to return of that type
           parameters: change amounts for quarters, dimes, and nickels
           returns: printed change statement, no values"""
    if q_ch > 0:  # if amount of change is > 0, print the amount.  otherwise, do not print for this type of currency
        print(f"\t{q_ch} quarter(s)")
    if d_ch > 0:
        print(f"\t{d_ch} dime(s)")
    if n_ch > 0:
        print(f"\t{n_ch} nickel(s)")


def stock_total(n_stock, d_stock, q_stock, o_stock, f_stock):  # print total stock at end of code, Kathryn Woest
    """description: calculates the final stock and prints it once the user quits
       parameters: amount of each currency type
       returns: print statement of final stock, no values"""
    # calculation for total stock using amount of each currency times how much each is worth and adding the products
    total = int((n_stock * 5) + (d_stock * 10) + (q_stock * 25) + (o_stock * 100) + (f_stock * 500))
    dollar = total // 100
    cents = total % 100
    if dollar > 0:  # if there is at least one full dollar, print with dollar.  otherwise, just print coins
        print(f"\nTotal: {dollar} dollar(s) and {cents} cents")
    else:
        print(f"\nTotal: {cents} cents")


def main():  # main code begins here, Chris Kau (61-112)
    # initial stock
    n_s = 25
    d_s = 25
    q_s = 25
    o_s = 0
    f_s = 0
    print("\nWelcome to the vending machine change maker program\nChange maker initialized.")
    stock(n_s, d_s, q_s, o_s, f_s)
    price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    while price != 'q':  # iterate through this loop until the user quits with 'q'
        f_price = float(price)  # convert the price entered into a float
        original_price = round(f_price * 100)  # convert price into cents (this variable is a constant)
        not_paid = round(f_price * 100)  # convert price into cents (this price will change throughout transaction)
        if original_price < 0 or original_price % 5 != 0:  # if price entered is not valid
            print("Illegal price: Must be a non-negative multiple of 5 cents.\n")
        else:
            menu()
            dollar = original_price // 100  # find original price in dollars and cents
            cents = original_price % 100
            while not_paid > 0:  # iterate through this loop until the amount paid >= the original price
                if dollar > 0:  # if there is at least one full dollar, print with dollar.  otherwise, just print coins
                    print(f"Payment due: {dollar} dollar(s) and {cents} cents")
                    deposit = input("Indicate your deposit: ")
                else:
                    print(f"Payment due: {cents} cents")
                    deposit = input("Indicate your deposit: ")
                while deposit != 'n' and deposit != 'd' and deposit != 'q' and deposit != 'o' \
                        and deposit != 'f' and deposit != 'c':  # iterate through this loop until deposit is valid
                    print(f"Illegal selection: {deposit}")
                    if dollar > 0:
                        print(f"Payment due: {dollar} dollar(s) and {cents} cents")
                        deposit = input("Indicate your deposit: ")
                    else:
                        print(f"Payment due: {cents} cents")
                        deposit = input("Indicate your deposit: ")
                # check each type of deposit, subtract the deposit from the total price, and add to the total stock
                if deposit == 'n':
                    not_paid -= 5
                    n_s += 1
                elif deposit == 'd':
                    not_paid -= 10
                    d_s += 1
                elif deposit == 'q':
                    not_paid -= 25
                    q_s += 1
                elif deposit == 'o':
                    not_paid -= 100
                    o_s += 1
                elif deposit == 'f':
                    not_paid -= 500
                    f_s += 1
                else:  # if the user enters 'c' for cancel: Kathryn Woest (113-216)
                    refund = original_price - not_paid  # calculate amount to refund
                    if refund != 0:  # if there is money to refund:
                        # move through each currency type and refund what is possible from each
                        q_possible = refund // 25  # find the max number of quarters that go into refund
                        if q_possible >= q_s:  # if max number is >= what is in the stock:
                            q_refund = int(q_s)  # refund what is in the stock
                            q_s = 0  # set the stock to 0
                            refund -= (q_refund * 25)  # subtract the quarters refund from the total refund
                        else:  # if max number is < what is in the stock:
                            q_refund = int(q_possible)  # refund the max number
                            q_s -= q_possible  # subtract the max number from the stock
                            refund -= (q_refund * 25)  # subtract the quarters refund from the total refund
                        d_possible = refund // 10  # repeat for dimes and nickels
                        if d_possible >= d_s:
                            d_refund = int(d_s)
                            d_s = 0
                            refund -= (d_refund * 10)
                        else:
                            d_refund = int(d_possible)
                            d_s -= d_possible
                            refund -= (d_refund * 10)
                        n_possible = refund // 5
                        if n_possible >= n_s:
                            n_refund = int(n_s)
                            n_s = 0
                            refund -= (n_refund * 5)
                        else:
                            n_refund = int(n_possible)
                            n_s -= n_possible
                            refund -= (n_refund * 5)
                        if refund > 0:  # if, once you go through all currency types, there is still money to refund:
                            print("\nPlease take the change below.")
                            refund_change(q_refund, d_refund, n_refund)
                            print("Machine is out of change.\nSee store manager for remaining refund.")
                            dollar = refund // 100
                            cents = refund % 100
                            if dollar > 0:
                                print(f"Amount due is: {dollar} dollar(s) and {cents} cents")
                            else:
                                print(f"Amount due is: {cents} cents")
                            stock(n_s, d_s, q_s, o_s, f_s)
                            break  # exit the loop and skip to asking the user for a new price/q input
                        else:  # if the stock can match the refund amount exactly:
                            print("\nPlease take the change below.")
                            refund_change(q_refund, d_refund, n_refund)
                            stock(n_s, d_s, q_s, o_s, f_s)
                            break  # exit the loop and skip to asking the user for a new price/q input
                    else:  # if the amount to be refunded is 0:
                        print("\nPlease take the change below.")
                        print("  No change due.")
                        stock(n_s, d_s, q_s, o_s, f_s)
                        break  # exit the loop and skip to asking the user for a new price/q input
                dollar = not_paid // 100  # recalculate the dollar and cents of remaining price and return to top
                cents = not_paid % 100
            if not_paid < 0:  # if the user pays more than the original price, we need to calculate change:
                change = -not_paid  # calculate change
                # move through each currency type and give change for what is possible from each
                q_possible = change // 25  # repeat refund steps but with new variables for change
                if q_possible >= q_s:
                    q_change = int(q_s)
                    q_s = 0
                    change -= (q_change * 25)
                else:
                    q_change = int(q_possible)
                    q_s -= q_possible
                    change -= (q_change * 25)
                d_possible = change // 10
                if d_possible >= d_s:
                    d_change = int(d_s)
                    d_s = 0
                    change -= (d_change * 10)
                else:
                    d_change = int(d_possible)
                    d_s -= d_possible
                    change -= (d_change * 10)
                n_possible = change // 5
                if n_possible >= n_s:
                    n_change = int(n_s)
                    n_s = 0
                    change -= (n_change * 5)
                else:
                    n_change = int(n_possible)
                    n_s -= n_possible
                    change -= (n_change * 5)
                if change > 0:  # if, once you go through all currency types, there is still money to return:
                    print("\nPlease take the change below.")
                    change_change(q_change, d_change, n_change)
                    print("Machine is out of change.\nSee store manager for remaining refund.")
                    dollar = change // 100
                    cents = change % 100
                    if dollar > 0:
                        print(f"Amount due is: {dollar} dollar(s) and {cents} cents")
                    else:
                        print(f"Amount due is: {cents} cents")
                    stock(n_s, d_s, q_s, o_s, f_s)
                else:  # if change can be dispensed exactly:
                    print("\nPlease take the change below.")
                    change_change(q_change, d_change, n_change)
                    stock(n_s, d_s, q_s, o_s, f_s)
            elif not_paid == 0:  # if the user enters the exact amount needed to pay:
                print("\nPlease take the change below.")
                print("  No change due.")
                stock(n_s, d_s, q_s, o_s, f_s)
        # ask again for a new input, then loop to the top and check to see if it is 'q', Chris Kau (217-224)
        price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    stock_total(n_s, d_s, q_s, o_s, f_s)  # print the total stock once the user quits


if __name__ == "__main__":  # run the main code
    main()