#!/usr/bin/python3
# coding: utf-8

'''
 Name: Michael Young
 Email: michaelyangbo@outlook.com
 Date: 2019/2/9
 Ref.:  https://en.wikipedia.org/wiki/A*_search_algorithm
'''

from tkinter import *
from gameManager import *

def main():
    root = Tk()
    root.title("A Star")
    canvas = Canvas(root,width=500,height=500)
    canvas.pack()
    gameDataInit(canvas)
    root.resizable(0,0)
    root.mainloop()

if __name__ == '__main__':
    main()