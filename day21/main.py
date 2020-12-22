from utils import read_file, print_part_1, print_part_2, duplicates

# -- PARSE INPUT -- #
foods = []

for line in read_file('input.txt'):
    ingredients, allergens = line.split(' (contains ')
    foods.append({'ingredients': ingredients.split(' '), 'allergens': allergens[:-1].split(', ')})

# -- PART 1 -- #
possible_allergens = {}
for food in foods:
    ingredients, allergens = food['ingredients'], food['allergens']

    for allergen in allergens:
        if allergen in possible_allergens:
            possible_allergens[allergen] = list(duplicates(possible_allergens[allergen] + ingredients))
        else:
            possible_allergens[allergen] = ingredients

real_allergens = {}
while len(real_allergens) != len(possible_allergens):
    for allergen in possible_allergens:
        if len(possible_allergens[allergen]) == 1:
            real_allergens[allergen] = possible_allergens[allergen][0]
            break

    for j in possible_allergens:
        if real_allergens[allergen] in possible_allergens[j]:
            possible_allergens[j].remove(real_allergens[allergen])

allergens = list(real_allergens.values())
num_ingredients_without_allergens = 0
for food in foods:
    ingredients = food['ingredients']
    num_ingredients_without_allergens += sum([1 for ingredient in ingredients if ingredient not in allergens])

print_part_1(num_ingredients_without_allergens)
# -- PART 2 -- #
canonical_list = ''

for allergen in sorted(real_allergens):
    canonical_list += real_allergens[allergen] + ','
canonical_list = canonical_list[0:-1]

print_part_2(canonical_list)
