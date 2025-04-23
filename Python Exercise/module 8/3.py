# Dogello, RJ-Mel B.
#BSIT 2D

#MODULE 7
#Define a class called MyRange that acts as an iterator and generates numbers f
# rom a start value to an end value (inclusive). Implement the __iter__() and __next__()
#  methods to iterate through the range.

class MyRange:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.stop:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

my_range = MyRange(1, 5)
for num in my_range:
    print(num, end=" ")








