class Solution:
    def findFloor(self, arr, x):
        low = 0
        high = len(arr) - 1
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] <= x:
                ans = arr[mid]
                low = mid + 1
            else:
                high = mid - 1

        return ans