class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = [] #heap
        counter = {} #hashmap
        for n in nums:
            counter[n] = 1 + counter.get(n, 0) #default values of counter is 0
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))

        res=[]
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res