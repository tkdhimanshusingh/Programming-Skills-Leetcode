class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        s11=list(s1)
        s22=list(s2)
        s11.sort()
        s22.sort()
        if s11!=s22:
            return False
        else:
            cnt=0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    cnt+=1
            if cnt==2:
                return True
            print(cnt)
            return False