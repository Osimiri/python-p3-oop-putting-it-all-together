#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size = 0):
        self.brand = brand 
        self.size = size
    
    # def get_color(self):
    #     return self.color

    def set_color(self, color):
        self.color = color

    def get_size(self):
        return self._size

    def set_size(self, size):
        if type(size) == int:
            self._size = size 
        else:
            print("size must be an integer")
    
    size = property(get_size, set_size)  #getter setter the deleter 

    def get_material(self):
        return self._material
    
    def get_condition(self):
        return self._condition
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
    



  