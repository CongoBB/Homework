class StepValueError(ValueError):
    pass


class EndpointValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError
        elif step > 0 and start > stop or step < 0 and stop > start or start == stop:
            raise EndpointValueError
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.current_pos = self.pointer
        if self.step > 0 and self.pointer <= self.stop or self.step < 0 and self.pointer >= self.stop:
            self.pointer += self.step

        elif self.step > 0 and self.pointer > self.stop or self.step < 0 and self.pointer < self.stop or \
                self.pointer == self.stop:
            raise StopIteration()
        return self.current_pos

try:
    c = Iterator(1, 2, -1)
except StepValueError:
    print('')
except EndpointValueError:
    print('Введены некорректные значения')

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
    for i in iter5:
        print(i, end=', ')
except EndpointValueError:
    print('Введены некорректные значения')


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=', ')
print()
for i in iter4:
    print(i, end=', ')
print()
