#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#


# @lc code=start
class Solution:
    def intervalIntersection(self, A: List[List[int]],
                             B: List[List[int]]) -> List[List[int]]:
        ia = 0
        ib = 0
        res = []
        while ia < len(A) and ib < len(B):
            # 没有交集的两种情况
            # a2 < b1， 推进ia
            if A[ia][-1] < B[ib][0]:
                ia += 1
                continue
            # b2 < a1， 推进ib
            if A[ia][0] > B[ib][-1]:
                ib += 1
                continue

            # 有交集的四种情况
            left = max(A[ia][0], B[ib][0])
            right = min(A[ia][-1], B[ib][-1])
            res.append([left, right])
            if A[ia][-1] < B[ib][-1]:
                ia += 1
            else:
                ib += 1

        return res


# @lc code=end
