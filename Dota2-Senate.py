from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()
        for i , val in enumerate(senate):
            if val == 'R':
                R.append(i)
            else:
                D.append(i)
        while R and D:
            d_term = D.popleft()
            r_term = R.popleft()
            if r_term < d_term:
                R.append(r_term + len(senate))
            else:
                D.append(d_term + len(senate))

        return 'Radiant' if R else 'Dire'
        