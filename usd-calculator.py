def prompt1():
    answer = input("Would you like to review your coins? [yes/no] ").lower()
    if answer == 'yes' or answer == 'y':
        print("You have " + pennies + " pennies, " + nickels + " nickels, " + dimes + " dimes, " + quarters + " quarters, " + penny_rolls + " penny rolls, " + nickel_rolls + " nickel rolls, " + dime_rolls + " dime rolls, and " + quarter_rolls + " quarter rolls.")
    elif answer == 'no' or answer == 'n':
        print()
        print("Okay, let's continue.")
    else:
        print("You didn't pick yes or no, try again.")
        prompt1()

def prompt2():
    answer = input("Would you like to review your bills? [yes/no] ").lower()
    if answer == 'yes' or answer == 'y':
        print("You have " + ones + " ones, " + twos + " twos, " + fives + " fives, " + tens + " tens, " + twenties + " twenties, " + fifties + " fifties, and " + hundreds + " hundreds.")
    elif answer == 'no' or answer == 'n':
        print()
        print("Okay, let's continue.")
    else:
        print("You didn't pick yes or no, try again.")
        prompt2()

print("Please input your coins: ")
pennies = float(input("pennies: "))
nickels = float(input("nickels: "))
dimes = float(input("dimes: "))
quarters = float(input("quarters: "))
penny_rolls = float(input("penny rolls: "))
nickel_rolls = float(input("nickel rolls: "))
dime_rolls = float(input("dime rolls: "))
quarter_rolls = float(input("quarter rolls: "))
dollar_coins = float(input("dollar coins: "))

print()

prompt1()

print()

print("Please input your bills: ")
ones = float(input("ones: "))
twos = float(input("twos: "))
fives = float(input("fives: "))
tens = float(input("tens: "))
twenties = float(input("twentites: "))
fifties = float(input("fifties: "))
hundreds = float(input("hundreds: "))

print()

prompt2()

print()

total = (int(pennies)*0.01) + (int(nickels)*0.05) + (int(dimes)*0.10) + (int(quarters)*0.25) + (int(dollat_coins)*1.00) + (int(penny_rolls)*0.50) + (int(nickel_rolls)*2.00) + (int(dime_rolls)*5.00) + (int(quarter_rolls)*10.00) + (int(ones)*1.00) + (int(twos)*2.00) + (int(fives)*5.00) + (int(tens)*10.00) + (int(twenties)*20.00) + (int(fifties)*50) + (int(hundreds)*100)

print("Your total is", total)
