from math import pi, atan2
class Solution(object):
    def visiblePoints(self, points, angle, location):
        x0, y0 = location
        angle *= pi / 180
        angles = sorted([atan2(x - x0, y - y0) for x, y in points if x != x0 or y != y0])
        n = len(angles)
        angles += [2 * pi + a for a in angles]
        left = right = max_visible_points = 0
        while left < n:
            while right < 2 * n and angles[right] - angles[left] <= angle:
                right += 1
            max_visible_points = max(max_visible_points, right - left)
            while left < n and angles[right] - angles[left] > angle:
                left += 1
        return max_visible_points + len(points) - n
