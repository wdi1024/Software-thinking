class Vec2:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        msg = "(" + str(self.x) + "," + str(self.y) + ")"
        return msg

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y+other.y)


if __name__ == "__main__":
    q = Vec2(-1, 2)
    p = Vec2(3, 4)
    r = p+q
    print(p)
    print(q)
    print(r)
