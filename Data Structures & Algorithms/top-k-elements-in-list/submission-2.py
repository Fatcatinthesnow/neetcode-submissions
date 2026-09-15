class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter
        count = Counter(nums)
        count = count.most_common(k)
        return [key for key, values in count]
