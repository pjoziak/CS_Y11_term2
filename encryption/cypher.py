from abc import abstractmethod

from encryption.key import Key


class Cypher:
    def __init__(self, key: Key):
        self.key = key

    @abstractmethod
    def encrypt(self, message: str) -> str:
        raise NotImplemented

    @abstractmethod
    def decrypt(self, message: str) -> str:
        raise NotImplemented
