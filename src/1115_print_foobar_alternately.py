from threading import Event

class FooBar:
    def __init__(self, n):
        self.event1 = Event()
        self.event1.set()
        self.event2 = Event()
        self.n = n


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.event1.wait()
            printFoo()
            self.event1.clear()
            self.event2.set()
        self.event1.set()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.event2.wait()
            printBar()
            self.event2.clear()
            self.event1.set()
        self.event2.clear()