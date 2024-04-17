from art import logo
print(logo)

#HINT: You can call clear() to clear the output in the console.

bidders = {}
bidding_finish = False


def find_highest_bidder(bidding_record):
    max_bid = 0
    for bidder in bidding_record:
        if bidding_record[bidder] > max_bid:
            max_bid = bidding_record[bidder]
            #winner = bidder
    
    print("The winner is {winner} with a bid of {max_bid}")

while not bidding_finish:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid
    should_continue = input("Are you any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        bidding_finish = True
        find_highest_bidder(bidders)
    elif should_continue == 'yes':
        print('\n' * 5)  # Efface la sortie de la console


