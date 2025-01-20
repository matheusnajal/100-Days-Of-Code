import data

profit = 0

def report():
    print(
        f"\nWater: {data.resources['water']}ml\n"
        f"Milk: {data.resources['milk']}ml\n"
        f"Coffee: {data.resources['coffee']}g\n"
        f"Money: ${profit}\n"
    )

def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > data.resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough = False
    return is_enough

def process_coins():
    print("Please insert coins.")
    total = int(input("How many pennies?: ")) * 0.01
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many quarters?: ")) * 0.25
    return round(total, 2)

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        data.resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

def main():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
            print("Invalid choice. Please select a valid option.")
            continue

        match choice:
            case 'off':
                print("Turning off the machine. Goodbye!")
                return
            case 'report':
                report()
            case _:
                drink = data.MENU.get(choice)
                if drink and is_resource_sufficient(drink["ingredients"]):
                    payment = process_coins()
                    if is_transaction_successful(payment, drink['cost']):
                        make_coffee(choice, drink["ingredients"])

if __name__ == '__main__':
    main()
