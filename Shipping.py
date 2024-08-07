weight = 41.5

#ground shipping
if weight <= 2:
  cost = weight*1.5+20
  print(f"cost: ${cost}")
elif 2 <= weight <= 6:
  cost = weight*3.0+20
  print(f"cost: ${cost}")
elif 6 <= weight <= 10:
  cost = weight*4.0+20
  print(f"cost: ${cost}")
else:
  cost = weight*4.75+20
  print(f"cost: ${cost}")

ground_premium = 125.0
total_price = cost+ground_premium
print(f"Ground shipment details = Cost: {cost}, Ground premium: {ground_premium}, and Total: {total_price}")

#drone shipping
if weight <= 2:
  cost = weight*4.5
  print(f"cost: ${cost}")
elif 2 <= weight <= 6:
  cost = weight*9
  print(f"cost: ${cost}")
elif 6 <= weight <= 10:
  cost = weight*12
  print(f"cost: ${cost}")
else:
  cost = weight*14.25
  print(f"cost: ${cost}")

ground_premium = 0
drone_total_price = cost
print(f"Drone shipment details = Cost: {cost}, Ground premium: {ground_premium}, and Drone Shipping Total: {drone_total_price}")

if total_price < drone_total_price:
  print("Ground shipping is cheaper")
elif total_price == drone_total_price:
  print("Cost is the same")
elif total_price > drone_total_price:
  print("Drone shipping is cheaper")
else:
  print("Error, check code again")
