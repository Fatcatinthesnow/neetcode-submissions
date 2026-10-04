class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        product = 1
        specialProduct = 1
        if nums.count(0) >= 2:
            return [0] * len(nums)
        for i in range(len(nums)):
            product*= nums[i]
            if nums[i] == 0:
                continue
            specialProduct*= nums[i]
        for i in range(len(nums)):
            if nums[i] == 0:
                answer.append(specialProduct)
                continue
            value = product//nums[i]
            answer.append(value)
        return answer
