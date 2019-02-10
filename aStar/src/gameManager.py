#!/usr/bin/python3
# coding: utf-8

'''
 Name: Michael Young
 Email: michaelyangbo@outlook.com
 Date: 2019/2/9
'''

from block import *
from game import *

blockArray = []
pathBlocks = []

def gameDataInit(canvas):
    canvas.bind("<Button-1>", cnvClick)
    displyLocationX = 50
    displyLocationY = 50
    width = 40
    for r in range(0,10):
        for c in range(0,10):
            block = Block(displyLocationX+c*width,displyLocationY+r*width,width)
            block.rowIndex = r
            block.columnIndex = c
            blockArray.append(block)
    drawBlocks(canvas)

def drawBlocks(canvas):
    for block in blockArray:
        block.draw(canvas)

def cnvClick(event):
    for b in pathBlocks:
        b.state = blockState[1]
        b.draw(event.widget)
    pathBlocks.clear()
    block = pickBlock(event.x,event.y)
    if block != None:
        if block.state == blockState[2]:
            block.state = blockState[1]
        else:
            block.state = blockState[2]
        block.draw(event.widget)

    aStarAlgorithm(blockArray,pathBlocks)
    for block in pathBlocks:
        block.draw(event.widget)

def pickBlock(x,y):
    for block in blockArray:
        if block.pick(x,y):
            return block
