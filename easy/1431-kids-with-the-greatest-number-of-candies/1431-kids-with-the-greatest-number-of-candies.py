    
        """
        :rtype: List[bool]
        :type extraCandies: int
        :type candies: List[int]
        """
        max_val=max(candies)
    def kidsWithCandies(self, candies, extraCandies):
class Solution(object):
        return list(map(lambda x: x+extraCandies>=max_val,candies))