import random
import colorama
import time
import sys

from colorama import Fore, Style

class Person:
    """
    A class to represent a person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        gender (str): The gender of the person.
        color (str): The color used for the person's introduction (randomly selected).
    """

    def __init__(self, name, age, gender):
        """
        Initializes a Person object with the provided name, age, and gender.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            gender (str): The gender of the person.
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.color = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])

    def introduce(self):
        """
        Introduces the person with their name, age, and gender using colorful text.

        Prints:
            The introduction of the person with colored text.
        """
        introduction = f"{self.color}Hello, my name is {self.name}. I am {self.age} years old, and I am a {self.gender}."
        print(introduction + Style.RESET_ALL)

if __name__ == "__main__":
    colorama.init()

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")

    person = Person(name, age, gender)

    print("Getting ready to introduce you...")
    for _ in range(3):
        print(Fore.YELLOW + "." + Style.RESET_ALL, end=" ", flush=True)
        time.sleep(0.5)

    print()
    person.introduce()
