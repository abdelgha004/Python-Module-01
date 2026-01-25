#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1


class FloweringPlant(Plant):
    def __init__(self, name, height, color=None, blooming=False):
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color=None, blooming=False,
                 prize_points=0):
        super().__init__(name, height, color, blooming)
        self.prize_points = prize_points


class GardenManager:
    total_managers = 0
    def __init__(self):
        self.gardens = []
        GardenManager.total_managers += 1

    class Garden:
        def __init__(self, owner):
            self.owner = owner
            self.plants = []
            self.total_growth = 0

        def add_plant(self, plant):
            self.plants.append(plant)
            print(f"Added {plant.name} to {self.owner}'s garden")

        def grow_all_plants(self):
            print(f"{self.owner} is helping all plants grow...")
            for plant in self.plants:
                plant.grow()
                self.total_growth += 1
                print(f"{plant.name} grew 1cm")

        def report(self):
            print(f"\n=== {self.owner}'s Garden Report ===")
            print("Plants in garden:")
            for plant in self.plants:
                line = f"- {plant.name}: {plant.height}cm"
                if isinstance(plant, FloweringPlant):
                    if plant.color:
                        line += f", {plant.color} flowers"
                    if plant.blooming:
                        line += " (blooming)"
                if isinstance(plant, PrizeFlower):
                    line += f", Prize points: {plant.prize_points}"
                print(line)
            stats = GardenManager.GardenStats(self)
            stats.count_plant_types()
            print(
                f"\nPlants added: {stats.total_plants},"
                f" Total growth: {self.total_growth}cm"
                )
            print(
                f"Plant types: {stats.regular} regular,"
                f" {stats.flowering} flowering, "
                f" {stats.prize} prize flowers"
                )
            stats.check_height_validity()
            print(f"Height validation test: {stats.height_validation}")

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def count_plant_types(self):
            self.regular = 0
            self.flowering = 0
            self.prize = 0
            self.total_plants = 0
            for plant in self.garden.plants:
                if isinstance(plant, PrizeFlower):
                    self.prize += 1
                elif isinstance(plant, FloweringPlant):
                    self.flowering += 1
                elif isinstance(plant, Plant):
                    self.regular += 1
                self.total_plants += 1

        def check_height_validity(self):
            self.height_validation = True
            for plant in self.garden.plants:
                if plant.height <= 0:
                    self.height_validation = False

    @classmethod
    def create_garden_network(cls):
        pass


if __name__ == "__main__":
    pass