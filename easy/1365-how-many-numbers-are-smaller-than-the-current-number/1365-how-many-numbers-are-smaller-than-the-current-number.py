        """
        result=[]
        for i in nums:
            for j in range(len(nums)):
                if i>nums[j]:
                    count+=1
            result.append(count)
        return result
        
            count=0