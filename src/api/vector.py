#a Vector api part
import math

class Vector:
    def __init__(self, x, y, z, w=1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def length(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)

    def multiplyVector(self, other):
        x = self.y * other.z - self.z*other.y
        y = self.z * other.x - self.x*other.z
        z = self.x * other.y - self.y*other.x

        return Vector(x, y, z)

    def __mul__(self, other):
        # scalar
        if type(other) in [int, float]:
            self.x *= other
            self.y *= other
            self.z *= other
        # vector
        elif type(other) == Vector:
            return self.multiplyVector(other)
        return self

    def normilize(self):
        length = self.length()

        self.x /= length
        self.y /= length
        self.z /= length

        return self

    def __repr__(self):
        return f'Vector {self.x} {self.y} {self.z} {self.w}'

    # useful vectors

    @classmethod
    def Forward(cls):
        return Vector(0, 0, -1, 0)
    @classmethod
    def Right(cls):
        return Vector(1, 0, 0, 0)

