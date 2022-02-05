from threading import Thread, Barrier, Semaphore
class H2O:
    def __init__(self):
        self.barrier = Barrier(3)
        self.h_semaphore = Semaphore(2)
        self.o_semaphore = Semaphore(1)
        pass


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_semaphore.acquire()
        self.barrier.wait()
        releaseHydrogen()
        self.h_semaphore.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_semaphore.acquire()
        self.barrier.wait()
        releaseOxygen()
        self.o_semaphore.release()

# h20 = H2O()
# releaseH = lambda: print("H", end="")
# releaseO = lambda: print("O", end="")
# t1 = Thread(target = h20.hydrogen, args = (releaseH,))
# t2 = Thread(target = h20.hydrogen, args = (releaseH,))
# t3 = Thread(target = h20.oxygen, args = (releaseO,))
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()