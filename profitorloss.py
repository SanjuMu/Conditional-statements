actual_cost = float(input("Please Enter the Actual Product price: "))
sale_amount = float(input ("Enter the sale amount:"))
if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))

else:
    print("NO PROFIT!!!!")