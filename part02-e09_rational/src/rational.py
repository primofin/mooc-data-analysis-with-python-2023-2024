#!/usr/bin/env python3

class Rational(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = x/y

    def __str__(self):
        return f"{self.x}/{self.y}"
    
    def __repr__(self):
        return "Rational(%i, %i)" % (self.x, self.y)
    
    def __eq__(self, other):
        return self.x * other.y == self.y * other.x


    def __truediv__(self, other):
        return Rational(self.x * other.y, self.y * other.x)
    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __mul__(self, other):
        return Rational(self.x * other.x, self.y * other.y)

    def __add__(self, other):
        return Rational(self.x * other.y + self.y * other.x, self.y * other.y)

    def __sub__(self, other):
        return Rational(self.x * other.y - self.y * other.x, self.y * other.y)
    
        
def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    # print(r1)
    # print(r2)
    # print(r1*r2)
    # print(r1/r2)
    print(r1+r2)
    # print(r1-r2)
    # print(Rational(1,2) == Rational(2,4))
    # print(Rational(1,2) > Rational(2,4))
    # print(Rational(1,2) > Rational(1,3))
    # print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()


# class Rational:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator

#     def __str__(self):
#         return f"{self.numerator}/{self.denominator}"

#     def __add__(self, other):
#         new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
#         new_denominator = self.denominator * other.denominator
#         return Rational(new_numerator, new_denominator)

#     def __sub__(self, other):
#         new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
#         new_denominator = self.denominator * other.denominator
#         return Rational(new_numerator, new_denominator)

#     def __mul__(self, other):
#         new_numerator = self.numerator * other.numerator
#         new_denominator = self.denominator * other.denominator
#         return Rational(new_numerator, new_denominator)

#     def __truediv__(self, other):
#         new_numerator = self.numerator * other.denominator
#         new_denominator = self.denominator * other.numerator
#         return Rational(new_numerator, new_denominator)

#     def __lt__(self, other):
#         return self.numerator * other.denominator < other.numerator * self.denominator

#     def __gt__(self, other):
#         return self.numerator * other.denominator > other.numerator * self.denominator

#     def __eq__(self, other):
#         return self.numerator * other.denominator == other.numerator * self.denominator

# # Testing the Rational class
# r1 = Rational(1, 4)
# r2 = Rational(2, 3)

# print("r1:", r1)
# print("r2:", r2)
# print("r1 + r2:", r1 + r2)
# print("r1 - r2:", r1 - r2)
# print("r1 * r2:", r1 * r2)
# print("r1 / r2:", r1 / r2)
# print("r1 < r2:", r1 < r2)
# print("r1 > r2:", r1 > r2)
# print("r1 == r2:", r1 == r2)
