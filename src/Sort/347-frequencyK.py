class Solution(object):
    def topKFrequent(self, nums, k):
        """
        给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1
        d = sorted(nums_dict.items(), key=lambda num: num[1], reverse=True)
        d = [x[0] for x in d]
        return list(d[:k])