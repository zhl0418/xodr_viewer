from elements.roadLanes import Lanes, LaneSection
from elements.road import Road

class DrawLaneSection():
    def __init__(self, laneSection:LaneSection):
        self._lane_section = laneSection

    def Draw(self):
        # get reference from road based on s-coordinate of start position
        _road:Road = self._lane_section.parentRoad
        s0 = self._lane_section.s0
        if self._lane_section.successor() != None:
            s1 = self._lane_section
        else:
            s1 = _road.planView.length
        # TODO: get linear space s0 to s1 
        ls = self._lane_section.successor()
        print(f"self id {id(self._lane_section)} {self._lane_section.idx}")
        if ls != None:
            print(f"{id(ls)} {ls.idx}")
