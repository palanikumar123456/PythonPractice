print("*******  100DaysOfPython - Dr Angela Yu  *******")
print("    Day02 Project Exercise: Tip Calculator      ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("""Note: 
Calculating the Total Bill Amount Per Person at a Restaurant

# If the Restaurant Bill was $150.00, and
# Split and share between 5 of Your Friends, and
# With a Tip of 12% then,
# Each Person should Pay: (150.00/5) * 1.12
 
Q1: How many of you went to the Restaurant.?
Q2: What is the Bill Amount at Restaurant.?
Q3: What is your Tip Percentage (10, 12 or 15) to offer.?
Q4: What is the Total Bill Amount.?
Q5: What is the Bill Amount to be paid by Each Person.?
Total Bill Amount : 'Bill Amount' -plus- 'Tip Amount'
Bill Per Person is: Total Bill / No.of Friends
Total Bill Amount Per Person shall be shown 2 Decimal Places.. 
""")
print("Welcome to the TIP Calculator")
bill_amount = float(input("What is the Bill Amount.? $"))
tip_percent = int(input("What is the Tip [10, 12, 15] Percentage offered.? "))
tip_as_percentage = tip_percent/100
tip_amount = bill_amount * tip_as_percentage
total_bill = bill_amount + tip_amount
no_of_people = int(input("How many of Friends went and Share the Bill.? "))
print(f"Bill Amount: {bill_amount}")
print(f"Tip Amount : {tip_amount}")
print(f"Total Bill As Is: {total_bill}")
print(f"Total Bill Amount Rounded : ${round(total_bill, 2)}")
bill_per_person = total_bill/no_of_people
print(f"Each Person should pay: ${round(bill_per_person, 2)} only.")
