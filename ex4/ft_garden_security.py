#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, new_height: int):
        if new_height > 0:
            self.__height = new_height
        else:
            print(
                "\nInvalid operation attempted: "
                f"height {new_height}cm [REJECTED]"
                )
            print("Security: Negative height rejected")

    def set_age(self, new_age: int):
        if new_age > 0:
            self.__age = new_age
        else:
            print(
                "\nInvalid operation attempted: "
                f"age {new_age} days [REJECTED]"
            )
            print("Security: Negative age rejected")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_info(self):
        print(
            f"\nCurrent plant: {self.name} "
            f"({self.__height}cm, {self.__age} days)"
        )


if __name__ == "__main__":
    rose = SecurePlant("Rose", 15, 20)
    rose.set_height(25)
    rose.set_age(30)

    print("=== Garden Security System ===")
    print(f"Plant created: {rose.name}")
    print(f"Height updated: {rose.get_height()}cm [OK]")
    print(f"Age updated: {rose.get_age()} days [OK]")
    rose.set_height(-5)
    rose.get_info()
