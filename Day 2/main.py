print("Welcome to the tip calculator!")
# Taking input from the user and converting to float
Bill = float(input("What was the total bill? $ "))
# Taking input from the user and converting to integer
tip = int(input("How much would you like to give? 5, 7 or 10? "))
# Taking input and converting to integer
split_people = int(input("How many people to split the bill? "))
# Logic for tip percentage calculation and final bill calculation
tip_as_percent = tip/100
total_tip_amount = Bill*tip_as_percent
total_bill = Bill + total_tip_amount
bill_per_person = total_bill/split_people
final_bill = round(bill_per_person, 2)
print(f"Each Person Should pay $ {final_bill}")