class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a=version1.split(".")
        b=version2.split(".")
        for i in range(max(len(a), len(b))):
            if i<len(a):
                v1=int(a[i])
            else:
                v1=0
            if i<len(b):
                v2=int(b[i])
            else:
                v2=0
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
        return 0