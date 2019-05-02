
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.


def display_inventory(inventory):
    '''Display the inventory like this:
    rope: 1
    torch: 6
    '''
    for item, count in inventory.items():
      print(f"{item}: {count}")


def add_to_inventory(inventory, added_items):
  for item in added_items:
    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1



def print_table(inventory, order=None):
    item_title = "item name"
    count_title = "count"
    separator = " | "
    dash_car = '-'
    
    max_width_item = max([len(str(item)) for item in inventory.keys()] + [len(item_title)])
    max_width_count = max([len(str(count)) for count in inventory.values()] + [len(count_title)])
    horizontal_line = dash_car * (max_width_count + max_width_item + len(separator))

    print(horizontal_line)
    print(f"{item_title:>{max_width_item}}{separator}{count_title:>{max_width_count}}")
    print(horizontal_line)

    inventory_items = []
    if order is "count,asc":
        inventory_items = sorted(inventory.items(), key=lambda items:items[1], reverse=False)
    elif order is "count,desc":
        inventory_items = sorted(inventory.items(), key=lambda items:items[1], reverse=True)
    else:
        inventory_items = inventory.items()

    for item, count in inventory_items:
        print(f"{item:>{max_width_item}}{separator}{count:>{max_width_count}}")

    print(horizontal_line)

    

def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    '''
    try:
      with open(filename) as file:
        for line in file:
          items_to_add = line.split(',')
          add_to_inventory(inventory, items_to_add)
    except FileNotFoundError:
      print(f"File '{filename}' not found!") 



def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''

    outputs = []

    for item, count in inventory.items():
      for i in range(count):
        outputs.append(item)
    
    outputs_with_commas = ",".join(outputs)

    try:
      with open(filename, "w")as file:
        file.write(outputs_with_commas)  
    except PermissionError:
      print(f"You don't have permission creating file '{filename}'!")
