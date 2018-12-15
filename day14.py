from tqdm import tqdm
import sys

recipe_ticks = 209231
checker = str(recipe_ticks)

recipes = [3, 7]

elf_one = 0
elf_two = 1

part1 = True

pbar = tqdm()

while True:
    pbar.update(1)
    if part1 and len(recipes) > recipe_ticks + 10:
        tqdm.write("Part 1: " + "".join([str(x) for x in recipes[recipe_ticks:recipe_ticks+10]]))
        part1 = False

    recipe_sum = recipes[elf_one] + recipes[elf_two]
    
    for char in str(recipe_sum):
        recipes.append(int(char))
        if "".join([str(x) for x in recipes[-(len(checker)):]]) == checker:
            tqdm.write(f"Part 2: {len(recipes)-len(checker)}")
            sys.exit()
    
    elf_one += 1 + recipes[elf_one]
    elf_two += 1 + recipes[elf_two]

    elf_one = elf_one % len(recipes)
    elf_two = elf_two % len(recipes)

    