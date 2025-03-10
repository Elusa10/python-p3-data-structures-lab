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
    """Return a list of names of spicy foods."""
    return [food["name"] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    """Return a list of the spiciest foods."""
    return [food for food in spicy_foods if food["heat_level"] > 5]
    pass

def print_spicy_foods(spicy_foods):
    """Print the names of spicy foods."""
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None
    pass

def print_spiciest_foods(spicy_foods):
    """Print the names of the spiciest foods."""
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_icons = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_icons}")
    pass

def get_average_heat_level(spicy_foods):
    """Return the average heat level of spicy foods."""
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    """Add a new spicy food to the list."""
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
