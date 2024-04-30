bowls = input()
bowls = list(bowls)
old_bowl = 0
bowl_height = 0

for bowl in bowls:
    if bowl != old_bowl:
        bowl_height += 10
    elif bowl == old_bowl:
        bowl_height +=5

    old_bowl = bowl

print(bowl_height)