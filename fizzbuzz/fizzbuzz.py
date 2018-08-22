class FizzBuzz:
    """
        This class implements FizzBuzz.
    """
    def __init__(self, start, end=None):
        assert isinstance(start, int), "start not an integer"
        if end is None:
            self.end = start
            self.current = 1
        elif end is not None:
            assert isinstance(end, int), "end not an integer"
            if start > end: 
                self.current = end
                self.end = start
            else:
                self.current = start
                self.end = end

    def __iter__(self):
        return self
    
    def fizz_buzz(self):
        while self.current <= self.end:
            
            if (self.current) % 15 == 0:
                yield 'FizzBuzz'
            elif (self.current) % 5 == 0:
                yield 'Buzz'
            elif (self.current) % 3 == 0:
                yield 'Fizz'
            else:
                yield str( self.current)
            self.current += 1   
                
    def __iter__(self):
        return self.fizz_buzz()
