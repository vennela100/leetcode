        currsum=nums[0]
        for i in nums[1:]:
            currsum=max(i,currsum+i)
            globlesum=max(globlesum,currsum)
        globlesum=nums[0]
        return(globlesum)
     
        