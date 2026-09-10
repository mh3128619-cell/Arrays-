class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        max_area = 0

        for i in range(n):
            min_height = heights[i]

            for j in range(i, n):
                min_height = min(min_height, heights[j])

                width = j - i + 1

                area = min_height * width

                max_area = max(max_area, area)

        return max_area
