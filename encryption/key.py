DEADLINE = '2022-04-18'


class Key:
    def __init__(self, key: str):  # dunder method == double underscore
        self.key = ''.join(c for c in key if c.isalpha()).upper()
        self.counter = 0
        self.length = len(self.key)

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        return f'Key(key={self.key})'

    def __iter__(self) -> str:  # to allow infinite wrap-around
        while True:
            if self.counter >= self.length:
                self.counter = 0
            self.counter += 1
            yield self.key[self.counter - 1]
