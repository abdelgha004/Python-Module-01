#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)
    garden_plants = [plant_1, plant_2, plant_3]
    print("=== Garden Plant Registry ===")
    for plant in garden_plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
