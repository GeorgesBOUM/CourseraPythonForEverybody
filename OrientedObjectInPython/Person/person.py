#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:53:33 2020

@author: gregoire
"""


class Person:
    """This class defines a person, having the following attributes:
        - last_name
        - first_name
        - age
        - living_town"""

    def __init__(self):
        """the constructor"""
        self.last_name = "Dupont"
        self.first_name = "Jean"
        self.age = 33
        self.living_town = "Anglet"


print(dir(Person()))
