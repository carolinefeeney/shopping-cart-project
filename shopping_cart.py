# shopping_cart.py


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# TODO: write some Python code here to produce the desired functionality...

#print(products)

#
# INFO CAPTURE / INPUT
#


total_price = 0
selected_ids = []

while True:
    selected_id = input("Please input a product identifier: ") #> "9" (string)
    # print(selected_id)
    # print(type(selected_id))
    #> "DONE"
    if selected_id == "DONE":
        break
    else:
        #matching_products = [p for p in products if str(p["id"]) == str(selected_id)] #> need to make sure that datatypes are the same when using == (str)
        #matching_product = matching_products[0]
        #total_price = total_price + matching_product["price"]
        #print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"])) #> remember to convert numbers to strings when concatenating them
        selected_ids.append(selected_id)

#
# INFO DISPLAY / OUTPUT
#

import datetime
now = datetime.datetime.strptime(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
#datetime.datetime.now()

print("---------------------------------")
print("FEENEY MART")
print("---------------------------------")
print("Phone:   908-499-8986")
print("Web:     www.feeney-mart.com")
print("Address: 3700 O Street NW ")
print("         Washington, D.C. 20057")
print("---------------------------------")
print("Checkout Time: "+ (str(now))) #TODO make more human friendly!
print("---------------------------------")
print("Shopping Cart Items:")
#print(selected_ids)




for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)] #> need to make sure that datatypes are the same when using == (str)
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    matching_product_usd = "${0:.2f}".format(matching_product["price"])
    print(" +" + " " + matching_product["name"] + " (" + str(matching_product_usd) + ")") #> remember to convert numbers to strings when concatenating them

#TODO format as USD!
#print_usd = "${0:.2f}".format(p["price"])
    #print(" + " + p["name"] + " (" + str(print_usd) + ")")

total_price_usd = "${0:.2f}".format(total_price) 
print("Subtotal: " + str(total_price_usd)) 
tax = total_price * (.06)
tax_usd = "${0:.2f}".format(tax)
print("Plus DC Sales Tax (6%): " + str(tax_usd)) 
end_total = total_price + tax
end_total_usd =  "${0:.2f}".format(end_total) 
print("Total: " + str(end_total_usd))
print("---------------------------------")
print("Thanks for shopping with us! Please come again soon.")

