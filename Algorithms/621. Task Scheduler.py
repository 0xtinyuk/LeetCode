class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task = {}
        cd = {}
        for i in tasks:
            if i in task:
                task[i] += 1
            else:
                task[i] = 1
                cd[i] = 0

        ans = 0
        mark = True
        while mark:
            maxKey = ''
            maxValue = 0
            mark = False
            for x in task.keys():
                if task[x] > 0:
                    if not mark:
                        mark = True
                    if cd[x] == 0:
                        if task[x] > maxValue:
                            maxValue = task[x]
                            maxKey = x
                    else:
                        cd[x] -= 1
            if mark:
                ans += 1
                if maxValue == 0:
                    pass
                else:
                    task[maxKey] -= 1
                    cd[maxKey] = n

        return ans
