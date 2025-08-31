        :rtype: List[List[int]]
        """
        transpose = [[matrix[j][i] for j in range(len(matrix))]
             for i in range(len(matrix[0]))]
        return transpose 
        :type matrix: List[List[int]]
        """
    def transpose(self, matrix):