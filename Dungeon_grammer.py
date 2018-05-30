import random

dungeon = ["obstacle", "treasure"]

def generate_obstacle():
    return [["key", "obstacle","lock","obstacle"],["monster","obstacle"],["room"]][random.randint(0,2)]

def process_dungeon(dungeon):
    new_dungeon = []
    for i in range(len(dungeon)):
        if dungeon[i] == "obstacle":
            generated_obstacle = generate_obstacle()
            for element in generated_obstacle:
                new_dungeon += [element]
        else:
            new_dungeon += [dungeon[i]]
    return new_dungeon

while "obstacle" in dungeon:
    dungeon = process_dungeon(dungeon)

print dungeon

#for i in range(1000):
#    results[random.randint(1,5)-1] += 1

#print results
