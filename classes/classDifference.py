class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        self.__elements.sort()
        result = abs(self.__elements[0]-self.__elements[-1])
        self.maximumDifference = result

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)