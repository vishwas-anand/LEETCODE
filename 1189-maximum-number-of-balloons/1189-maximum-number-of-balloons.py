class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ctrText = Counter(text)
        print(ctrText)
        cntB, cntA, cntN = ctrText['b'], ctrText['a'], ctrText['n']
        print(cntB, cntA, cntN)
        cntL, cntO = ctrText['l']//2 , ctrText['o'] //2

        return min(cntB, cntA, cntL, cntO, cntN)