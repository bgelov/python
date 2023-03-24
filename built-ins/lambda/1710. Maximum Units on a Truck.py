# https://leetcode.com/problems/maximum-units-on-a-truck
# Oleg Belov

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units = 0
        for box_t in boxTypes:
            if box_t[0] <= truckSize:
                truckSize -= box_t[0]
                units += box_t[0] * box_t[1]
            else:
                units += truckSize * box_t[1]
                break
        return units