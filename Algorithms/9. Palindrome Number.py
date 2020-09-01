class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if (x>=10):
            base = int(math.pow(10,int(math.log10(x))))
        while(x>=10):
            if x//base != x%10:
                return False
            # ox=x
            x=(x-(x//base*base))//10
            if x==0:
                return True
            else:
                new_base = int(math.pow(10,int(math.log10(x))))
            # print(x,new_base,base)
            if(base//new_base>100):
                t=base//new_base//100
                if(x-x//t*t)>0:
                    return False
                x=x//t
                if x==0:
                    return True
                else:
                    base = int(math.pow(10,int(math.log10(x))))
            else:
                base=new_base
        return True
        
        