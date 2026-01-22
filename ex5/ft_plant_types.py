#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, color: str):
        self.color = color
    
    def bloom():
        pass

class Tree(Plant):
    def __init__(self, trunk_diameter: int):
            self.trunk_diameter = trunk_diameter
        
    def produce_shade():
        pass
class Vegetable(Plant):
        def __init__(self, harvest_season: str, nutritional_value: str):
            self.harvest_season = harvest_season
            self.nutritional_value = nutritional_value