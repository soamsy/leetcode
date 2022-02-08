def fizzBuzz(self, n: int) -> List[str]:
    return [f"{'Fizz' if i % 3 == 0 else ''}{'Buzz' if i % 5 == 0 else ''}" or str(i) for i in range(1, n + 1)]