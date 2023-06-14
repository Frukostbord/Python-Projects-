import random
world = {(w,h) for w in range(0, 11) for h in range(0, 11) if random.randint(1, 10) <= 3}


print(world)