#!/usr/bin/env python3

class Plant:
    """
    A simple data model for a garden plant.

    This class represents a plant by storing its basic properties:
    name, height in centimeters, and age in days.
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height of the plant in centimeters.
            age (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age
        self.weekly_growth = 0
        self.days = 1

    def grow(self):
        self.height += 1
        self.weekly_growth += 1

    def age_up(self):
        self.age += 1
        self.days += 1

    def get_info(self):
        print(f"=== Day {self.days} ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    rose.get_info()
    for _ in range(6):
        rose.grow()
        rose.age_up()
    rose.get_info()
    print(f"Growth this week: +{rose.weekly_growth}cm")
