class Cube:
    def __init__(self, weight, right=None, up=None, down=None, left=None, back=None, front=None):
        self.weight = weight
        self.up = 6 if not up else up
        self.down = 1 if not down else down
        self.right = 2 if not right else right
        self.left = 3 if not left else left
        self.back = 4 if not back else back
        self.front = 5 if not front else front

    def __repr__(self):
        return "[{} {} {} {} {} {} {} ]".format(self.weight,
                                                    self.up, self.down, self.left, self.right, self.back, self.front)
