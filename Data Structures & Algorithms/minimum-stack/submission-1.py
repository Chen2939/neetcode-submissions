class MinStack:

    def __init__(self):
        self.inp = []
        self.minRec = []

    def push(self, val: int) -> None:
        self.inp.append(val)
        self.minRec.append(
            min(self.minRec[-1] if self.minRec else float("infinity"), val)
            )

    def pop(self) -> None:
        self.inp.pop()
        self.minRec.pop()

    def top(self) -> int:
        return self.inp[-1]

    def getMin(self) -> int:
        return self.minRec[-1]
