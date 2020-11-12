class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # def crossProduct(x1:int,y1:int,x2:int,y2):
        #     return abs(x1*y2-x2*y1)
        side = None
        longer_side = None
        points = [p1,p2,p3,p4]
        for j in range(1,len(points)):
            dis = (points[0][0]-points[j][0])*(points[0][0]-points[j][0])+(points[0][1]-points[j][1])*(points[0][1]-points[j][1])
            if (side is None) or (side == dis):
                side = dis
            elif (longer_side is None) or (longer_side==dis):
                longer_side = dis
        if (side is None) or (longer_side is None):
            return False
        if (side>longer_side):
            side, longer_side = longer_side, side
        if side*2!=longer_side:
            return False

        for i in range(len(points)):
            c1=0
            c2=0
            for j in range(len(points)):
                if i!=j:
                    dis = (points[i][0]-points[j][0])*(points[i][0]-points[j][0])+(points[i][1]-points[j][1])*(points[i][1]-points[j][1])
                    if side == dis:
                        c1+=1
                        if c1>2:
                            return False
                    elif longer_side == dis:
                        c2+=1
                        if c2>1:
                            return False
                    else:
                        return False
        return True