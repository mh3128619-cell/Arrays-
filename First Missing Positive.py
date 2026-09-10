class Solution(object):
    def firstMissingPositive(self, nums):
        clean_nums = sorted(set(x for x in nums if x > 0))

        target = 1
        for num in clean_nums:
            if num == target:
                target += 1
            elif num > target:
                break

        return target
