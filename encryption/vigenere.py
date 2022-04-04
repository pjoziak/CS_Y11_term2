from encryption.cypher import Cypher


class VigenereCypher(Cypher):

    def encrypt(self, message: str) -> str:
        return message

    def decrypt(self, message: str) -> str:
        return message