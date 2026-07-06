class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        largest_i = 0
        largest_j = 0
        i = 0
        j = len(heights) - 1

        while i <= j:
            if heights[i] < largest_i: #Doesn't re-evaluate similar heights at smaller widths
                i += 1
                continue

            if heights[j] < largest_j:
                j -= 1
                continue

            area = abs(i - j) * min(heights[i],heights[j])
            print(area)
            max_area = max(area,max_area)

            if heights[i] < heights[j]:
                i += 1
                continue

            if heights[i] > heights[j]:
                j -= 1
                continue
            
            if heights[i] == heights[j]:
                i += 1
                j -= 1
                continue
        return max_area