#!/usr/bin/env python
# coding: utf-8


import xodr_parser 
from lxml import etree
import matplotlib.pyplot as plt
import elements
from math import cos, sin, radians




class XodrViewer:
    def __init__(self, fpath: str):
        tree = etree.parse(fpath)
        root = tree.getroot()
        self.xodr = xodr_parser.parse_opendrive(root)
        #print(len(self.xodr.roads))
        for road in self.xodr.roads:
            for geometry in road.planView.get_geometries:
                if isinstance(geometry,elements.geometry.Line):
                    self.draw_line(geometry)

    @staticmethod 
    def draw_line(line: elements.geometry.Line):
        x,y = line.start_position
        length = line.length
        heading = line.heading
        print(length)
        end_x = x + length * cos(radians(heading))
        end_y = y + length * sin(radians(heading))
        plt.plot([x, end_x], [y, end_y], 'r-')
        
        


if __name__ == "__main__":
    # viewer = XodrViewer("./xodr/straight_500m.xodr")
    viewer1 = XodrViewer("./xodr/multi_intersections.xodr")
    plt.axis('equal')
    plt.show()