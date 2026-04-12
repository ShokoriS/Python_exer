
def add_me_to_the_queue(express, normal, ticket_type, person_name):
    #express_ticket = 1, normal_ticket = 0
    #if the person has a ticket type of 1 put it in express list otherwise to normal list

    if tickit_type == 1:
        express.append(persone_name)
    else:
        normal.append(person)

def find_my_friend(queue, name):

    #return queue.index(name)
    
    dict_queue = {queue[i]:i for i in range(len(queue))}

    return dict_queue.get(name, None)

print(find_my_friend([ 'how', 'well'], 'hi'))

def add_me_with_my_friends(queue, index, person_name):

    #queue.insert(index, person_name)
    #return queue
    first_half = queue[:index]
    first_half.append(person_name)

    return first_half + queue[index:]
    

print(add_me_with_my_friends(["hi", 'how', 'are'], 2, 'which'))

from collections import defaultdict

def create_inventory(input_list):
    
    products = defaultdict(int)

    for product in input_list:
        products[product] += 1

    return dict(products)


print(create_inventory(["coal", "wood", "wood", "diamond"]))

def add_items(inventory_dict, item_list):
    
    for product in item_list:
        inventory_dict[product] = inventory_dict.get(product, 0) + 1
    return inventory_dict

print(add_items({'coal':1},['wood', 'iron', 'coal', 'wood']))

def decrement_items(inventory_dict, items_list):

    for product in items_list:
        if inventory_dict.get(product, 0) > 0:
            inventory_dict[product] -= 1
    return inventory_dict
print(decrement_items({'coal': 2, 'wood': 2, 'iron': 1}, ['wood', 'iron', 'coal', 'wood']))

def remove_item(inventory_dict, item):
    
    if item in inventory_dict:
        inventory_dict.pop(item)
        
    return inventory_dict

print(remove_item({'coal': 2, 'wood': 2, 'iron': 1}, 'coal'))


def list_inventory(inventory_dict):

    return [(key, value) for key,value in inventory_dict.items() if value > 0]
print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))


#=====================================dict methods=============================

def updated_recipe(ideas, recipe_updates):

    

    for recipe_name, recipe_data in recipe_updates:
        ideas[recipe_name] = recipe_data

    return ideas




print(updated_recipe(
    {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
     'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
    (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),)
    )=={'Banana Bread': {'Banana': 4, 'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}, 
 'Raspberry Pie': {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}})


def sorted_cart(cart):
    return dict(sorted(cart.items()))

print(sorted_cart({'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}))


def update_store_inventory(fulfillment_cart, store_inventory):

    updated_inventory = {}
    for product_name, quantity in fulfillment_cart.items():
        new_data = [quantity]
        new_data.extend(store_inventory[product_name])
        updated_inventory[product_name] = new_data

    return dict(sorted(updated_inventory.items(), reverse=True))

print(update_store_inventory({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
                  {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}))


def update_store_inventory(fulfillment_cart, store_inventory):
    
    updated_inventory = {}

    for product_name, product_info in store_inventory.items():

        store_quantity = product_info[0]
        cart_product_quantity = fulfillment_cart[product_name][0]
        updated_quantity = (store_quantity - cart_product_quantity) 
        updated_inventory[product_name] = [updated_quantity if updated_quantity > 0 else "Out of Stock"] + product_info[1:]

    return updated_inventory

print(update_store_inventory({'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
{'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}))



fruits_vegetables = [["apple", "banana"], ["carrot", "potato"]]

for [first, second] in fruits_vegetables:
    print(first, second)

zipped = zip(*fruits_vegetables)
print(*zipped)

"""The program for solving the hay, sheep, wolf problem; I am going to do it again and write it again, but this time
I am gonna write it more clean....
The farmer is player, and he is the one the player can control only, that moves to two sides of the river....We will indicate which side he is currently on...
But first we will create rules, as the wolf and the sheep can't be left alone, and the sheep and they hay"""

# The rules
rules = [('wolf', 'sheep'), ('sheep', 'hay')]

# now we will define the two sides of the river as well as the side of the river...
right_side = {'wolf', 'sheep', 'hay'}
left_side = set()
farmer_side = 'right'

# now we define the movements of the farmer

def move(input_data):
    global farmer_side 
    input_data = input_data.lower().strip()
    if input_data in right_side and farmer_side == 'right':
        right_side.remove(input_data)
        left_side.add(input_data)
        farmer_side = 'left'
        

    elif input_data in left_side and farmer_side == 'left':
        left_side.remove(input_data)
        right_side.add(input_data)
        farmer_side = 'right'

    elif input_data == "":
        farmer_side = 'right' if farmer_side == 'left' else 'left'

    else:
        return "wrong move, try again..."

# here we check if the the player has won or lost?
def check_rules(input_data):
    global farmer_side, right_side, left_side, rules
    if len(right_side) < 3 or len(left_side) < 3:
        for rule in rules:
            if rule[0] in right_side and rule[1] in right_side and farmer_side == 'left':
                return f"Game over...You can't leave {rule[0]} and {rule[1]} alone..."
            elif rule[0] in left_side and rule[1] in left_side and farmer_side == 'right':
                return f"Game over....You can't leave {rule[0]} and {rule[1]} alone...."
    if len(left_side) > 2:
        return "Congrats you have won the game....."
    else:
        return None

def main():
    global right_side, left_side, farmer_side
    while True:
        print("right_side:", right_side)
        print("left_side:", left_side)
        print("farmer_side:", farmer_side)
        input_data = input("which one do you want to move wolf/sheep/hay?")
        wrong_move = move(input_data)
        if wrong_move:
            print(wrong_move)
            break
        checked_rule = check_rules(input_data)
        if checked_rule is not None:
            print(checked_rule)
            break

print("There is a formar that wants to travle to the other side of the river but he has a sheep, a wolf and hay.... Though he can't leave the hay with the sheep and the sheep with the wolf...It is a narrow boat so he can only take one...What do you think he should do?")





def get_list_of_wagons(*args):
    [*combined] = args

    return combined

def fix_list_of_wagons(wagons_id, missing_wagons):

    first, second, third, *rest = wagons_id
    [*combined] = third, *missing_wagons, *rest, first, second
    return combined

def add_missing_stops(data, **stops):
    
    
    data['stops'] = [*stops.values()]
    return data


print(add_missing_stops({"from": "New York", "to": "Miami"},
                      stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
                      stop_4="Jacksonville", stop_5="Orlando"))


def extend_route_information(route, more_route_info):

    return {**route, **more_route_info}

print(extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"}))

"""fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red")],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                    ])

[
[(2, "red"), (5, "blue"), (3, "orange")],
[(4, "red"), (9, "blue"), (7, "orange")],
[(8, "red"), (13,"blue"), (11, "orange")]
]"""

def fix_wagon_depot(wagons_rows):
        

    return [list(row) for row in zip(*wagons_rows)] 
for each in fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red"), (15, 'red')],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                    ]):
    print(each)



def clean_ingredients(dish_name, dish_ingredients):

    return dish_name, set().union(dish_ingredients)

res = clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro'])

print(res)


print(sorted( ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro']) == sorted(list(res[1])))


set1 = {'cow', 'dog', 'cat'}
set2 = {'monkey', 'donkey', 'pigeon', 'cow'}

print(set1.isdisjoint(set2))
print(set1.intersection(set2))

new_set = set()

dishes = [ {'tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'},
           {'pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts',
           'balsamic vinegar', 'onions', 'black pepper'},
           {'honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'}]
appetizers = ['Kingfish Lettuce Cups','Avocado Deviled Eggs','Satay Steak Skewers',
              'Dahi Puri with Black Chickpeas','Avocado Deviled Eggs','Asparagus Puffs',
              'Asparagus Puffs']

dishes =    ['Avocado Deviled Eggs','Flank Steak with Chimichurri and Asparagus', 'Kingfish Lettuce Cups',
             'Grilled Flank Steak with Caesar Salad','Vegetarian Khoresh Bademjan','Avocado Deviled Eggs',
             'Barley Risotto','Kingfish Lettuce Cups']
          

both = set(dishes).union(set(appetizers))
print(both.difference(set(appetizers)))


Vegan = {"hi" ,'ho', 'hao'}




dishes = [
    {"tomato", "salt", "pepper"},
    {"salt", "chicken"},
    {"pepper", "rice"}
]

all_dishes = set()
for dish in dishes:
    all_dishes = all_dishes.union(dish)



first = all_dishes
print(first)
second = {"tomato", "chicken", "rice"}

print(first.difference(second))
