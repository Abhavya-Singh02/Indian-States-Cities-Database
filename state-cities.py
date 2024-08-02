# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 23:19:22 2024

@author: abhav
"""

import json
states = ["Andaman & Nicobar", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh", "Chhattisgarh", "Dadra & Nagar Haveli", "Daman & Diu", "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand",
          "Karnataka", "Kerala", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Orissa", "Pondicherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura", "Uttar Pradesh", "Uttaranchal", "West Bengal"]


# Read JSON data from file to get list of cities. Json file provide in repo data.json.
with open('data.json', 'r') as f:
    jsonString = f.read()

python_list = json.loads(jsonString)
print(python_list)


cities = python_list

cities.pop(0)


# code for city 
state = input("Enter State: ")
for i in range(len(states)):
    if states[i]==state:
        print(cities[i])
        
# code for state
city = input("Enter City: ")
cities1 = ""
for i in range(len(cities)):
    cities1 += str(cities[i].strip().split('|'))
    if city in cities1:
        print(states[i])
        break


