from threading import Event
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.enumber = Event()
        self.enumber.set()
        self.efizz = Event()
        self.ebuzz = Event()
        self.efizzbuzz = Event()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(self.n // 3 - self.n // 15):
            self.efizz.wait()
            printFizz()
            self.efizz.clear()
            self.enumber.set()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n // 5 - self.n // 15):
            self.ebuzz.wait()
            printBuzz()
            self.ebuzz.clear()
            self.enumber.set()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n // 15):
            self.efizzbuzz.wait()
            printFizzBuzz()
            self.efizzbuzz.clear()
            self.enumber.set()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.enumber.wait()
            if i % 15 == 0:
                self.enumber.clear()
                self.efizzbuzz.set()
            elif i % 5 == 0:
                self.enumber.clear()
                self.ebuzz.set()
            elif i % 3 == 0:
                self.enumber.clear()
                self.efizz.set()
            else:
                printNumber(i)
                i += 1