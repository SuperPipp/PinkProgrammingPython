def test_recipe(food_1, food_2):
    return ("How about some " + food_1+ " a la " + food_2)
food_1 = 'Creme'
food_2 = 'Strawberry'
food_combo = test_recipe(food_1, food_2)
print(food_combo)