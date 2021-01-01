import random
class Node:
    def __init__(self,val,left=None,right=None,up=None,down=None):
        self.val = val
        self.left = left
        self.right = right
        self.up = up
        self.down = down
            
class Skiplist:
    

    def __init__(self):
        self.root = None
        self.level = 1
        self.size = 0
    
    def randomLevel(self,maxLevel):
        l = 1
        while l<maxLevel and random.random()<0.5:
            l+=1
        return l

    def search(self, target: int) -> bool:
        cur = self.root
        while cur:
            if cur.val==target:
                return True
            if cur.val>target:
                return False
            else:
                if cur.right is None or cur.right.val>target:
                    cur=cur.down
                else:
                    cur=cur.right
        if cur is None:
            return False

    def add(self, num: int) -> None:
        self.size+=1
        if self.root is None:
            self.root = Node(num,None,None,None,None)
            return
        if self.size>(1<<(self.level-1)):
            self.root = Node(self.root.val,None,None,None,self.root)
            self.root.down.up = self.root
            self.level+=1
        cur = self.root
        if cur.val>num:
            target = cur.val
            while cur:
                cur.val = num
                cur = cur.down
            self.size-=1
            self.add(target)
            return
        print(self.size,self.level)
        while cur:
            while cur.right and cur.right.val<=num:
                cur=cur.right
            if cur.down:
                cur=cur.down
            else:
                break
        cur.right = Node(num,cur,cur.right,None,None)
        newNode = cur.right
        if newNode.right:
            newNode.right.left = newNode
        newLevel = self.randomLevel(self.level-1)
        while newLevel>1:
            print(cur.val,cur.up)
            while cur.up is None:
                print(cur.val,cur.up)
                cur=cur.left
            cur = cur.up
            cur.right = Node(num,cur,cur.right,None,newNode)
            temp = cur.right
            if temp.right:
                temp.right.left = temp
            newNode.up = temp
            newNode=temp
            newLevel-=1
        return
        

    def erase(self, num: int) -> bool:
        if self.size ==0:
            return False
        if self.size == 1:
            if self.root.val==num:
                self.root=None
                self.size=0
                return True
            else:
                return False
        if self.root.val == num:
            cur = self.root
            while cur.down:
                cur = cur.down
            target = cur.right.val
            temp = cur.right
            while temp:
                cur.right = temp.right
                if temp.right:
                    temp.right.left = cur
                cur.val = temp.val
                cur=cur.up
                temp = temp.up
            while cur:
                cur.val = target
                cur = cur.up
            self.size-=1
            if self.size<=(1<<(self.level-2)):
                self.level-=1
            return True
        cur = self.root
        if num<cur.val:
            return False
        while cur and cur.val!=num:
            while cur.right and cur.right.val<=num:
                cur = cur.right
            if cur.down:
                cur = cur.down
            else:
                if cur.val!=num:
                    return False
        if cur is None or cur.val!=num:
            return False
        while cur.down:
            cur = cur.down
        while cur:
            cur.left.right = cur.right
            if cur.right:
                cur.right.left = cur.left
            cur = cur.up
        self.size-=1
        if self.size<=(1<<(self.level-2)):
            self.level-=1
        return True
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)