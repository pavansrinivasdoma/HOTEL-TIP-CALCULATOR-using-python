# ******* TIP CALCULATOR *******

print("\t**^**WELCOME TO TIP CALCULATOR**^**\t")  #WELCOME MESSAGE
#USER GIVES DETAILS ABOUT BILL
bill_amount = int(input('Enter the bill amount: Rs.'))
tip = int(input('Enter the tip percentage you would like to give: '))
people = int(input('Enter how many members are there: '))

tip_as_percent = tip/100  #CONVERT TIP INTO PERCENTAGE
total_tip = bill_amount*tip_as_percent  #CALCULATING TIP AMOUNT
total_bill = bill_amount + total_tip  #CALCULATING TOTAL BILL AMOUNT
bill_per_person = total_bill/people  #CALCULATING HOW MUCH AMOUNT EACH ONE HAS TO PAY
final_amount = round(bill_per_person,2)  #ROUNDING OFF THE VALUE TO 2 DECIMALS IF ITS A BIG DECIMAIL NUMBER
final_amount = "{:.2f}".format(bill_per_person)  #SOME TIMES PYTHON WILL NOT ROUND OFF TO 2 DECIMAL POINTS DUE TO SOME COMPLEX MATHEMATICAL OPERATIONS. SO WE MAKE USE OF THIS format FUNCTION
print(f'Each member has to pay Rs.{final_amount}')  #PRINTS THE FINAL AMOUNT EACH ONE HAS TO PAY
