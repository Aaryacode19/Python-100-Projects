#This is a simple program to calculate tips. You enter the total bill and the tip percentage you want to give and also how many people u wan split bill with. The program then calculates the tip amount and tells the total bill each person should pay with the tip included. It's a handy tool for making sure you leave a fair tip at restaurants! 
#So next time you need to tip someone and split ur bill, use your personal tool and make tipping easy and accurate! 

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
