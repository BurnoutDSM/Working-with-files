from pprint import pprint

def make_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        for i in file:
            dush_name = i.strip()
            dush_count = int(file.readline())
            ingrids = []
            for i in range(dush_count):
                ingr = file.readline().split(' | ')
                ingredients = {'ingredient_name': ingr[0], 'quantity': int(ingr[1]), 'measure': ingr[2].strip()}
                ingrids.append(ingredients)
            cook_book[dush_name] = ingrids
            file.readline()
    return cook_book


pprint(make_cook_book('recipes.txt'), width=70)


def get_shop_list_by_dishes(dishes, person_count):
    recipes = make_cook_book('recipes.txt')
    count_ingredients = {}
    for dish in dishes:
        for dish_from_book in recipes.keys():
            if dish_from_book == dish:
                for ingred in recipes[dish]:
                    ingred['quantity'] = ingred['quantity'] * person_count
                    ingred_list = ingred.pop('ingredient_name')
                    count_ingredients[ingred_list] = ingred
    return count_ingredients

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), width=70)