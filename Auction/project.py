bid = {}

def bidding_status(bidding):
    highest_amt = 0
    winner = ""
    for bidder in bidding:
        bid_amt = bidding[bidder]
        if bid_amt > highest_amt:
            highest_amt = bid_amt
            winner = bidder
    print(f"The winner is {winner} and the highest bid is {highest_amt}")

biding_over = False
while not biding_over:
    name = input("Enter your name: ")
    price = int(input("Enter your bid amount in rupees: "))
    bid[name] = price
    a = input("if you want to continue the bid enter 'y' and if you want to end the bid enter 'n'")
    if a == 'n':
        bidding_status(bid)
        biding_over = True
    elif a == 'y':
        biding_over == False
    else:
        print("Invalid input")


