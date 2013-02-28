# answer 1
dairy_section = ["milk", "cottage cheese", "butter", "yogurt"]

# answer 2
print("First:%s and Last: %s" % (dairy_section[0], dairy_section[-1]))
# result First:milk and Last: yogurt

# answer 3
milk_expiration = ("2013", "02", "15")

# answer 4
print("This milk carton will expire on %s/%s/%s" % (milk_expiration[1], milk_expiration[2], milk_expiration[0]))

# answer 5
milk_carton = {}
milk_carton["Expiration_date"] = milk_expiration
milk_carton["fl_oz"] = 32
milk_carton["cost"] = 2.50
milk_carton["band_name"] = "Milk"

# answer 6
print("The Expiration date was %s/%s/%s." % (milk_carton["Expiration_date"][1], milk_carton["Expiration_date"][2],
      milk_carton["Expiration_date"][0]))

# answer 7
print("The cost for 6 carton of milk is %0.02f" % (milk_carton["cost"] * 6))

# answer 8
cheese = ["cheddar", "american", "mozzarella"]
print(cheese)
# result ['cheddar', 'american', 'mozzarella']
# method 1
dairy_section.extend(cheese)
print(dairy_section)
# result ['milk', 'cottage cheese', 'butter', 'yogurt', 'cheddar', 'american', 'mozzarella']
dairy_section.pop()
dairy_section.pop()
dairy_section.pop()
print(dairy_section)
# result ['milk', 'cottage cheese', 'butter', 'yogurt']
# method 2
dairy_section.append(cheese)
print(dairy_section)
# result ['milk', 'cottage cheese', 'butter', 'yogurt', ['cheddar', 'american', 'mozzarella']]
dairy_section.pop()
print(dairy_section)
# result ['milk', 'cottage cheese', 'butter', 'yogurt']

# answer 9
print(len(cheese))

# answer 10
print("First five letters of %s is %s." % (cheese[0], cheese[0][0:5]))
