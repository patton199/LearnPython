# answer 3
wait_to_search_list = ("1st", "2nd", "3rd", "4th", "5th")
search_string = "4th"
for i, string in enumerate(wait_to_search_list):
    if string == search_string:
        print ("search_string is equal string, position is on %d" % i)
    else:
        print("search_string's position isn't on %d." % (i))

# answer 4
fridge = {"egg": 8, "mushroom": 20, "pepper": 3, "cheese": 2, "tomato": 4, "milk": 13}
food_sought = "apple"
# 遍历fridge里的值
for key in fridge.keys():
    print ("%s's value is %s." % (key, fridge[key]))
# 判字):
for key in (fridge):
    if food_sought == key:
        print ("Found what I was looking for: %s's number is %d." % (key, fridge[key]))
        break
else:
    print("%s wasn't found in the fridge." % (food_sought))

# answer 5
fridge = {"egg": 8, "mushroom": 20, "pepper": 3, "cheese": 2, "tomato": 4, "milk": 13}
fridge_list = fridge.keys()
print (fridge_list)
