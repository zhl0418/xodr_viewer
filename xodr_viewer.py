#!/usr/bin/env python
# coding: utf-8


import xodr_parser 
from lxml import etree
import matplotlib.pyplot as plt




class XodrViewer:
    def __init__(self, fpath: str):
        tree = etree.parse(fpath)
        root = tree.getroot()
        self.xodr = xodr_parser.parse_opendrive(root)
        print(len(self.xodr.roads))
        


if __name__ == "__main__":
    # viewer = XodrViewer("./xodr/straight_500m.xodr")
    viewer1 = XodrViewer("./xodr/multi_intersections.xodr")
