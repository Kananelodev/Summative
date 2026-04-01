"""
main.py

This file contains the implementations for the Summative assessment questions.
"""

# Question 1: parse_pothole_reports
def parse_pothole_reports(raw_data: list) -> dict:
    new = {}

    for i in raw_data:
        ok = i.split('|')
        well = ok[0].split(":")
        wello = ok[1].split(":")

        new.setdefault(well[1], int(wello[1]))
    return new
     

# print(parse_pothole_reports(["STREET:Bree|SEVERITY:3", "STREET:Alice|SEVERITY:8"]))
# Question 2: taxi_revenue_tracker
def taxi_revenue_tracker(trips: list) -> dict:
    new = {}

    for trip in trips:
        driver = trip['driver']
        amount = trip['fare']
        new[driver] = new.get(driver, 0) + amount
    return new

# print(taxi_revenue_tracker([{"driver": "Sipho", "fare": 100},
#                             {"driver": "Amara", "fare": 200}, 
#                             {"driver": "Sipho", "fare": 50}]))

# Question 3: electrical_grid_status
def electrical_grid_status(suburbs: dict) -> list:
    new = []

    for key, value in suburbs.items():
        well = value
        if isinstance(well, dict):
            new.extend(electrical_grid_status(value))
        
        elif value == "OFF":
            new.append(key)
    
    return new

# print(electrical_grid_status({"Gauteng": {"Soweto": "OFF", "Sandton": "ON"}, 
#                               "Western Cape": {"Langa": "OFF"}}))

# Question 4: grant_payment_formatter
def grant_payment_formatter(beneficiaries: list) -> str:
    pass

# Question 5: logistics_chain_validator
def logistics_chain_validator(nodes: list, cargo_weight: int) -> bool:
    well = [i for i in nodes if i > cargo_weight]

    if len(well) < len(nodes):
        return False
    else:
        return True

# print(logistics_chain_validator([100, 80, 150], 90))
from collections import Counter
# Question 6: deep_merge_inventories
def deep_merge_inventories(store_a: dict, store_b: dict) -> dict:
    
   well = Counter(store_a) + Counter(store_b)
   return well

print(deep_merge_inventories( {"Milk": 2}, {"Milk": 3, "Bread": 1}))
