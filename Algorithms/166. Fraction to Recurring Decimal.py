class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        negative = False
        if numerator<0:
            negative = not negative
            numerator = -numerator
        if denominator<0:
            negative = not negative
            denominator = -denominator
        memory = {}
        i = numerator // denominator
        remainder = numerator-(denominator*i)
        if remainder ==0:
            if negative:
                return str(-i)
            return str(i)
        r = []
        memory[remainder]=0
        remainder*=10
        while remainder:
            while remainder<denominator:
                remainder *=10
                r.append(0)
            cur = remainder//denominator
            remainder = remainder - cur*denominator
            r.append(cur)
            if remainder == 0:
                if negative:
                    return "-"+str(i)+"."+"".join([str(x) for x in r])
                return str(i)+"."+"".join([str(x) for x in r])
            if not(memory.get(remainder) is None):
                if negative:
                    return "-"+str(i)+"."+"".join([str(x) for x in r[:memory[remainder]]])+"("+"".join([str(x) for x in r[memory[remainder]:]])+")"
                return str(i)+"."+"".join([str(x) for x in r[:memory[remainder]]])+"("+"".join([str(x) for x in r[memory[remainder]:]])+")"
            memory[remainder]=len(r)
            remainder*=10
        return str(i)