inventory = []

def add_item(x):
    inventory.append(x)

def count_items(items):
    if len(items) == 0:  
        return 0  
    else:
        return 1 + count_items(items[1:])  

show_item = lambda item: print(f"Item in Stock: {item}")

def main():

    add_item("Dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    print(inventory)

    for item in inventory:
        show_item(item)

    total = count_items(inventory)
    print(f"\nTotal number of items: {total}")   


main()