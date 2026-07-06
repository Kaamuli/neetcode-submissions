class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def merge_sort(arr):
            if len(arr) == 1:
                return arr

            if len(arr) > 1:
                left_arr = arr[len(arr)//2:]
                right_arr = arr[:len(arr)//2]

                #recursion
                merge_sort(left_arr)
                merge_sort(right_arr)

                #merging

                i = 0 #pointer of left array
                j = 0 #pointer of right array
                k = 0 #pointer of merged array

                while i < len(left_arr) and j < len(right_arr):
                    if left_arr[i] < right_arr[j]:
                        arr[k] = left_arr[i]
                        i += 1
                        k += 1
                    else:
                        arr[k] = right_arr[j]
                        j += 1
                        k += 1

                while i < len(left_arr):
                    arr[k] = left_arr[i]
                    i += 1
                    k += 1

                while j < len(right_arr):
                    arr[k] = right_arr[j]
                    j += 1
                    k += 1
            return arr
        return merge_sort(nums)
        