#Electricity_bill_calculator........
customer_name = input("enter customer_name : ")
electricity_units = int(input("enter number of electricity units used : "))
print("customer name : ", customer_name)
print("units used : ", electricity_units)

if electricity_units < 0:
    print("Invalid units")
