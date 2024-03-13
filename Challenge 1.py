import os
import time
from termcolor import colored

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]
    
    def hitshell(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] >= self._y
    
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark  # Corrected assignment operator
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Corrected clear command
    
    def print(self):
        self.clear()
        for row in self._canvas:  # Corrected variable name
            print(' '.join(row))  # Corrected variable name

    def drawSquare(self, size):
        # Draw the right side
        i = 0
        while i < size:
            self.setPos((i, 0), colored('-', 'red'))
            i += 1
        
        # Draw the bottom side
        i = 0
        while i < size:
            self.setPos((size - 1, i), colored('-', 'red'))
            i += 1
        
        # Draw the left side
        i = size - 1
        while i >= 0:
            self.setPos((i, size - 1), colored('-', 'red'))
            i -= 1
        
        # Draw the top side
        i = size - 1
        while i >= 0:
            self.setPos((0, i), colored('-', 'red'))
            i -= 1

# Testing the function
if __name__ == "__main__":
    scribe = Canvas(15, 15)  # Adjust the canvas size as needed
    scribe.drawSquare(10)
    scribe.print()
