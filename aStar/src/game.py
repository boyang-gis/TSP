#!/usr/bin/python3
# coding: utf-8

'''
 Name: Michael Young
 Email: michaelyangbo@outlook.com
 Date: 2019/2/9
'''

import sys
from block import *

openList = []
closeList = []
pathList = []

def init():
    openList.clear()
    closeList.clear()
    pathList.clear()

def aStarAlgorithm(blockArray,pathBlocks):
    init()

	#The starting point is the first square and the ending point is the last square
    openList.append(blockArray[0])
    blockArray[0].g = 0

    loop(blockArray)
    for b in pathList:
        pathBlocks.append(b)

def loop(blockArray):
    selectBlock = None
    minF = sys.maxsize
    for b in openList:
        if b.f < minF:
            selectBlock = b
            minF = selectBlock.f

    openList.remove(selectBlock)
    closeList.append(selectBlock)

    adjacentBlocks = getAdjacentBlocks(selectBlock,blockArray)
    for b in adjacentBlocks:
        if b in closeList or b.state == blockState[2]:
            continue
        if b not in openList:
            openList.append(b)
            b.parent = selectBlock
            b.g = selectBlock.g + selectBlock.width
            if b.rowIndex == 9 and b.columnIndex == 9:
                createPath(b)
                return
        else:
            if b.g > selectBlock.g + selectBlock.width:
                b.parent = selectBlock
                b.g = selectBlock.g + selectBlock.width
    if len(pathList) != 0 or len(openList) == 0:
        return
    loop(blockArray)

def createPath(block):
    block.state = blockState[0]
    pathList.append(block)
    if block.parent != None:
        createPath(block.parent)

def getAdjacentBlocks(block,blockArray):
    blockList = []
    for b in blockArray:
        if b.rowIndex == block.rowIndex - 1 and b.columnIndex == block.columnIndex \
        or b.rowIndex == block.rowIndex+1 and b.columnIndex == block.columnIndex \
        or b.rowIndex == block.rowIndex and b.columnIndex == block.columnIndex-1 \
		or b.rowIndex == block.rowIndex and b.columnIndex == block.columnIndex+1:
            blockList.append(b)
    return blockList