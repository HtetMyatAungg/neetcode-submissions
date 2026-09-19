class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        
        
        for n in nums:
            dic[n] += 1
        output = []
        l = []
        n = {key:value for key, value in sorted(dic.items(), key = lambda value:value[1], reverse=True)}

        l = [key for key in n.keys()]
        for i in range(k):
            output.append(l[i])
        return output


