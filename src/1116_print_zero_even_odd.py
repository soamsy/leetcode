from threading import Event
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.e1 = Event()
        self.e1.set()
        self.e2 = Event()
        self.e3 = Event()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.e1.wait()
            printNumber(0)
            self.e1.clear()
            if i % 2 != 0:
                self.e2.set()
            else:
                self.e3.set()

        self.e1.set()
        
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.e2.wait()
            printNumber(i)
            self.e2.clear()
            self.e1.set()
        self.e2.clear()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.e3.wait()
            printNumber(i)
            self.e3.clear()
            self.e1.set()
        self.e3.clear()