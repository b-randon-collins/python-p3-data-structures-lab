spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    list = [food["name"] for food in spicy_foods]
    print(list)
    return list
    
# get_names(spicy_foods)
# => ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

def get_spiciest_foods(spicy_foods):
    list = [food for food in spicy_foods if food["heat_level"] > 5]
    print(list)
    return list
    

# get_spiciest_foods(spicy_foods)
# => [{"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}, {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}]


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
        
# print_spicy_foods(spicy_foods)
# => Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# => Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# => Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            print(food)
            return food
    return None

    
# get_spicy_food_by_cuisine(spicy_foods, "American")
# # => {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}

# get_spicy_food_by_cuisine(spicy_foods, "Thai")
# # => {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
    pass


# print_spiciest_foods(spicy_foods)
# => Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# => Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶


def get_average_heat_level(spicy_foods):
    list = sum(food["heat_level"] for food in spicy_foods) / len(spicy_foods)

    print(list)
    return list        

# get_average_heat_level(spicy_foods)
# => 6

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)

    print(spicy_foods)
    return spicy_foods


create_spicy_food(
    spicy_foods,
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
)

# => [
# =>     {
# =>         "name": "Green Curry",
# =>         "cuisine": "Thai",
# =>         "heat_level": 9,
# =>     },
# =>     {
# =>         "name": "Buffalo Wings",
# =>         "cuisine": "American",
# =>         "heat_level": 3,
# =>     },
# =>     {
# =>         "name": "Mapo Tofu",
# =>         "cuisine": "Sichuan",
# =>         "heat_level": 6,
# =>     },
# =>     {
# =>         'name': 'Griot',
# =>         'cuisine': 'Haitian',
# =>         'heat_level': 10,
# =>     },
# => ]