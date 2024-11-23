# Welcome to dice rolling example first
import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print("(",dice1,",",dice2,")",sep="")

# Welcome to dice rolling example 2
# alternate version
import random
values = []
for _ in range(2):
    rolls = random.randint(1,6)
    values.append(rolls)
one,two = values
print(f"({one},{two})")

