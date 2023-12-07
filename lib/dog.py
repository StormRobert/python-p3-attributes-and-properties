#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name = 'Simba', breed = 'French Bulldog') -> None:
        self.name = name
        self.breed = breed

    def get_name(self):
        return self.name
        
    def set_name(self, name):
        if isinstance(name, str) and 0 < len(name) < 26:
            self.name = name
        else:
            print('Name must be string between 1 and 25 characters')
    name = property(get_name, set_name)
