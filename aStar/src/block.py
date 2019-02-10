#!/usr/bin/python3
# coding: utf-8

'''
 Name: Michael Young
 Email: michaelyangbo@outlook.com
 Date: 2019/2/9
'''

blockState = [0, 1, 2]


class Block(object):
    def __init__(self, locationX, locationY, width):
        self.rowIndex = 0
        self.columnIndex = 0
        self.state = 1
        self.g = 0
        self.locationX = locationX
        self.locationY = locationY
        self.width = width
        self.parent = None
        self.fillColor = "white"

    @property
    def h(self):
        return (10 - self.rowIndex + 10 - self.columnIndex) * self.width

    @property
    def f(self):
        return self.h + self.g

    def draw(self, canvas):
        if self.state == blockState[0]:
            self.fillColor = "red"
        elif self.state == blockState[1]:
            self.fillColor = "white"
        elif self.state == blockState[2]:
            self.fillColor = "blue"
        canvas.create_rectangle(self.locationX, self.locationY, self.locationX + self.width,
                                self.locationY + self.width, fill=self.fillColor, width="1")

    def pick(self, x, y):
        if x <= self.locationX + self.width and x >= self.locationX and y <= self.locationY + self.width and y >= self.locationY:
            return True
        return False