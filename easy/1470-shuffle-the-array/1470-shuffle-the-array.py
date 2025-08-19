        result=[]
        arr1=nums[:n]
        """
        :rtype: List[int]
        arr2=nums[n:]
        for pair in zip(arr1,arr2):
            for j in pair:
                result.append(j)
        return result
        