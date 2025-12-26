stocks = {
    "GME": 5.00,
    "APPL": 120.00,
    "PURP": 800.00,
}
print(stocks["GME"])
stocks["Poop"] = 10.00
print(stocks)

#looping in a dictionary
for key in stocks:
    print(key, stocks[key])

# for nested dictionary with list see the following on how to print a certain element

# travel_log = {
#   "France": ["Paris, "Lille", "Dijon"]
# }

# to print lille you would do the following
# print(travel_log["France"][1]) as it is on element 1 and you access the key first.

## for nested list see below
# nested_list = ["a", "b", ["c" , "d"]

#print(nested_list[2][1])

## the following is nesting a dictionary in a dictionary
# travel_log = {
#   "France": {
#   "num_times_visted": 8,
#    "cities_visited":  ["Paris, "Lille", "Dijon"]
# }
# print(travel_log["France"]["cities_visited"[1]) will print Lille.