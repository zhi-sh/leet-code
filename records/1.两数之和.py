#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:
    r'''
        通过遍历List，将遍历过的元素加入字典；
        在遍历时，计算对偶元素是否在字典中，如果在，则说明该target可以分解
    '''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for ix, num in enumerate(nums):
            coup_num = target - num
            if coup_num in maps:
                return [maps[coup_num], ix]
            maps[num] = ix
        return None


# @lc code=end
