# Create a shopping cart programme that will continuously ask the user for a product and the price of the product
# Add an exit clause if the user wishes to stop adding items to the cart
# At the end of shopping show the food items and the total cost to the user
# Step 1 declare the variable - food[list], quantity, price

items = []
prices = []
total = 0

#continuoulsy = loop

while True:
    item = input("Choose the item to add to your trolley or press 'q' to quit: ")
    if item.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price of the {item}: R"))
        items.append(item)
        prices.append(price)
                
print("----Your Cart----")    

for item in items:
    print(item, end= " ") 
    
for price in prices:
    total += price  
    
print("\n")
print(f"The total is: R{total}")     
        