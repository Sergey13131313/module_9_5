class StepValueError(Exception):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if (step > 0 and start > stop) or (step < 0 and start < stop):
            raise StepValueError('Шаг указан неверно')

        self.start = start
        self.stop = stop
        self.pointer = start
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        else:
            self.step = step

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        value = self.pointer
        self.pointer += self.step
        if self.step < 0 and self.pointer < self.stop:
            raise StopIteration
        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration
        return value


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
try:
    iter5 = Iterator(10, 1)
except StepValueError:
    print('Шаг указан неверно')

a = iter2.__iter__()

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()

try:
    for i in iter5:
        print(i, end=' ')
    print()
except:
    print('Шаг указан неверно')


aa = 11
