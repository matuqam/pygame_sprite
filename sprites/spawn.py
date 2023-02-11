'''Used for span data
When a new Rect (or other object ?) is created, a usefull information is to
know where it should be placed.
This class will hold information on whre items should be placed.'''

class Pos:
    '''Holds coordinates'''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Strategy:
    '''Logic for positioning spawned objects
    with each subsequent call it returns the next Pos to use for spawning'''
    # Different strategies
    # * use static position
    # * dynamic position; recalculate position based on algorithm
    # * use first available position in sequence (reusable positions)
    # * use next position in predetermined sequence (delete after each use )
    def __init__(self):
        raise NotImplementedError

class Spawn:
    '''holds spawn points by type
    when new instance of a given type is created, this will return an
    appropriate Pos for it. A spawn `strategy` will help make this decision'''
    def __init__(self, type):
        raise NotImplementedError
