# a Matrix api part

class Matrix:
    def __init__(self, matrix=None):
        self.body = matrix if matrix else [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
    def __mul__(self, other):

        if type(other) == Matrix:
            m = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]

            for i in range(4):
                for j in range(4):
                    m[i][j] = self.body[i][0]*other.body[0][j] + self.body[i][1]*other.body[1][j] + self.body[i][2]*other.body[2][j] + self.body[i][3] * other.body[3][j]

            return Matrix(m)

    def __repr__(self):
        return "Matrix [ \n\t" + str('\n\t'.join(map(str, self.body))) + "\n ]"
