#!/usr/bin/python3
import abc


class Animal(abc.ABC):
    """Abstract base class representing an animal."""

    @abc.abstractmethod
    def sound(self):
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """Dog subclass that implements the sound method."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat subclass that implements the sound method."""

    def sound(self):
        return "Meow"



if __name__ == "__main__":
    bobby = Dog()
    garfield = Cat()

    print(bobby.sound())
    print(garfield.sound())
