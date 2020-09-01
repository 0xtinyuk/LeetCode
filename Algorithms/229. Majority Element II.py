class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        can1 = -1234567
        can2 = -1234567
        for i in nums:
            if (i == can1) or (i == can2):
                if(i == can1):
                    count1 += 1
                else:
                    count2 += 1
            else:
                if(count1 == 0):
                    can1 = i
                    count1 = 1
                elif count2 == 0:
                    can2 = i
                    count2 = 1
                else:
                    count1 -= 1
                    count2 -= 1

        count1 = count2 = 0
        for i in nums:
            if i == can1:
                count1 += 1
            if i == can2:
                count2 += 1
        res = []
        if count1 > len(nums)//3:
            res.append(can1)
        if count2 > len(nums)//3:
            res.append(can2)
        return res
