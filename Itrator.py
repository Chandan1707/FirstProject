
class PowTwo:
    def __init__(self, max):
        self.max = max
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.max:
            raise StopIteration
        val = self.num
        self.num += 1
        return val*val


c1 = PowTwo(10)
it = iter(c1)
c2 = PowTwo(12)
while True:
    try:
        print(c1.__next__())
    except StopIteration:
        break

for i in c2:
    print(i)
