import art
print(art.logo)
#todo-1: ask the user for input

#todo-2: save data into dictionary {name: price}

#todo-3: whether if new bids needs to be added
#step:5
def find_highest_bidders(bidding_dictionary): # bidding dictionary means bid
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary: # for bidder in bid:
        """bidding_dictionary[bidder] it fetch value pair from dict and stored to variable bid_amount"""
        bid_amount = bidding_dictionary[bidder] # fetch (value-price)
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder # in bidder it have name (key from dictionary, in key stores name of bidder )
    print(f"The winner is {winner} with bid amount {highest_bid}.")

bid = {} # creating empty dictionary , after step1
continue_bidding = True
while continue_bidding:
    #step1:  ask the user for input name and price
    name = input("what is your name?: ")
    price = int(input("Enter your bid price: $"))
    #step2: save data into dictionary {name: price}
    bid[name] = price # assign key as name and value as price in bid dictionary
    # step 3: whether if new bids needs to be added
    should_continue = input("Are there any other bidders? type 'yes' or 'no': ")
    #step:4
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidders(bid) # for calling this we have to create function
    elif should_continue == 'yes':
        print("\n" * 20)

#todo-4: compare bids in dictionary


