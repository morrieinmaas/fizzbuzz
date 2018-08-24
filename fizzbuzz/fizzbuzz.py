import argparse

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


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", type=int, required=True,
                        help="starting point")
    parser.add_argument("-e", "--end", type=int, default=None,
                        help="endpoint")
    args = parser.parse_args()

    f = FizzBuzz(args.start, args.end)

    for i in f:
        print(i)

if __name__ == "__main__":
   main()

