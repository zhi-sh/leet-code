#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#


# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = []
        queue.append('0000')

        # 记录需要跳过的死亡密码
        deads = set()
        for s in deadends:
            deads.add(s)

        # 记录访问过的密码，防止走回头路
        visited = set()
        visited.add('0000')

        step = 0
        while queue:
            sz = len(queue)
            for _ in range(sz):
                s = queue.pop(0)
                
                # 判断是否到达终点
                if s in deads:
                    continue
                if s == target:
                    return step

                cur = [int(_) for _ in s]
                for j in range(4):
                    up = self.plusOne(cur.copy(), j)
                    if up not in visited:
                        queue.append(up)
                        visited.add(up)
                    down = self.minusOne(cur.copy(), j)
                    if down not in visited:
                        queue.append(down)
                        visited.add(down)
            step += 1
        return -1  # 如果穷尽可能，仍未有解

    # 将s[j]向上拨动一次
    def plusOne(self, s, j: int):
        if s[j] == 9:
            s[j] = 0
        else:
            s[j] += 1
        return f"{s[0]}{s[1]}{s[2]}{s[3]}"

    # 将s[j]向下拨动一次
    def minusOne(self, s, j: int):
        if s[j] == 0:
            s[j] = 9
        else:
            s[j] -= 1
        return f"{s[0]}{s[1]}{s[2]}{s[3]}"


# @lc code=end
