# string = input()
# string = string.upper()
# print(string)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"({self.x}, {self.y})"

# Example usage:
point = Point(3, 4)
print("Original Point:", point)

point.move(2, 3)
print("After move:", point)
