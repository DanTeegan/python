
fighters = {"name": "Jon Jones",
          "profession": "fighter",
          "number of fights": 22,
          "styles": ["Boxing", "Muay thai", "BJJ", "Wrestling"]
          }


print(fighters)

print(fighters.keys())

print(fighters.values())
fighters.update({"num losses": 0})

fighters["styles"].append("Wrestling")


print(fighters.values())
print(fighters.values())

for fighter in fighters:
    print(fighter, ":", fighters[fighter])