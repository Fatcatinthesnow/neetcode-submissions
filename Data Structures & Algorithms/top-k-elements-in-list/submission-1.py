class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        arr = []
        for num, cnt in my_dict.items():
            arr.append([cnt, num])
        arr.sort()

        final = []
        while len(final) < k:
            final.append(arr.pop()[1])
        return final
