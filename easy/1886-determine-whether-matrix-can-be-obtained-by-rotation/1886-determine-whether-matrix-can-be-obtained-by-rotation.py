        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        for _ in range(4): 
            if mat == target: return True
            mat = [list(x) for x in zip(*mat[::-1])]
        return False 