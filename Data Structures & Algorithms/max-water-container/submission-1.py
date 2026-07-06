class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        i = 0
        j = len(heights) - 1

        while i <= j:

            area = abs(i - j) * min(heights[i],heights[j])
            print(area)
            max_area = max(area,max_area)

            if heights[i] < heights[j]:
                old_left_height = heights[i]

                i += 1

                while i < j and heights[i] <= old_left_height:
                    i += 1
                continue

            if heights[i] > heights[j]:
                old_right_height = heights[j]

                j -= 1

                while i < j and heights[j] <= old_right_height:
                    j -= 1
                continue
            
            if heights[i] == heights[j]:
                i += 1
                j -= 1
                continue
        return max_area

            