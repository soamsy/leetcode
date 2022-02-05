from threading import Semaphore
class Foo:
    def __init__(self):
        self.blockSecond = Semaphore(0)
        self.blockThird = Semaphore(0)
        pass

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.blockSecond.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.blockSecond:
            
            printSecond()
            self.blockThird.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.blockThird:
            printThird()