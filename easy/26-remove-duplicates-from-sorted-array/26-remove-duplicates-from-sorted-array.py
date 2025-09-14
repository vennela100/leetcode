        :rtype: int
        """
        :type nums: List[int]
        """
    def removeDuplicates(self, nums):
        nums[:]=sorted(set(nums))
        return len(nums)
        