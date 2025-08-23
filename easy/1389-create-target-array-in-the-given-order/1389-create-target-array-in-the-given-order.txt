        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in range(0,len(nums)):
        
            result.insert(index[i],nums[i])
        return result