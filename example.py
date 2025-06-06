from typing import Any, Callable, TypeVar, Generic
import time

from decoratorbasic import (
    DecoratorBasic, get_decorator_callable, get_decorators
)
TCallable = TypeVar('TCallable', bound=Callable)    

class TimerDecorator(DecoratorBasic[TCallable], Generic[TCallable]):
    def definator(self, callable:TCallable):
        print(f"Add Decorator '{callable.__name__}': '{self.__class__.__name__}'")
        return callable

    def decorator(self, callable:TCallable, *args, **kwargs):
        self.start = time.time()
        result = callable(*args, **kwargs)
        self.end = time.time()
        print(f"Result '{callable.__name__}': {self.end - self.start}")
        return result

@TimerDecorator()
def test_range(start:int, stop:int):
    for n in range(start, stop): ...

@TimerDecorator()
class testo:
    def __init__(self):
        for n in range(1, 10000000):...

test_range(1,4000000)

print('DecoratorFunction: {}; BaseFuntion: {}'.format(test_range, get_decorator_callable(test_range)))

print('Decorators: {}'.format(str(get_decorators(test_range))))

testo()
