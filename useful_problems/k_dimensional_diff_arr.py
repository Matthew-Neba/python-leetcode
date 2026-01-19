
"""
    CORE IDENTITY (difference arrays in ANY dimension)

    --------------------------------------------------
    1D (difference array):

        a[i] =
            sum_{0 <= x <= i} diff[x]

    --------------------------------------------------
    2D (difference array):

        A[i][j] =
            sum_{0 <= x <= i, 0 <= y <= j} diff[x][y]

    - Thus we update the four corners accordindly to make this true when doing the query update
    --------------------------------------------------
    kD (general case):

        A[i1, i2, ..., ik] =
            sum_{0 <= x1 <= i1}
            sum_{0 <= x2 <= i2}
            ...
            sum_{0 <= xk <= ik}
            D[x1, x2, ..., xk]

        - same identity
        - same logic
        - same inclusion–exclusion principle

    - Thus we update the four corners accordindly to make this true when doing the query update
    
"""