
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_to_pay = int(input("How many people to split the bill? "))

percentagem = percent_tip / 100 + 1

bill_for_each = total_bill / people_to_pay * percentagem
bill_for_each_round = "{:.2f}".format(bill_for_each)
print(f"Each person should pay: ${bill_for_each_round}")

