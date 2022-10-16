service_time = int(input("Service Time: "))
business_hours = [5, 6, 7]
amount = int(input("Computer: "))
wiling_to_Drop = True
pick_up = True

base_fee = 0
additional_fee = 0
 
if amount == 1 or amount  == 2:
    base_fee, additional_fee = 50, 0
elif 3 <= amount <= 10:
    base_fee, additional_fee = 100, 10
elif amount > 10:
    base_fee, additional_fee =500, 10


if service_time not in business_hours:
    base_fee = base_fee*2
if wiling_to_Drop and pick_up:
    base_fee = base_fee//2

print(base_fee, additional_fee)
    
    
