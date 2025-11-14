
fruits = ["Apple", "Banana", "Mango"]
vegetables = ["Tomato", "Carrot", "Spinach"]
beverages = ["Juice", "Soda", "Water"]
fruits.append("Orange")
vegetables.insert(1, "Potato")
beverages.pop()
inventory = [fruits, vegetables, beverages]
first_two_fruits = fruits[:2]
last_vegetable = vegetables[-1]
fruit_lengths = [len(item) for item in fruits]
is_water_available = "Water" in beverages
first_items_tuple = (fruits[0], vegetables[0], beverages[0])
print("Fruits:", fruits)
print("Vegetables:", vegetables)
print("Beverages:", beverages)
print("Inventory:", inventory)
print("First two fruits:", first_two_fruits)
print("Last vegetable:", last_vegetable)
print("Fruit lengths:", fruit_lengths)
print("Is 'Water' available?:", is_water_available)
print("Tuple of first items:", first_items_tuple)
