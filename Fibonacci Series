class Fibonacci:

    def __init__(self, stop=100):
        self.num1 = 0
        self.num2 = 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.num1 > self.stop:
            raise StopIteration
        num = self.num1
        self.num1, self.num2 = self.num2, self.num1 + self.num2
        return num


f1 = Fibonacci()
# for i in f1:
#     print(i)
# for loop internal

iter_obj = iter(f1)

while True:
    try:
        print(iter_obj.__next__())
    except StopIteration:
        break
