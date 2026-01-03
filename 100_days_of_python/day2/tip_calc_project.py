"""BILL COMES"""
bill = float(input("what was total bill ?:\n "))
"""TAKE AN BILL ALSO THINK ABOUT TIP PERCENT"""
tip = int(input("what percent tip like to give? 10 12 15:\n "))
"""HOW MUCH PERSON"""
people = int(input("how many going to split the bill ?:\n "))
"""CALCULATION OF BILL AND TIP"""
# need to calculate tip : for 15%: 15/100 = 0.15 ,
tip_as_percent = bill/100   # 0.15 stored in tp as percent
# thn calculate total tip amount with total 153.45*0.15 = 23.0175
total_tip = bill * tip_as_percent # 153.45*0.15 = 23.0175
#ADD the bill and total tip
total_bill = bill + total_tip
#each person bill
bill_per_person = total_bill / people
final_bill = round(bill_per_person, 2)
print(f"Each should pay: {final_bill}")

