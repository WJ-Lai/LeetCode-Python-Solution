class Solution(object):

    # 列表：时间复杂度O(n^2),空间复杂度O(n)
    # 哈希表：时间复杂度O(n),空间复杂度O(n)
    # 数学：时间复杂度O(n),空间复杂度O(n)
    # 位操作：时间复杂度O(n),空间复杂度O(1)

    # 列表：时间复杂度O(n^2),空间复杂度O(n)
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for n in nums:
            if n not in res:
                res.append(n)
            else:
                res.remove(n)
        return res[0]

    # 哈希表：时间复杂度O(n),空间复杂度O(n)
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = {}
        for n in nums:
            try:
                res.pop(n)
            except:
                res[n] = 1
        return res.popitem()[0]

    # 数学：时间复杂度O(n),空间复杂度O(n)
    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums))-sum(nums)

    # 位操作：时间复杂度O(n),空间复杂度O(1)
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res ^= n
        return res
