# Food Chain Game Using Python - www.101computing.net/food-chain-game-using-python/
import random
import find_path
organisms = ["grass", "insect", "rabbit", "slug", "frog", "vole", "thrush", "fox", "hawk"]
organismsLength = len(organisms)

# Select organism for player
playerPosition = random.randint(0, organismsLength - 1)
playerOrganism = organisms[playerPosition]
print("Player Organism: " + playerOrganism)

# Select organism for computer
computerPosition = random.randint(0, organismsLength - 1)
# Ensure that the computer organism will be different from the player organism
while computerPosition == playerPosition:
    computerPosition = random.randint(0, organismsLength - 1)

computerOrganism = organisms[computerPosition]
print("Computer Organism: " + computerOrganism)

foodWeb = {'insect': ['grass'],
           'rabbit': ['grass'],
           'slug': ['grass'],
           'thrush': ['slug', 'insect'],
           'vole': ['insect'],
           'frog': ['insect'],
           'hawk': ['frog', 'vole', 'thrush'],
           'fox': ['rabbit', 'frog', 'vole']}

# Complete code here to find out if the computer organism and the player organism are linked (Direct link or indirect
# link) If a link is detected decide who between the computer and the player wins the game
link1 = find_path.main(playerOrganism, computerOrganism, foodWeb)
link2 = find_path.main(computerOrganism, playerOrganism, foodWeb)
print(link1, link2)
