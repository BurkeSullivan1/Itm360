# Program 0 Practice problems 1-3 Review
# Burke Sullivan
# ITM 360


##########

#1 Pig latin
"""
def getPigLatin(pigStr):
    # Split the sentence into words
    words = pigStr.split()

    # Convert each word to Pig Latin
    pigLatinWords = [word[1:] + word[0] + "ay" for word in words]

    pigLatinSentence = ' '.join(pigLatinWords)

    return pigLatinSentence

def main():
    # Example sentence
    sentence = "I SLEPT MOST OF THE NIGHT"

    # Convert to Pig Latin
    pigLatinSentence = getPigLatin(sentence)

    # Print the Pig Latin sentence
    print("English:", sentence)
    print("Pig Latin:", pigLatinSentence)

# Call the main function
main()

#Q2

# Shi[p packages local or internationally
def ship_packages(weight,location):
    if weight <= 2:
        if location.lower() == "domestic":
            return 1.50
        elif location.lower() == "international":
            return 5.00
    elif 2 < weight <= 6:
        if location.lower() == "domestic":
            return 3
        elif location.lower() == "international":
            return 10
    elif 6 < weight <= 10:
        if location.lower() == "domestic":
            return 4
        elif location.lower() == "international":
            return 15
    else:
        if location.lower() == "domestic":
            return 4.75
        elif location.lower() == "international":
            return 25




def run_function():
    cost_P = 0

    for x in range(1,2):  #start with a package
        print(f"Package: {x}")
        location = input("Where would you like to ship? ")
        weight = float(input("How much weight?"))

        total_cost = ship_packages(weight,location)
        cost_P += total_cost

        print(f'For package {x} the total cost is {cost_P}$ ')




run_function()

"""


##Q3
###Bank account - Balance -- withdraw, deposit 

def depositAmount(balance,amount):
    updated_balance = balance + amount
    return (f'Your new balance is ${updated_balance}')


def withdrawAmount(balance,amount):
    if balance >= amount:
        balance -= amount  # Subtract amount from balance
        print(f"Withdrawal successful. New balance: {balance}")
    else:
        print("Insufficient balance! No withdrawals made.")
    return balance

def main():
    # Ask user for their starting balance
    balance = float(input("What is your starting balance? "))

    while True:
        # Ask user what they want to do
        action = input("Do you want to withdraw funds, deposit funds, or quit? (withdraw/deposit/quit): ").lower()

        if action == 'withdraw':
            amount = float(input("How much would you like to withdraw? "))
            balance = withdrawAmount(balance, amount)
        elif action == 'deposit':
            amount = float(input("How much would you like to deposit? "))
            balance = depositAmount(balance, amount)
        elif action == 'quit':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose 'withdraw', 'deposit', or 'quit'.")

        print(f"Current balance: {balance}")

# Call the main function
if __name__ == "__main__":
    main()









