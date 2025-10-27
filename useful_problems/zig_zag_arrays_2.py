class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        # n here is really large, dp + prefix sum technique will not work
        #
        # we have a linear dp recurrence that uses the same space for all iterations, 
        # we can use the matrix exponentiation trick here. Will be instead log(n)

        def mat_mul(A, B, MOD):
            # compute A * B
            ROWS, COLS, OFFSET = len(A), len(B[0]), len(B)

            res = [[0] * COLS for _ in range(ROWS)]
            for r in range(ROWS):
                for offset in range(OFFSET):
                    if A[r][offset]:
                        for c in range(COLS):
                            res[r][c] += (A[r][offset] * B[offset][c]) % MOD

            return res

        def mat_expo(A, n, MOD):
            ROWS, COLS = len(A), len(A[0])
            # initialize to identity matrix
            res = [[0] * COLS for _ in range(ROWS)]
            for i in range(ROWS):
                res[i][i] = 1

            while n > 0:
                if n & 1:
                    res = mat_mul(res, A, MOD)
                
                A = mat_mul(A,A,MOD)
                n >>= 1
            
            return res


        vals = r - l + 1
        k = 2 * vals

        # upper vals are for up streak, lower vals are for down streak
        state_vector = [[1] for _ in range(k)]
        mat = [[0] * k for _ in range(k)]

        # build the state transition matrix
        # first handle the upper half of the matrix (up)
        for up in range(vals):
            for down in range(up+1, vals):
                mat[up][down + vals] = 1
        
        # then handle lower half of the matrix (down)
        for down in range(vals):
            for up in range(down):
                mat[down + vals][up] = 1

        # now do the compute the n-1 state transition matrix
        A = mat_expo(mat, n - 1, MOD)
        new_state_vector = mat_mul(A, state_vector, MOD)

        res = sum(row[0] for row in new_state_vector) % MOD
        return res




        