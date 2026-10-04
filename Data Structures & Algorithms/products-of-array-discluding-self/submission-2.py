class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        copy = nums
        for i in range(len(copy)):
            value = 1
            keyNum = copy.pop(i)
            copy.insert(0, keyNum)
            for num in copy[1:]:
                value*= num
            answer.append(value)
        return answer
