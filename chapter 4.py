apples = ["Mackintosh", "Golden Delicious", "Fuji", "Mitsu"]
apple_trees = ["Golden Delicious", "Fuji", "Mitsu", "Mackintosh"]
print(apples == apple_trees)
# result false

apple_trees = ["Mackintosh", "Golden Delicious", "Fuji", "Mitsu"]
print(apples == apple_trees)
# result True

tuesday_breakfast_sold = {"pancakes": 10, "french toast": 4, "bagels": 32, "omelets": 12, "egg and sausages": 13}
wednesday_breakfast_sold = {"pancakes": 8, "french toast": 5, "bagels": 22, "omelets": 16, "egg and sausages": 22}
print(tuesday_breakfast_sold == wednesday_breakfast_sold)
# result false

wednesday_breakfast_sold = {"pancakes": 10, "french toast": 4, "bagels": 32, "omelets": 12, "egg and sausages": 13}
print(tuesday_breakfast_sold == wednesday_breakfast_sold)
# result true

'''
if :
elif :
else:
'''
OJ_price = 2.50
if OJ_price < 1.25:
    print ("Get one, I'm thirsty.")
elif OJ_price <= 2.00:
    print("Ummm... sure, but I'll drink it slowly.")
else:
    print ("I don't have enough money. Never mind.")
# result I don't have enough money. Never mind.


# for
# continue
for food in ("pate", "cheese", "rotten apples", "crackers", "whip cream", "tomato soup"):
    if food[0:6] == "rotten":
        continue
    print("Hey you can %s." % (food))

# try:
fridge_contents = {"egg": 8, "mushroom": 20, "pepper": 3, "cheese": 2, "tomato": 4, "milk": 13}
try:
    if fridge_contents["orange juice"] > 3:
        print("Sure, let's have some juice!")
except KeyError:
    print("Awww, there is no juice. Let's go shopping!")
# result Awww, there is no juice. Let's go shopping!

try:
    if fridge_contents["orange juice"] > 3:
        print("Sure, let's have some juice!")
except (KeyError) as error:
    print("woah! There is no %s." % error)
# result woah! There is no 'orange juice'.
