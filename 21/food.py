from pprint import pprint
import re


def get_allergen_mapping(food, allergen_mapping):

    for i in range(len(allergen_mapping)):
        for allergen in allergen_mapping:
            food_with_allergen = [ingredients for ingredients, allergens in food if allergen in allergens]
            if not food_with_allergen:
                continue
            common = set.intersection(*food_with_allergen)
            if len(common) == 1:
                ingredient = list(common)[0]
                allergen_mapping[allergen] = ingredient
                for ingredients, allergens in food:
                    if ingredient in ingredients:
                        ingredients.remove(ingredient)
                        allergens.discard(allergen)


    without_allergens = []
    for ingredients, allergens in food:
        if allergens:
            raise RuntimeError('Not reduced')
        without_allergens.extend(ingredients)


    print(len(without_allergens))


def main():
    food = []
    allergen_mapping = {}
    with open('input.txt') as f:
        for line in f:
            ingredients = set()
            allergens = set()
            is_allergen = False
            for m in re.finditer('(\w+)', line):
                if m.group(1) == 'contains':
                    is_allergen = True
                    continue
                if is_allergen:
                    allergen_mapping[m.group(1)] = None
                    allergens.add(m.group(1))
                else:
                    ingredients.add(m.group(1))
            food.append((ingredients, allergens))

    get_allergen_mapping(food, allergen_mapping)

if __name__ == '__main__':
    main()
