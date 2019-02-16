#!/usr/bin/python3
# coding: utf-8

'''
 Name: Michael Young
 Email: michaelyangbo@outlook.com
 Date: 2019/2/16
'''

import networkx as nx
import matplotlib.pyplot as plt
import pylab
from threading import *

class XYZ(Thread):
    def __init__(self, val):
        self.val = val
        self.run()

    def run(self):
        self.DrawGraph(self.val)

    def DrawGraph(self,Data):

        n=0
        fig = plt.figure()

        # creating a timer object and setting an interval of 3000 milliseconds
        timer = fig.canvas.new_timer(interval=3000)
        timer.add_callback(self.close_event)

        #for m in range(len(Data)):
        #Data=2d ary
        g = nx.DiGraph()
        for i in range(len(Data[0])):
            for j in range(len(Data[0])):
                if Data[i][j]!=0:
                    g.add_edges_from([(str(i+n),str(j+n))],weight=Data[i][j])

            n=n+n
            edge_labels=dict([((u,v,),d['weight'])
                              for u,v,d in g.edges(data=True)])
            pos=nx.spring_layout(g)
            nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels)
            nx.draw(g,pos, node_color = 'yellow', node_size=1000,edge_color='black',edge_cmap=plt.cm.Reds,with_labels=True)
            plt.draw()
            timer.start()
            pylab.show()

    def close_event(self):

        # timer calls this function after 3 seconds and closes the window
        plt.close()

