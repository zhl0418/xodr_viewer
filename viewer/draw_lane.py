from elements.roadLanes import Lanes, LaneSection


class DrawLaneSection():
    def __init__(self, laneSection):
        self._lane_section = laneSection

    def Draw(self):
        # get reference from road based on s-coordinate of start position
        ls = self._lane_section.successor()
        print(f"self id {id(self._lane_section)} {self._lane_section.idx}")
        if ls != None:
            print(f"{id(ls)} {ls.idx}")
