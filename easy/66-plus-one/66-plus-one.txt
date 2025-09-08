        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result=int("".join(str(i) for i in digits))+1
        a=list(str(result))
        
        return [int(j) for j in a]
         