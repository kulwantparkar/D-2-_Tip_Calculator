#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("WELCOME TO THE TIP CALCULATOR")
while True:
  total_bill = float(input("what was the total bill?-\n$"))
  no_of_people = int(input("how many people to split the bill?-\n"))
  tip = int(input("what percentage tip would you like to give?- 10%, 12%, 15%\n"))
  total_tip=float((tip/100) + 1)
  bill_of_each_person = (total_bill/no_of_people)*total_tip
  in_two_decimal="{:.2f}".format(bill_of_each_person)
  print("$" + in_two_decimal)

  continue_or_not = input("if you want to continue press - y/n\n")
  if continue_or_not == "y":
    continue
  else:
    break


