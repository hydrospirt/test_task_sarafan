from datetime import datetime as dt
from typing import Generator

from art import art, text2art

VERSION = "prototype v0.1"
TIME = dt.now()


def sequence_generator(sequence_length: int) -> Generator[str, None, None]:
    count = 0
    for i in range(1, sequence_length + 1):
        for j in range(i):
            count += 1
            if count > sequence_length:
                return
            yield str(i)


if __name__ == "__main__":
    logo = text2art("sequence generator")
    print("_" * 110)
    print(logo)
    print(VERSION, "/", TIME)
    print("_" * 110)
    print("")
    while True:
        n = input("> Введите положительное целое число: ")
        n = n.strip()
        if n.isdigit():
            n = int(n)
            break
        else:
            print(f"> {n} - это не положительное целое число. "
                  + "Попробуйте снова.")
            print(art("sad1", number=3, space=5))
print("".join(sequence_generator(n)))
