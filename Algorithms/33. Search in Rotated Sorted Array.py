class Solution:

    def search(self, nums: List[int], target: int) -> int:
        return self.searchOnly(nums, target, 0, len(nums)-1)

    def searchOnly(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l == r:
            if nums[l] == target:
                return l
            else:
                return -1
        if l > r:
            return -1
        ans = self.searchAndCheck(nums, target, l, r, -1, 0, l, r)
        if ans == -3 or ans == -2:
            if ans == -3:
                ans = self.searchOnly(
                    nums, target, (l+r)//2+1, r)
            if ans == -2:
                ans = self.searchOnly(
                    nums, target, l, (l+r)//2-1)
        if ans == -3 or ans == -2:
            return -1
        return ans

    def searchAndCheck(self, nums: List[int], target: int, l: int, r: int, last: int, bigger: int, ll: int, rr: int) -> int:
        print(l,r)
        if l == r:
            if nums[l] == target:
                return l
            else:
                if l == ll:
                    return -3
                if l == rr:
                    return -2
                return -1
        if l > r:
            if l == ll:
                return -3
            return -1
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        if (bigger == 1) and (nums[mid] < last):
            return self.searchAndCheck(nums, target, l, mid-1, last, 1, ll, rr)
        if (bigger == -1) and (nums[mid] > last):
            return self.searchAndCheck(nums, target, mid+1, r, last, -1, ll, rr)

        if nums[mid] < target:
            return self.searchAndCheck(nums, target, mid+1, r, nums[mid], 1, ll, rr)
        else:
            return self.searchAndCheck(nums, target, l, mid-1, nums[mid], -1, ll, rr)
