#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.weekly_growth = 0
        self.days = 1

    def grow(self):
        self.height += 1

    def age_up(self):
        self.age += 1
        self.days += 1

    def get_info(self):
        print(f"=== Day {self.days} ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Cactus", 5, 90)
    ]
    for plant in plants:
        plant.get_info()
        for i in range(6):
            plant.grow()
            plant.age_up()
        plant.get_info()
        print(f"Growth this week: +{i + 1}cm")
        print("-------------------")
