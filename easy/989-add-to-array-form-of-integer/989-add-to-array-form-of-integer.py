        :rtype: List[int]
        """
        result=[]
        a=int("".join(str(i) for i in num))
        b=a+k
        for i in str(b):
            result .append(int(i))
        return result
        