class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if A>C or B>D:
            A,B,C,D = C,D,A,B
        if E>G or F>H:
            E,F,G,H = G,H,E,F
        ans = (C-A)*(D-B) + (G-E)*(H-F)
        sx = 0
        sy = 0
        if ( (A<=E) and (E<=C) ):
            sx = min(C,G)-E
        if (A<=G) and (G<=C):
            sx = G- max(A,E)
        if E<=A and C<=G:
            sx = C-A
        if ( (B<=F) and (F<=D) ):
            sy = min(D,H)-F
        if (B<=H) and (H<=D):
            sy = H- max(B,F)
        if F<=B and D<=H:
            sy = D-B
        return ans - sx*sy
        
        