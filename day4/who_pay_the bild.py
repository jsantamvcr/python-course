import random
# who pay the bill

friends = ['susan', 'bob', 'alice', 'tom']

#randomly select a name from the list of friends

bill_payer = random.choice(friends)
print(f"{bill_payer.upper()} WILL PAY THE BILL.")

random_number = random.randint(0,5)
friend = friends[random_number].upper()
print(f"{friend} WILL PAY THE BILL.")


