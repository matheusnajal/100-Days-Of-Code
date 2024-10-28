from art import logo
import os

print(logo)

bids = {}

while True:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))

    bids[name] = price

    should_continue = input('Is this the last bid? ("Yes" or "No") \n').lower()
    os.system('cls')
    if should_continue == "yes":
        break

max_bidder = max(bids, key=bids.get)
max_bid = bids[max_bidder]

print(f"The winner is {max_bidder} with a bid of ${max_bid:.2f}")