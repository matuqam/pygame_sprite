'''
This module contains the selection logic for the prites

contain logic to determine when to get next sprite
contain logic to determin how long each sprite show show
contain logic for
    sprite selection via
        ex.:
            by name
            by index
            by general rule
    based on specified logic recieved
        ex.:
            variable has/does not have value
            expression is `True`
        for now will use variables with target values to (not) have
        future options
            use iterables with (does not) (x amounts) contain(s),
            is (not) smallest/largest


'''

from typing import List, Tuple, Any, Literal
import operator

class Loader:
    '''
    sprites
    '''
    def __init__(self):
        pass

    def get_next_sprite(self):
        pass


class Predicate:
    def __init__(self, name: str=None, value: Any=None, comparator: Any=None, operation: operator=None):
        self.name = name
        self.value = value
        self.comparator = comparator
        self.operation = operation

    def evaluate(self, new_value:Any=None, comparator:Any=None, operation: Any=None):
        self.value = new_value if new_value is not None else self.value
        self.comparator = comparator if comparator is not None else self.comparator
        self.operation = operation if operation is not None else self.operation
        if self.operation is operator.contains:
            return self.operation(self.comparator, self.value)
        return self.operation(self.value, self.comparator)


class Predicates:
    def __init__(self, predicates: List[Predicate]=None, operation: operator=None):
        self.predicates = predicates
        self.operation = operation

    def evaluate(self):
        if self.predicates is None:  # No condition for True so default to True
            return True
        return self.operation([predicate.evaluate() for predicate in self.predicates])

