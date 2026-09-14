#Electricity_bill_calculator........
customer_name = input("enter customer_name : ")
electricity_units = int(input("enter number of electricity units used : "))
print("customer name : ", customer_name)
print("units used : ", electricity_units)

if electricity_units < 0:
    print("Invalid units")
elif electricity_units<=100 :
    bill = electricity_units*5
elif electricity_units<=200 :
    bill= (100*5)+(electricity_units- 100)*7
 elif electricity_units<=300 :
        bill = (100*5)+(100*7)+(electricity_units-200)*10
else:
        bill= (100*5)+(100*7)+(100*10)+(electricity_units-300)*12    
if bill > 2000:
        surcharge = bill * 0.1
 else:
        surcharge = 0
    print("surcharge :", surcharge)
    final_bill = bill + surcharge
    print("final_bill :", final_bill)
